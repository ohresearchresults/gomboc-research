"""Whole-body persistence consolidation with literal physical free vertices."""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from persistence_birth import evaluate
from vertex_geometry import geometry
from support_geometry import escape
from polish_211 import run as repair

def run(source,out,iters,target='211'):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);X=np.load(source);assert len(X)<=84;start=time.time();records=[]
 for stage,eta in enumerate([.01,.001,.0001,.00001]):
  d=out/f'stage{stage}';d.mkdir();np.save(d/'initial.npy',X);best=np.inf;calls=0
  def fun(flat):
   nonlocal best,calls
   calls+=1;Y=flat.reshape(X.shape);v,G,info=evaluate(Y,eta)
   if v<best:
    best=v;np.save(d/'best.npy',Y);info.update(calls=calls,seconds=time.time()-start);(d/'best.json').write_text(json.dumps(info,indent=2))
   if max(info['Pmax'],info['Qmax'])<1e-12:
    np.save(d/f'potential{calls}.npy',Y);print('FREE_CONSOLIDATION_POTENTIAL_REQUIRES_EXACT',d,info,flush=True)
   if calls%1000==0:print('FREE_CONSOLIDATE',stage,calls,info['Pmax'],info['Qmax'],v,flush=True)
   return v,G.ravel()
  r=minimize(fun,X.ravel(),jac=True,method='L-BFGS-B',options=dict(maxiter=iters,maxls=50,maxcor=35,gtol=1e-11,ftol=1e-15));X=np.load(d/'best.npy');(d/'termination.json').write_text(json.dumps(dict(message=r.message,nit=r.nit),indent=2))
  if target=='211':repair(d/'best.npy',d/'strict211',400,1e-6);p=d/'strict211/success.npy'
  else:
   from polish_121 import run as repair121
   repair121(d/'best.npy',d/'strict121',400,1e-6);p=d/'strict121/potential.npy'
  if p.exists():
   yy=np.load(p);inf=evaluate(yy)[2];records.append(dict(stage=stage,result='strict'+target+' numerical',P=inf['Pmax'],Q=inf['Qmax'],path=str(p)));X=yy
  else:records.append(dict(stage=stage,result='strict'+target+' retraction failed',path=str(d/'best.npy')))
  (out/'stages.json').write_text(json.dumps(records,indent=2));print('FREE_CONSOLIDATE_STAGE',records[-1],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--iterations',type=int,default=6000);p.add_argument('--target',choices=['211','121'],default='211');a=p.parse_args();run(a.input,a.out,a.iterations,a.target)
