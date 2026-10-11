"""Full physical continuation without restoring a chosen equilibrium class.

Large eta first approximates the sum of all relative finite bar depths. Later
stages resolve the small features. Every source point remains a free literal
physical coordinate; the mass is integrated on its fresh convex hull. Strict
repair is a separate final experiment, never an intervening constraint.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from persistence_birth import evaluate
from vertex_geometry import geometry
from polynomial_body_search import features

def run(source,out,seed,perturb,steps):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);g=geometry(np.load(source),False);X=g['Z'][g['vertices']];assert len(X)<=84;X/=np.max(np.linalg.norm(X,axis=1));rng=np.random.default_rng(seed)
 if perturb:
  F=features(X);F-=F.mean(0);u,s,v=np.linalg.svd(F,full_matrices=False);X+=u@rng.normal(size=(u.shape[1],3))*perturb*np.sqrt(len(X)/u.shape[1])
 np.save(out/'initial.npy',X);(out/'definition.json').write_text(json.dumps(dict(source=source,seed=seed,perturb=perturb,uniform_mass=True,no_intermediate_equilibrium_class_repair=True),indent=2));records=[];start=time.time()
 for stage,eta in enumerate([1.,.3,.1,.03,.01,.003,.001,.0001,.00001]):
  d=out/f'stage{stage}';d.mkdir();np.save(d/'initial.npy',X);best=np.inf;calls=0
  def fun(flat):
   nonlocal best,calls
   calls+=1;Y=flat.reshape(X.shape);value,G,info=evaluate(Y,eta)
   if value<best:
    best=value;np.save(d/'best.npy',Y);info.update(calls=calls,seconds=time.time()-start);(d/'best.json').write_text(json.dumps(info,indent=2))
   if max(info['Pmax'],info['Qmax'])<1e-12:
    np.save(d/f'potential{calls}.npy',Y);print('UNRESTRICTED_POTENTIAL_REQUIRES_EXACT',d,info,flush=True)
   return value,G.ravel()
  r=minimize(fun,X.ravel(),jac=True,method='L-BFGS-B',options=dict(maxiter=steps,maxfun=10*steps,maxls=60,maxcor=40,gtol=1e-11,ftol=1e-16));X=np.load(d/'best.npy');info=evaluate(X,eta)[2];row=dict(stage=stage,eta=eta,message=r.message,calls=calls,nit=r.nit,Pmax=info['Pmax'],Qmax=info['Qmax'],P_count=len(info['P']),Q_count=len(info['Q']),V=info['V'],seconds=time.time()-start);records.append(row);(d/'termination.json').write_text(json.dumps(row,indent=2));(out/'stages.json').write_text(json.dumps(records,indent=2));print('UNRESTRICTED_STAGE',out,row,flush=True)
 np.save(out/'final.npy',X)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--seed',type=int,default=75000);p.add_argument('--perturb',type=float,default=0.);p.add_argument('--steps',type=int,default=5000);a=p.parse_args();run(a.input,a.out,a.seed,a.perturb,a.steps)
