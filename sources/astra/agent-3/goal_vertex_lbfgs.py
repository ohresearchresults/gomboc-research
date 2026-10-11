"""Goal-only unrestricted physical point optimization, with a hard <=84 input bound."""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from persistence_birth import evaluate
from vertex_geometry import geometry
from direct_face_polish import guards
from goal_nomination import preserve


def run(source,out,steps):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);X=np.load(source);assert len(X)<=84;np.save(out/'initial.npy',X);calls=0;start=time.time();history=[]
 for stage,eta in enumerate([.03,.008,.001,.0001]):
  d=out/f'stage{stage:02d}';d.mkdir();best=np.inf
  def fun(flat):
   nonlocal calls,best
   calls+=1;Y=flat.reshape(X.shape)
   try:
    value,G,info=evaluate(Y,eta);g=geometry(Y,False);v,_,cl=guards(g,False)
   except(ValueError,np.linalg.LinAlgError):return 1e5,np.zeros_like(flat)
   if value<best:
    best=value;np.save(d/'best.npy',Y);(d/'best.json').write_text(json.dumps(dict(loss=value,eta=eta,calls=calls,seconds=time.time()-start,P=info['Pmax'],Q=info['Qmax'],**cl),indent=2))
   if cl['S']==cl['U']==1:preserve(Y,d/f'exact_nomination{calls}','unrestricted <=84 physical input points, numerical own110 at actual filled centroid')
   if calls%200==0:print('VERTEX_GOAL_LBFGS',stage,calls,value,info['Pmax'],info['Qmax'],cl,flush=True)
   return value,G.ravel()
  r=minimize(fun,X.ravel(),jac=True,method='L-BFGS-B',bounds=[(-3.,3.)]*X.size,options=dict(maxiter=steps,maxls=60,maxcor=25,ftol=1e-15,gtol=1e-10))
  if (d/'best.npy').exists():X=np.load(d/'best.npy')
  rec=dict(stage=stage,eta=eta,calls=calls,message=str(r.message),iterations=int(r.nit),best=best);history.append(rec);(out/'history.json').write_text(json.dumps(history,indent=2));print('VERTEX_GOAL_STAGE',rec,flush=True)


if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--steps',type=int,default=1200);a=p.parse_args();run(a.source,a.out,a.steps)
