"""Sample the pullback of the genuine volume centroid throughout the material region.
The sampled point is NOT assigned as a reference centre to an unchanged solid.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import sys,json,time,argparse
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from isotropic_metric import IsotropicOrbit

def invert_pullback(m,c):
 X=m.X-c;tri=m.tri;tr0=X[tri];w0=np.einsum('ni,ni->n',tr0[:,0],np.cross(tr0[:,1],tr0[:,2]));assert w0.min()>0
 def state(u):
  d=1+X@u
  if d.min()<=0:raise ArithmeticError('Shifted horizon')
  y=X/d[:,None];tr=y[tri];w=w0/np.prod(d[tri],axis=1);W=w.sum();s=tr.sum(axis=1);g=np.einsum('n,ni->i',w,s)/(4*W)
  second=(np.einsum('n,ni,nj->ij',w,s,s)+np.einsum('n,nai,naj->ij',w,tr,tr))/(20*W)
  K=5*second-4*np.outer(g,g);return g,K,W/6,d
 u=np.zeros(3)
 for it in range(150):
  g,K,V,d=state(u)
  if np.linalg.norm(g,np.inf)<2e-12:break
  du=np.linalg.solve(K,g);dd=X@du;alpha=min(1.,.95*np.min(-d[dd<0]/dd[dd<0]) if (dd<0).any() else 1.);slope=-4*g@du
  for back in range(70):
   uu=u+alpha*du;gg,KK,VV,ddd=state(uu)
   if np.log(VV)<=np.log(V)+1e-4*alpha*slope or np.linalg.norm(gg)<np.linalg.norm(g):u=uu;break
   alpha*=.5
  else:raise ArithmeticError('Pullback centering backtracking exhausted')
 else:raise ArithmeticError('Pullback centering finite iteration budget')
 d0=1-u@c;assert d0>0;t=u/d0;y,b,K,d,V=m.state(t);got=b/(1-t@b);error=float(np.linalg.norm(got-c,np.inf));assert error<1e-8
 return t,b,dict(centering_iterations=it,pullback_error=error,original_min_den=float(d.min()),requested_pullback=c.tolist(),actual_pullback=got.tolist())

def main():
 p=argparse.ArgumentParser();p.add_argument('report');p.add_argument('out');p.add_argument('--centres',type=int,default=400);p.add_argument('--starts',type=int,default=3);p.add_argument('--evals',type=int,default=120);p.add_argument('--seed',type=int,default=720623);a=p.parse_args();out=Path(a.out);out.mkdir(exist_ok=False);m=IsotropicOrbit(a.report);rng=np.random.default_rng(a.seed);prob=m.w0/m.w0.sum();best={};observations=0;fail=0;clock=time.monotonic()
 low=np.array([-1.5,-1.5,-3,-3,-3.]);high=-low
 def observe(z,k,seed):
  nonlocal observations
  v,J,info,data=m.all_data(z);observations+=1;count=(len(info['S']),len(info['U']));score=float(np.minimum(v-1e-5,0)@np.minimum(v-1e-5,0));key=f'S{count[0]}U{count[1]}'
  if sum(count)<=6 and info['condition']<1000 and (key not in best or score<best[key]):
   best[key]=score;rec=dict(info,loss=score,centre_sample=k,metric_start=seed,evaluation=observations);(out/(key+'.json')).write_text(json.dumps(rec,sort_keys=True))
   with (out/'IMPROVEMENTS.jsonl').open('a') as f:f.write(json.dumps(rec,sort_keys=True)+'\n')
   print('BEST',k,seed,count,score,info['condition'],info['min_den'],flush=True)
  if count==(1,1) and info['min_nonroot']>1e-8:
   (out/'NUMERICAL_WINNER.json').write_text(json.dumps(info,sort_keys=True));return True
  return False
 for k in range(a.centres):
  if k==0:c=m.b0.copy()
  elif k==1:c=np.zeros(3)
  elif k<4:c=.7*m.X[m.report['unstable_vertices'][(k-2)%len(m.report['unstable_vertices'])]]
  else:
   tri=m.tri[int(rng.choice(len(m.tri),p=prob))];weights=rng.dirichlet(np.full(4,1. if k%3 else .3));c=weights[1:]@m.X[tri]
   c*=1-2**(-int(rng.integers(7,14)))
  try:
   t,b,receipt=invert_pullback(m,c);m.last_t=t.copy();m.last=None
   with (out/'CENTRES.jsonl').open('a') as f:f.write(json.dumps(dict(sample=k,t=t.tolist(),actual_volume_centroid=b.tolist(),**receipt),sort_keys=True)+'\n')
   for seed in range(a.starts):
    if seed==0:v=np.zeros(5)
    elif seed==1:
     _,g,K,_,_=m.state(t);L=np.linalg.cholesky((K-np.outer(g,g))/5);Q,R=np.linalg.qr(L);R=np.diag(np.sign(np.diag(R)))@R;R/=np.linalg.det(L)**(1/3)
     v=np.array([np.log(R[0,0]),np.log(R[1,1]),R[0,1]/R[0,0],R[0,2]/R[0,0],R[1,2]/R[1,1]])
    else:v=rng.normal(size=5)*.5
    v=np.clip(v,low+1e-5,high-1e-5)
    def res(v):
     z=np.r_[b,v];observe(z,k,seed);return m.residual(z)
    sol=least_squares(res,v,jac=lambda v:m.jacobian(np.r_[b,v])[:,3:],bounds=(low,high),max_nfev=a.evals,loss='soft_l1',f_scale=.03,ftol=1e-10,xtol=1e-11,gtol=1e-11)
    if (out/'NUMERICAL_WINNER.json').exists():break
  except (ArithmeticError,ValueError,np.linalg.LinAlgError,AssertionError) as exc:
   fail+=1;m.last=None;m.last_t=np.zeros(3)
   with (out/'FAILURES.txt').open('a') as f:f.write(str(k)+' '+repr(exc)+'\n')
  if (out/'NUMERICAL_WINNER.json').exists():break
  if k%25==0:print('SAMPLES',k,observations,fail,time.monotonic()-clock,flush=True)
 (out/'CONFIG.json').write_text(json.dumps(vars(a),sort_keys=True));(out/'SUMMARY.json').write_text(json.dumps(dict(samples=k+1,observations=observations,failures=fail,seconds=time.monotonic()-clock),sort_keys=True));print('FINITE_PULLBACK_CENTROID_METRIC_SEARCH_FINISHED',k+1,observations,fail,flush=True)
if __name__=='__main__':main()
