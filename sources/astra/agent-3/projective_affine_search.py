"""Physical projective/affine families: rebuild uniform mass AFTER mapping vertices.
No metric-only or transported-density claim. Input/output physical vertices are saved.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,time,argparse
from pathlib import Path
from scipy.optimize import differential_evolution,minimize
from persistence_birth import evaluate
from vertex_geometry import geometry

def transform(X,t,pscale):
 a,b,c,d,e=t[:5];p=t[5:]*pscale;A=np.array([[np.exp(a),c,d],[0,np.exp(b),e],[0,0,np.exp(-a-b)]]);den=1+X@p
 assert den.min()>0
 Y=X/den[:,None];Z=Y@A.T
 return Z,Y,A,den

def run(source,out,seed,iterations,span,power):
 out=Path(out);out.mkdir(exist_ok=False,parents=True);X=np.load(source);g=geometry(X,False)['g'];X=X-g;np.save(out/'input.npy',X);pscale=power/np.max(np.sum(np.abs(X),axis=1));(out/'parameters.json').write_text(json.dumps({'seed':seed,'maxiter':iterations,'affine_span':span,'projective_denominator_lower_bound':1-power,'pscale':pscale,'source':source},indent=2));calls=0;best=1e100;t0=time.time()
 def fun(t,jac=False):
  nonlocal calls,best
  calls+=1;Z,Y,A,den=transform(X,t,pscale);v,G,info=evaluate(Z,.01);GA=G.T@Y;Gy=G@A;grad=np.r_[GA[0,0]*A[0,0]-GA[2,2]*A[2,2],GA[1,1]*A[1,1]-GA[2,2]*A[2,2],GA[0,1],GA[0,2],GA[1,2],-pscale*np.sum((np.sum(Gy*X,axis=1)/den**2)[:,None]*X,axis=0)]
  if v<best:
   best=v;np.save(out/'best_params.npy',t);np.save(out/'best.npy',Z);(out/'best.json').write_text(json.dumps(dict(info,calls=calls,elapsed=time.time()-t0),indent=2))
  if max(info['Pmax'],info['Qmax'])<1e-11:
   np.save(out/'potential.npy',Z);(out/'potential.json').write_text(json.dumps(info,indent=2));print('POTENTIAL_PROJECTIVE_AFFINE110',out,info,flush=True)
  return (v,grad) if jac else v
 bounds=[(-span,span)]*5+[(-1,1)]*3;rng=np.random.default_rng(seed);initial=np.column_stack((rng.uniform(-span,span,(128,5)),rng.uniform(-1,1,(128,3))));initial[0]=0
 de=differential_evolution(fun,bounds,maxiter=iterations,init=initial,seed=seed,polish=False,tol=1e-9,atol=1e-10,updating='immediate');res=minimize(lambda t:fun(t,True),np.load(out/'best_params.npy'),jac=True,method='L-BFGS-B',bounds=bounds,options={'maxiter':4000,'maxls':50,'ftol':1e-16,'gtol':1e-12})
 print('PROJECTIVE_AFFINE_DONE',out,de.message,res.message,json.load(open(out/'best.json')),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('output');p.add_argument('--seed',type=int,default=37001);p.add_argument('--iterations',type=int,default=1000);p.add_argument('--span',type=float,default=1.);p.add_argument('--power',type=float,default=.8);a=p.parse_args();run(a.input,a.output,a.seed,a.iterations,a.span,a.power)
