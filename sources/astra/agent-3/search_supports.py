"""Independent support-coordinate search under F<=85, E<=249.
Every loss evaluation rebuilds the physical hull and integrates its own mass.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,time,argparse
from pathlib import Path
from scipy.spatial import ConvexHull
from scipy.optimize import minimize
import search_score as score
core=score.core

def evaluate(Q,eps=1e-5,derivative=True):
 dual=ConvexHull(Q)
 if dual.equations[:,3].max()>=-1e-9:raise ValueError('origin no longer strictly inside support hull')
 X0=-dual.equations[:,:3]/dual.equations[:,3,None]
 _,keep=np.unique(np.round(X0,10),axis=0,return_index=True);keep=np.sort(keep);T=dual.simplices[keep];X=X0[keep]
 value,GX,info=core.evaluate(X,eps,derivative)
 GQ=np.zeros_like(Q)
 if derivative:
  w=np.linalg.solve(np.swapaxes(Q[T],1,2),GX[...,None])[...,0];dQ=-w[:,:,None]*X[:,None,:]
  np.add.at(GQ,T.reshape(-1),dQ.reshape(-1,3))
 return value,GQ,info,X

def run(seed,n,steps,eps):
 rng=np.random.default_rng(seed);Y=np.load('artifacts/c622/seed.npz')['Q'];ids=[3];dist=np.linalg.norm(Y-Y[3],axis=1)
 while len(ids)<n:
  k=int(np.argmax(dist*(.85+.3*rng.random(len(Y)))));ids.append(k);dist=np.minimum(dist,np.linalg.norm(Y-Y[k],axis=1))
 Q=Y[ids].copy()+rng.normal(size=(n,3))*1e-7
 folder=Path(f'artifacts/support_search/{n}_{seed}');folder.mkdir(parents=True,exist_ok=False)
 counter=0;best=1e100;start=time.time()
 def fun(z):
  nonlocal counter,best
  counter+=1;qq=z.reshape(-1,3);value,grad,info,X=evaluate(qq,eps)
  if value<best:
   best=value;np.save(folder/'best_supports.npy',qq);np.save(folder/'best_vertices.npy',X);(folder/'best.json').write_text(json.dumps(dict(info,calls=counter,seed=seed,elapsed=time.time()-start),indent=2)+'\n')
  if counter%200==0:print('SUPPORT',seed,counter,info,flush=True)
  if info['S']==info['U']==1 and min(info['marginV'],info['marginF'])>1e-9:
   np.save(folder/'potential_supports.npy',qq);np.save(folder/'potential_vertices.npy',X);(folder/'potential.json').write_text(json.dumps(info,indent=2));print('POTENTIAL_SUPPORT110',seed,info,flush=True)
  return value,grad.ravel()
 initial=evaluate(Q,eps)[2];print('START',seed,initial,flush=True)
 res=minimize(fun,Q.ravel(),method='L-BFGS-B',jac=True,options={'maxiter':steps,'maxfun':steps*4,'maxls':40,'ftol':1e-16,'gtol':1e-10,'maxcor':30})
 print('FINISH',seed,res.message,json.load(open(folder/'best.json')),flush=True)
 (folder/'termination.json').write_text(json.dumps({'success':bool(res.success),'message':str(res.message),'calls':counter,'iterations':int(res.nit)},indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--seed',type=int,default=32928);p.add_argument('--n',type=int,default=85);p.add_argument('--steps',type=int,default=5000);p.add_argument('--trials',type=int,default=4);p.add_argument('--epsilon',type=float,default=1e-5);p.add_argument('--check',action='store_true');a=p.parse_args()
 if a.check:
  Q=np.random.default_rng(754).normal(size=(25,3));d=np.random.default_rng(755).normal(size=Q.shape);d/=np.linalg.norm(d);v,G,_,_=evaluate(Q)
  for h in [1e-4,1e-5,1e-6]:print(h,(evaluate(Q+h*d,derivative=False)[0]-evaluate(Q-h*d,derivative=False)[0])/(2*h),np.sum(G*d))
 else:
  for seed in range(a.seed,a.seed+a.trials):run(seed,a.n,a.steps,a.epsilon)
