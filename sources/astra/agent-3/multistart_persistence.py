"""Seeded physical vertex exploration from literal own121 J84; no delegation.
Coordinates, parameters, every best stage, and completed trial summaries persist.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,time,argparse
from pathlib import Path
from scipy.spatial import ConvexHull
from scipy.optimize import minimize
from persistence_vertices import evaluate
from search_vertices import evaluate as census

def seedbody(seed,n):
 rng=np.random.default_rng(seed);X=np.load('artifacts/j84_seed.npy').copy();h=ConvexHull(X);g=census(X)[2]['centroid'];X-=g
 # Put spare geometric controls over actual surface triangles, with a reproducible outward offset.
 while len(X)<n:
  k=int(rng.integers(len(h.simplices)));tri=h.simplices[k];weights=rng.dirichlet([1,1,1]);point=weights@X[tri];normal=h.equations[k,:3];point+=normal*rng.uniform(.002,.04);X=np.vstack((X,point))
 noise=[0.,.002,.01,.04,.1][seed%5]
 X+=rng.normal(size=X.shape)*noise
 if seed%4:
  A=np.eye(3)+rng.normal(size=(3,3))*.08;X=X@A.T
 return X,dict(seed=seed,n=n,noise=noise,source='literal J82_S1_ROBUST_G6, native SHA753b899123a05588f7a566b8f08d08cc6e72636fdbd59bca5c7f465f32bea3ab')

def trial(seed,n,steps):
 X,meta=seedbody(seed,n);out=Path(f'artifacts/multistart/n{n}_s{seed}');out.mkdir(exist_ok=False,parents=True);np.save(out/'initial.npy',X);(out/'input.json').write_text(json.dumps(meta,indent=2));calls=0;start=time.time();result=[]
 for stage,eta in enumerate([.02,.002,.0002]):
  folder=out/f'stage{stage}';folder.mkdir();best=1e100
  def fun(z):
   nonlocal calls,best
   calls+=1;x=z.reshape(-1,3);v,G,info=evaluate(x,eta)
   if v<best:
    best=v;np.save(folder/'best.npy',x);(folder/'best.json').write_text(json.dumps(dict(info,calls=calls,eta=eta,elapsed=time.time()-start),indent=2))
   if max(info['Pmax'],info['Qmax'])<1e-11:
    np.save(out/'potential.npy',x);(out/'potential.json').write_text(json.dumps(info,indent=2));print('POTENTIAL_MULTISTART',out,info,flush=True)
   return v,G.ravel()
  r=minimize(fun,X.ravel(),jac=True,method='L-BFGS-B',options={'maxiter':steps,'maxfun':steps*6,'maxls':50,'maxcor':30,'ftol':1e-16,'gtol':1e-11});X=np.load(folder/'best.npy');info=json.load(open(folder/'best.json'));ci=census(X)[2];row=dict(stage=stage,eta=eta,termination=str(r.message),calls=calls,nit=int(r.nit),Pmax=info['Pmax'],Qmax=info['Qmax'],S=ci['S'],U=ci['U'],V=ci['V'],E=ci['E'],F=ci['F']);result.append(row);print('MULTISTART',seed,n,row,flush=True)
  (out/'summary.json').write_text(json.dumps(result,indent=2))
 print('TRIAL_COMPLETE',seed,n,'seconds',time.time()-start,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--seed',type=int,default=35000);p.add_argument('--trials',type=int,default=16);p.add_argument('--steps',type=int,default=5000);a=p.parse_args()
 for seed in range(a.seed,a.seed+a.trials):
  n=[45,55,65,75,85][seed%5];trial(seed,n,a.steps)
