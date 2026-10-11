"""Finite centroid-metric experiments, allowing either critical carrier to change."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import json,sys,time,argparse
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from centroid_metric import CentroidOrbit
from isotropic_metric import IsotropicOrbit

def main():
 p=argparse.ArgumentParser();p.add_argument('report');p.add_argument('out');p.add_argument('--seed',type=int,default=720619);p.add_argument('--starts',type=int,default=300);p.add_argument('--evals',type=int,default=250);p.add_argument('--chart',choices=['raw','isotropic'],default='isotropic');p.add_argument('--loss',choices=['linear','soft_l1','cauchy'],default='cauchy');p.add_argument('--sigma',type=float,default=.01);p.add_argument('--bound',type=float,default=1.2);p.add_argument('--centres',type=float,default=30.);p.add_argument('--prefer',choices=['none','U','S'],default='none');p.add_argument('--forest',type=int,default=0);a=p.parse_args()
 out=Path(a.out);out.mkdir(exist_ok=False);m=(IsotropicOrbit if a.chart=='isotropic' else CentroidOrbit)(a.report)
 z0=np.r_[m.b0,np.zeros(5)]
 if a.chart=='isotropic':
  _,g,K,_,_=m.state(np.zeros(3));C=(K-np.outer(g,g))/5;L=np.linalg.cholesky(C);Q,R=np.linalg.qr(L);R=np.diag(np.sign(np.diag(R)))@R;R/=np.linalg.det(L)**(1/3)
  z0[3:]=[np.log(R[0,0]),np.log(R[1,1]),R[0,1]/R[0,0],R[0,2]/R[0,0],R[1,2]/R[1,1]]
 low=np.r_[np.full(3,-a.centres),np.full(2,-a.bound),np.full(3,-2.)];high=-low
 rng=np.random.default_rng(a.seed);weights=np.ones(sum(m.ns))
 if a.prefer=='U':weights[:m.ns[0]]=10
 if a.prefer=='S':weights[m.ns[0]:]=10
 best=None;records=[];clock=time.monotonic();failed=0
 def record(z,k):
  nonlocal best
  v,J,info,data=m.all_data(z);score=float(np.sum(np.minimum(v-1e-5,0)**2));key=(len(info['S'])+len(info['U']),score)
  info.update(start=k,loss=score)
  records.append(info)
  with (out/'ALL.jsonl').open('a') as f:f.write(json.dumps(info,sort_keys=True)+'\n')
  if best is None or key<best[0]:
   best=(key,z.copy());(out/'BEST.json').write_text(json.dumps(info,sort_keys=True));print('BEST',k,key,info['min_den'],info['condition'],flush=True)
  if len(info['S'])==1 and len(info['U'])==1 and info['min_nonroot']>1e-8:
   (out/'NUMERICAL_WINNER.json').write_text(json.dumps(info,sort_keys=True));print('NUMERICAL_110_REQUIRES_EXACT_AUDITS',flush=True);return True
  return False
 record(z0,-1)
 good=[]
 for k in range(a.starts):
  if k==0:z=z0.copy()
  elif k%5==0:z=best[1]+rng.normal(size=8)*(.003 if k%10==0 else .05)
  elif k%5==1 and good:z=good[int(rng.integers(len(good)))]+rng.normal(size=8)*.1
  elif k%5==2:z=z0+rng.normal(size=8)*10**rng.uniform(-5,-.7)
  else:z=np.r_[rng.normal(size=3)*10**rng.uniform(-1.7,1.5),rng.uniform(-a.bound,a.bound,2),rng.normal(size=3)]
  z=np.clip(z,low+1e-7,high-1e-7)
  try:
   if a.forest:
    for it in range(a.forest):
     ids=m.forest(z,1+(k%2));fw=np.r_[np.full(m.ns[0]-1,weights[0]),np.full(m.ns[1]-1,weights[-1])]
     sol=least_squares(lambda x:m.fixed(x,ids)[0]*fw,z,jac=lambda x:m.fixed(x,ids)[1]*fw[:,None],bounds=(low,high),loss=a.loss,f_scale=a.sigma,max_nfev=a.evals,ftol=1e-10,xtol=1e-11,gtol=1e-11)
     dif=np.linalg.norm(z-sol.x);z=sol.x
     if record(z,k) or dif<1e-8:break
   else:
    sol=least_squares(lambda x:m.residual(x)*weights,z,jac=lambda x:m.jacobian(x)*weights[:,None],bounds=(low,high),loss=a.loss,f_scale=a.sigma,max_nfev=a.evals,ftol=1e-10,xtol=1e-11,gtol=1e-11)
    z=sol.x;record(z,k)
   info=m.all_data(z)[2]
   if len(info['U'])+len(info['S'])<=5:
    good.append(z.copy());good=good[-50:]
   if (out/'NUMERICAL_WINNER.json').exists():break
  except (ArithmeticError,ValueError,np.linalg.LinAlgError) as exc:
   failed+=1;m.last=None;m.last_t=np.zeros(3)
   with (out/'FAILURES.txt').open('a') as f:f.write(str(k)+' '+repr(exc)+'\n')
  if k%25==0:print('STEP',k,'seconds',time.monotonic()-clock,'failures',failed,flush=True)
 (out/'CONFIG.json').write_text(json.dumps(vars(a),sort_keys=True))
 (out/'SUMMARY.json').write_text(json.dumps(dict(attempts=k+1,records=len(records),failures=failed,calls=m.calls,newton_calls=m.newton_calls,seconds=time.monotonic()-clock),sort_keys=True))
 print('FINITE_CENTROID_METRIC_FAMILY_FINISHED',k+1,failed,flush=True)
if __name__=='__main__':main()
