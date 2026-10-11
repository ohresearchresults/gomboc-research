"""Finite affine deformation of an entire dying radial component and optional collar.
All convex hulls remain within50 submitted vertices; own centroid and both barcodes
are recomputed. The bounded DE family is a discovery experiment, not an exclusion.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,time,argparse
from pathlib import Path
from scipy.optimize import differential_evolution,minimize
from vertex_geometry import geometry
from constrained_p_flow import feature
from persistence_birth import evaluate

def component(X,collar):
 g=geometry(X,False);val,_,roots,se=feature(g,False);Z=g['Z'];T=g['T'];edges=np.unique(np.sort(np.concatenate([T[:,[0,1]],T[:,[1,2]],T[:,[2,0]]]),axis=1),axis=0);i,j=edges.T;e=Z[j]-Z[i];t=np.clip(-np.sum(Z[i]*e,axis=1)/np.sum(e*e,axis=1),0,1);death=np.sum((Z[i]+t[:,None]*e)**2,axis=1);kk=np.where(np.all(edges==se,axis=1))[0][0];level=death[kk];B={roots[1]};todo=[roots[1]]
 while todo:
  u=todo.pop()
  for (a,b),d in zip(edges,death):
   if d<=level+1e-12:continue
   v=b if a==u else a if b==u else None
   if v is not None and v not in B:B.add(int(v));todo.append(int(v))
 assert roots[0] not in B
 weights=np.zeros(len(X));weights[list(B)]=1
 if collar:
  for a,b in edges:
   if a in B and b not in B:weights[b]=.5
   if b in B and a not in B:weights[a]=.5
 weights[roots[0]]=0
 return weights,dict(component=sorted(B),weights=weights.tolist(),roots=roots,saddle=se,relative_basin=val)

def run(seed,collar,bound,iters):
 X=np.load('artifacts/polish121_1/exact_g9/hull_float.npy');w,meta=component(X,collar);center=np.average(X,axis=0,weights=w);basis=np.zeros((len(X),3,12))
 for a in range(3):
  for b in range(3):basis[:,a,3*a+b]=w*(X[:,b]-center[b])
  basis[:,a,9+a]=w
 out=Path(f'artifacts/finite_basin/s{seed}_c{collar}_b{bound:g}');out.mkdir(exist_ok=False,parents=True);meta.update(seed=seed,collar=collar,bound=bound,maxiter=iters);(out/'input.json').write_text(json.dumps(meta,indent=2));np.save(out/'initial.npy',X);np.save(out/'basis.npy',basis);calls=0;best=1e100;start=time.time()
 def fun(theta,jac=False):
  nonlocal calls,best
  calls+=1;Y=X+np.einsum('icp,p->ic',basis,theta);v,G,info=evaluate(Y,eta=.01);grad=np.einsum('ic,icp->p',G,basis)
  if v<best:
   best=v;np.save(out/'best_params.npy',theta);np.save(out/'best.npy',Y);(out/'best.json').write_text(json.dumps(dict(info,calls=calls,elapsed=time.time()-start),indent=2))
  if max(info['Pmax'],info['Qmax'])<1e-11:
   np.save(out/'potential.npy',Y);(out/'potential.json').write_text(json.dumps(info,indent=2));print('POTENTIAL_FINITE_BASIN110',out,info,flush=True)
  return (v,grad) if jac else v
 rng=np.random.default_rng(seed);init=rng.uniform(-bound,bound,size=(96,12));init[0]=0
 de=differential_evolution(fun,[(-bound,bound)]*12,maxiter=iters,popsize=8,init=init,seed=seed,polish=False,tol=1e-7,atol=1e-9,updating='immediate')
 bestp=np.load(out/'best_params.npy');res=minimize(lambda t:fun(t,True),bestp,jac=True,method='L-BFGS-B',bounds=[(-bound,bound)]*12,options={'maxiter':3000,'maxls':50,'ftol':1e-15,'gtol':1e-10})
 print('FINITE_BASIN_DONE',out,de.message,res.message,json.load(open(out/'best.json')),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--seed',type=int,default=36000);p.add_argument('--iterations',type=int,default=400);a=p.parse_args()
 for collar in [0,1]:
  for bound in [.15,.4,.8]:run(a.seed+collar*3+int(10*bound),collar,bound,a.iterations)
