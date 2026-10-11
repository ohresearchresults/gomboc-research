"""Global finite physical polynomial warps of <=84 hull vertices.
The convex hull of the warped literal points is the uniformly filled body;
mass is recomputed there. Polynomial maps are not presumed volume preserving.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import differential_evolution,minimize
from vertex_geometry import geometry
from persistence_birth import evaluate
from support_geometry import escape

def features(X):
 x,y,z=X.T;return np.column_stack((x*x,y*y,z*z,x*y,x*z,y*z,x**3,y**3,z**3,x*x*y,x*x*z,y*y*x,y*y*z,z*z*x,z*z*y,x*y*z))
def run(source,out,seed,iterations,eta):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);g=geometry(np.load(source),False);X=g['Z'][g['vertices']];assert len(X)<=84;X/=np.max(np.linalg.norm(X,axis=1));F=features(X);F-=F.mean(0);F/=np.sqrt(np.mean(F*F,axis=0));Q,R=np.linalg.qr(F);F=Q*np.sqrt(len(X));np.save(out/'source_vertices.npy',X);np.save(out/'basis.npy',F);(out/'definition.json').write_text(json.dumps(dict(source=str(Path(source).resolve()),seed=seed,eta=eta,formula='convex_hull(source_vertices + basis @ coefficient_matrix), uniform density1',features='quadratic and cubic monomials orthogonalized on literal source points'),indent=2));calls=0;best=np.inf;start=time.time();d=F.shape[1]*3
 def fun(t,gradient=False):
  nonlocal calls,best
  calls+=1;Y=X+F@t.reshape(-1,3);v,G,info=evaluate(Y,eta)
  if v<best:
   best=v;np.save(out/'best_coefficients.npy',t);np.save(out/'best.npy',Y);info.update(calls=calls,seconds=time.time()-start);(out/'best.json').write_text(json.dumps(info,indent=2))
  if max(info['Pmax'],info['Qmax'])<1e-11:
   np.save(out/f'potential_{calls}.npy',Y);print('POLYNOMIAL_POTENTIAL_REQUIRES_EXACT',info,flush=True)
  if calls%10000==0:print('POLYNOMIAL_SEARCH',calls,'best',best,'currentP',info['Pmax'],'currentQ',info['Qmax'],flush=True)
  return (v,(F.T@G).ravel()) if gradient else v
 rng=np.random.default_rng(seed);bounds=[(-.25,.25)]*d;pop=rng.normal(size=(144,d))*.015;pop[0]=0
 result=differential_evolution(fun,bounds,init=pop,seed=seed,maxiter=iterations,polish=False,tol=1e-8,mutation=(.4,1.),recombination=.6,updating='immediate');res=minimize(lambda t:fun(t,True),np.load(out/'best_coefficients.npy'),jac=True,method='L-BFGS-B',bounds=bounds,options=dict(maxiter=6000,maxls=50,ftol=1e-15,gtol=1e-10));(out/'termination.json').write_text(json.dumps(dict(global_message=result.message,local_message=res.message,calls=calls,seconds=time.time()-start),indent=2));print('POLYNOMIAL_DONE',out,json.loads((out/'best.json').read_text()),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--seed',type=int,default=72301);p.add_argument('--iterations',type=int,default=1600);p.add_argument('--eta',type=float,default=.05);a=p.parse_args();run(a.input,a.out,a.seed,a.iterations,a.eta)
