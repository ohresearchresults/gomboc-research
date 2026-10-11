import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,argparse,time
from pathlib import Path
from scipy.optimize import minimize
from symmetric_search import shape
from persistence_vertices import evaluate

def run(initial,out,steps):
 source=Path(initial);meta=json.load(open(source/'input.json'));p=np.load(source/'initial_params.npy');K,m,a=meta['K'],meta['m'],meta['a'];out=Path(out);out.mkdir(exist_ok=False,parents=True);(out/'input.json').write_text(json.dumps(meta,indent=2));np.save(out/'initial_params.npy',p);bounds=[b for _ in range(K) for b in [(-a+1e-5,.99999),(-2,2),(-2,2)]]+[(.02,2)]
 calls=0;t0=time.time()
 for stage,eta in enumerate([.05,.005,.0005]):
  best=1e100;folder=out/f'stage{stage}';folder.mkdir()
  def fun(x):
   nonlocal calls,best
   calls+=1;X,U=shape(x,K,m,a);v,G,info=evaluate(X,eta);GP=G[1:1+K]+G[1+K:1+2*K]*[1,-1,-1];gr=np.sum(G[-m:,1:]*U);grad=np.r_[GP.ravel(),gr]
   if v<best:
    best=v;np.save(folder/'best_params.npy',x);np.save(folder/'best.npy',X);(folder/'best.json').write_text(json.dumps(dict(info,calls=calls,eta=eta,elapsed=time.time()-t0),indent=2))
   if calls%1000==0:print('SYM_PERSIST',out,stage,calls,{k:info[k] for k in ['V','loss','Pmax','Qmax']},flush=True)
   if max(info['Pmax'],info['Qmax'])<1e-12:
    np.save(out/'potential_params.npy',x);np.save(out/'potential.npy',X);(out/'potential.json').write_text(json.dumps(info,indent=2));print('POTENTIAL_SYM_PERSIST',out,info,flush=True)
   return v,grad
  r=minimize(fun,p,jac=True,method='L-BFGS-B',bounds=bounds,options={'maxiter':steps,'maxfun':steps*6,'maxls':50,'maxcor':40,'ftol':1e-15,'gtol':1e-10});p=np.load(folder/'best_params.npy');print('DONE_SYM_PERSIST',out,stage,r.message,json.load(open(folder/'best.json')),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--steps',type=int,default=5000);a=p.parse_args()
 for source in sorted(Path('artifacts/symmetric').iterdir()):
  run(source,Path('artifacts/symmetric_persistence')/source.name,a.steps)
