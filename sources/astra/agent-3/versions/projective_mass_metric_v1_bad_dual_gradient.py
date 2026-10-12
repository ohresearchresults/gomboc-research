"""Projectively normalize actual homogeneous mass, then search physical metrics.
Starting origin is a literal reference110 point. For y=x/(1+p.x), the
Jacobian is(1+p.x)^-4 and centroid zero minimizes transformed volume in p.
The numerical Newton solve integrates the actual transformed polyhedron.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import differential_evolution,minimize
from gmpy2 import mpq
from polar_centroid_orbits import mesh,base,mass,D
from persistence_birth import bars_loss
from support_geometry import escape

def normalize(X,T):
 p=np.zeros(3);hist=[]
 for it in range(60):
  den=1+X@p;assert min(den)>0;Y=X/den[:,None];DY=-Y[:,:,None]*Y[:,None,:];a,b,c=Y[T[:,0]],Y[T[:,1]],Y[T[:,2]];da,db,dc=DY[T[:,0]],DY[T[:,1]],DY[T[:,2]];v6=np.einsum('ic,ic->i',a,np.cross(b,c));V=v6.sum()/6;g=np.sum(v6[:,None]*(a+b+c),axis=0)/(4*v6.sum());dv=np.einsum('ic,icp->ip',np.cross(b,c),da)+np.einsum('ic,icp->ip',np.cross(c,a),db)+np.einsum('ic,icp->ip',np.cross(a,b),dc);dg=(np.einsum('ip,ic->cp',dv,a+b+c-4*g)+np.einsum('i,icp->cp',v6,da+db+dc))/(4*v6.sum());row=dict(it=it,norm=float(np.linalg.norm(g)),volume=float(V),min_denominator=float(min(den)),p=p.tolist());hist.append(row)
  if np.linalg.norm(g)<1e-13:return Y,p,hist
  dp=-np.linalg.solve(dg,g);ok=False
  for k in range(20):
   pp=p+2.**-k*dp;dd=1+X@pp
   if min(dd)<=0:continue
   yy=X/dd[:,None];gg,vv=mass(yy,T)
   if np.linalg.norm(gg)<np.linalg.norm(g)*(1-1e-5):p=pp;ok=True;break
  if not ok:raise ValueError('projective uniform-centroid normalization failed')
 raise ValueError('projective centroid normalization exceeded60steps')

def run(audit,reference,out,iterations,seed):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);src=Path(audit);a=json.loads(src.read_text());r=json.loads(Path(reference).read_text());c=np.array([float(mpq(v)) for v in r['reference_center']]);X=np.array([[float(mpq(v)) for v in row] for row in a['raw_vertices']])-c;B=mesh(X,a['faces']);Y,p,hist=normalize(X,B['T']);(out/'normalization.json').write_text(json.dumps(hist,indent=2));np.save(out/'normalized_vertices.npy',Y);P=np.eye(4);P[3,:3]=p;T=np.eye(4);T[:3,3]=-c;P=P@T
 bases=base(audit);opposite=bases[1];Qh=np.column_stack((opposite['points'],np.ones(len(opposite['points']))))@(D@np.linalg.inv(P).T@D).T;Q=Qh[:,:3]/Qh[:,-1,None];calls=0;best=np.inf;start=time.time();bounds=[(-3.,3.),(-3.,3.),(-5.,5.),(-5.,5.),(-5.,5.)]
 def fun(t,jac=False):
  nonlocal calls,best
  calls+=1;aa,bb,cx,dx,ex=t;A=np.array([[np.exp(aa),cx,dx],[0.,np.exp(bb),ex],[0.,0.,np.exp(-aa-bb)]]);Z=Y@A.T;H=Q@np.linalg.inv(A);pv,GP,ps=bars_loss(Z,B['edges'],.01);qv,GQ,qs=bars_loss(H,opposite['edges'],.01);loss=pv+qv;info=dict(S=int(np.sum(escape(H)[0]<0)),U=int(np.sum(escape(Z)[0]<0)),Pmax=max(ps,default=0.),Qmax=max(qs,default=0.),loss=loss,calls=calls,seconds=time.time()-start)
  if loss<best:
   best=loss;AP=np.eye(4);AP[:3,:3]=A;np.savez(out/'best_embedding.npz',P=AP@P,dual=0);np.save(out/'best_params.npy',t);np.save(out/'best_vertices.npy',Z);(out/'best.json').write_text(json.dumps(info,indent=2))
  if info['S']==info['U']==1:
   dest=out/f'potential{calls}';dest.mkdir();AP=np.eye(4);AP[:3,:3]=A;np.savez(dest/'embedding.npz',P=AP@P,dual=0);(dest/'source.json').write_text((out/'source.json').read_text());(dest/'nomination.json').write_text(json.dumps(info,indent=2));print('METRIC_POTENTIAL_PHYSICAL_REQUIRES_EXACT',dest,info,flush=True)
  if not jac:return loss
  I=np.linalg.inv(A);GA=GP.T@Y-I.T@H.T@GQ@I.T;grad=np.array([GA[0,0]*A[0,0]-GA[2,2]*A[2,2],GA[1,1]*A[1,1]-GA[2,2]*A[2,2],GA[0,1],GA[0,2],GA[1,2]]);return loss,grad
 import hashlib
 (out/'source.json').write_text(json.dumps(dict(audit_path=str(src.resolve()),audit_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),reference_source=str(Path(reference).resolve())),indent=2));rng=np.random.default_rng(seed);pop=np.column_stack((rng.uniform(-1,1,(96,2)),rng.uniform(-1,1,(96,3))));pop[0]=0;r=differential_evolution(fun,bounds,maxiter=iterations,seed=seed,init=pop,polish=False,tol=1e-10);r2=minimize(lambda t:fun(t,True),np.load(out/'best_params.npy'),jac=True,method='L-BFGS-B',bounds=bounds,options=dict(maxiter=4000,maxls=50,ftol=1e-15,gtol=1e-10));(out/'termination.json').write_text(json.dumps(dict(global_message=r.message,local_message=r2.message),indent=2));print('MASS_METRIC_DONE',out,json.loads((out/'best.json').read_text()),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('audit');p.add_argument('reference');p.add_argument('out');p.add_argument('--iterations',type=int,default=1400);p.add_argument('--seed',type=int,default=82301);a=p.parse_args();run(a.audit,a.reference,a.out,a.iterations,a.seed)
