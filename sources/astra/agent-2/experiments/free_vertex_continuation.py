"""Literal free-vertex shape continuation with complete own-mass P/Q objectives.
Source analytic derivative is pinned from agent3, with a local directional check.
Only the convex hull is physical. All numerical results need a separate exact audit.
"""
import sys,json,hashlib,time,numpy as np
from pathlib import Path
from scipy.optimize import minimize
from scipy.spatial import ConvexHull
from gmpy2 import mpq
from geometry import angular_scores,mass
ROOT=Path(__file__).resolve().parents[1];sys.set_int_max_str_digits(0)
helper=ROOT/'sources/peer_agent3_persistence_birth.py';sys.path.insert(0,str(helper.parent));from peer_agent3_persistence_birth import evaluate

def run(src,out,seed,perturb,steps):
 if src.suffix=='.npy':
  X=np.load(src).copy();g=np.asarray(evaluate(X,.01)[2]['centroid'])
 else:
  r=json.loads(src.read_text());X=np.array([[float(mpq(v)) for v in row] for row in r['raw_vertices']]);g=np.array([float(mpq(v)) for v in r['raw_centroid']])
 X-=g;X/=np.linalg.norm(X,axis=1).max();assert len(X)<=84;out.mkdir(exist_ok=False,parents=True);rng=np.random.default_rng(seed)
 if perturb:
  x,y,z=X.T;F=np.column_stack([x*x,y*y,z*z,x*y,x*z,y*z,x**3,y**3,z**3,x*y*z]);F-=F.mean(0);Q,R=np.linalg.qr(F);X+=Q@rng.normal(size=(Q.shape[1],3))*perturb*np.sqrt(len(X)/Q.shape[1])
 # Check the exact symbolic differential away from coplanar seams on a private copy.
 T=X+rng.normal(size=X.shape)*1e-5;d=rng.normal(size=X.shape);d/=np.linalg.norm(d);v,G,inf=evaluate(T,.03);eps=1e-7;finite=(evaluate(T+eps*d,.03)[0]-evaluate(T-eps*d,.03)[0])/(2*eps);analytic=float((G*d).sum());rel=abs(finite-analytic)/max(1,abs(finite),abs(analytic));(out/'gradient_check.json').write_text(json.dumps(dict(analytic=analytic,finite=finite,relative_error=rel,epsilon=eps),indent=2)+'\n');assert rel<2e-4,'unverified derivative at selected test';print('GRADIENT_CHECK',out.name,rel,flush=True);np.save(out/'initial.npy',X);(out/'provenance.json').write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(src.read_bytes()).hexdigest(),seed=seed,perturb=perturb,helper=str(helper),helper_sha256=hashlib.sha256(helper.read_bytes()).hexdigest()),indent=2)+'\n');start=time.time();stages=[]
 for stage,eta in enumerate([1.,.3,.1,.03,.01,.003,.001,.0001,.00001]):
  dest=out/f'stage{stage}';dest.mkdir();calls=0;best=np.inf
  def fun(flat):
   nonlocal calls,best
   A=flat.reshape(X.shape);value,G,info=evaluate(A,eta);calls+=1
   if value<best:
    best=value;np.save(dest/'best.npy',A);info.update(calls=calls,seconds=time.time()-start);(dest/'best.json').write_text(json.dumps(info,indent=2)+'\n')
   if max(info['Pmax'],info['Qmax'])<1e-11:np.save(dest/f'NUMERICAL_NOMINATION_{calls}.npy',A)
   return value,G.ravel()
  opt=minimize(fun,X.ravel(),jac=True,method='L-BFGS-B',options=dict(maxiter=steps,maxfun=12*steps,maxls=60,maxcor=30,gtol=1e-11,ftol=1e-16));X=np.load(dest/'best.npy');info=evaluate(X,eta)[2];row=dict(stage=stage,eta=eta,Pmax=info['Pmax'],Qmax=info['Qmax'],Pcount=len(info['P']),Qcount=len(info['Q']),V=info['V'],nit=int(opt.nit),calls=calls,seconds=time.time()-start,message=str(opt.message));stages.append(row);(out/'stages.json').write_text(json.dumps(stages,indent=2)+'\n');print('FREE_VERTEX_STAGE',out.name,row,flush=True)
 np.save(out/'final.npy',X)
if __name__=='__main__':
 src=ROOT/sys.argv[1];out=ROOT/sys.argv[2];run(src,out,int(sys.argv[3]),float(sys.argv[4]),int(sys.argv[5]) if len(sys.argv)>5 else 1500)
