"""Live-hull own-centroid search in a vertex budget, with analytic derivatives.
Floating search only: numerical roots and tolerances never certify a body.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from pathlib import Path
import json,sys,time,argparse
import numpy as np
from scipy.spatial import ConvexHull,QhullError
from scipy.optimize import minimize

def escapes(A,eps,weight=1.):
 n=len(A);e=A[None,:,:]-A[:,None,:];aa=np.sum(A*A,axis=1);ee=np.sum(e*e,axis=2)
 den=np.sqrt(np.maximum(aa[:,None]*ee,1e-60));phi=np.einsum('ic,ijc->ij',A,e)/den;np.fill_diagonal(phi,-np.inf)
 j=phi.argmax(axis=1);i=np.arange(n);val=phi[i,j];root=int(aa.argmax());res=np.maximum(eps-val,0);res[root]=0
 d=e[i,j];ds=ee[i,j];de=den[i,j];v=val
 # phi = a.(b-a)/(|a| |b-a|), differentiated in each endpoint.
 gi=(d-A)/de[:,None]-v[:,None]*(A/aa[:,None]-d/ds[:,None]);gj=A/de[:,None]-v[:,None]*d/ds[:,None]
 coef=-2*weight*res;grad=coef[:,None]*gi
 np.add.at(grad,j,coef[:,None]*gj)
 return weight*np.sum(res*res),grad,dict(root=root,roots=np.where(val<0)[0].tolist(),margin=float(np.min(np.delete(val,root))),resmax=float(res.max()),escape=val)

def evaluate(X,eps=1e-5,derivative=True):
 hull=ConvexHull(X);T=hull.simplices.copy();a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]]
 flip=np.einsum('ij,ij->i',np.cross(b-a,c-a),hull.equations[:,:3])<0
 T[flip]=T[flip][:,[0,2,1]]
 a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]]
 d=np.einsum('ij,ij->i',a,np.cross(b,c));D=d.sum();g=np.sum(d[:,None]*(a+b+c),axis=0)/(4*D);Z=X-g
 V=Z[hull.vertices];lv,gv,iv=escapes(V,eps);G=np.zeros_like(Z);G[hull.vertices]=gv
 # Generic triangular facets only: duplicate polar points are merged for an actual-hull root nomination.
 # Derivatives follow a representative triangle; any coplanar event is re-hulled at the next evaluation.
 H0=-hull.equations[:,:3]/(hull.equations[:,3]+hull.equations[:,:3]@g)[:,None]
 key=np.round(H0,10);_,keep=np.unique(key,axis=0,return_index=True);keep=np.sort(keep);TT=T[keep]
 H=H0[keep];lh,gh,ih=escapes(H,eps)
 if derivative:
  w=np.linalg.solve(np.swapaxes(Z[TT],1,2),gh[...,None])[...,0]
  dZT=-w[:,:,None]*H[:,None,:]
  np.add.at(G,TT.reshape(-1),dZT.reshape(-1,3))
  t=-G.sum(axis=0);s=(a+b+c-4*g)@t
  for k,cr in [(0,np.cross(b,c)),(1,np.cross(c,a)),(2,np.cross(a,b))]:
   add=(d[:,None]*t+s[:,None]*cr)/(4*D);np.add.at(G,T[:,k],add)
 info=dict(S=len(ih['roots']),U=len(iv['roots']),V=len(hull.vertices),F=len(H),E=len(hull.vertices)+len(H)-2,volume=float(D/6),marginV=iv['margin'],marginF=ih['margin'],loss=float(lv+lh),stable_roots=ih['roots'],unstable_roots=np.array(hull.vertices)[iv['roots']].tolist(),centroid=g.tolist())
 return lv+lh,G,info

def trial(seed,n,steps,epsilon,folder,source='primal'):
 rng=np.random.default_rng(seed);seedbody=np.load('artifacts/c622/seed.npz');Y=seedbody['X' if source=='primal' else 'Q'].copy()
 # Farthest-point coverage retains both extremes of the inherited equilibrium landscape.
 first=int(np.argmax(np.sum(Y*Y,axis=1)));ids=[first];dist=np.linalg.norm(Y-Y[first],axis=1)
 while len(ids)<n:
  weights=dist*(.85+.3*rng.random(len(Y)));k=int(np.argmax(weights));ids.append(k);dist=np.minimum(dist,np.linalg.norm(Y-Y[k],axis=1))
 X=Y[ids];X+=rng.normal(size=X.shape)*1e-5
 # Dual route: these are physical vertices too; polar conversion is explicitly separate below.
 X-=X.mean(axis=0);X/=np.sqrt(np.mean(np.sum(X*X,axis=1)))
 counter=0;best=(float('inf'),None);start=time.time();history=[]
 def fun(z):
  nonlocal counter,best
  counter+=1;x=z.reshape(-1,3)
  loss,grad,info=evaluate(x,epsilon)
  if loss<best[0]:
   best=(loss,x.copy());np.save(folder/'best.npy',x)
   (folder/'best.json').write_text(json.dumps(dict(info,calls=counter,seed=seed,n=n,source=source,elapsed=time.time()-start),indent=2)+'\n')
  if counter%100==0:
   history.append(dict(info,calls=counter,elapsed=time.time()-start));print(seed,n,counter,info,flush=True)
   (folder/'history.json').write_text(json.dumps(history,indent=2)+'\n')
  if info['S']==info['U']==1 and info['marginV']>1e-7 and info['marginF']>1e-7:
   np.save(folder/'potential.npy',x);(folder/'potential.json').write_text(json.dumps(info,indent=2));print('POTENTIAL_OWN110_PRESERVED',folder,info,flush=True)
  return loss,grad.ravel()
 result=minimize(fun,X.ravel(),method='L-BFGS-B',jac=True,options={'maxiter':steps,'maxfun':steps*4,'maxls':40,'ftol':1e-16,'gtol':1e-10,'maxcor':25})
 loss,grad,info=evaluate(best[1],epsilon)
 (folder/'result.json').write_text(json.dumps(dict(info,success=bool(result.success),message=str(result.message),calls=counter,iterations=int(result.nit),seed=seed,n=n,epsilon=epsilon),indent=2)+'\n')
 print('TRIAL_DONE',seed,n,source,info,result.message,flush=True)
 return info

def gradient_check():
 r=np.random.default_rng(431);X=r.normal(size=(16,3));v,G,i=evaluate(X,1e-3);d=r.normal(size=X.shape);d/=np.linalg.norm(d)
 for h in [1e-4,1e-5,1e-6,1e-7]:
  f1=evaluate(X+h*d,1e-3,False)[0];f0=evaluate(X-h*d,1e-3,False)[0];print('GRADIENT',h,(f1-f0)/(2*h),np.sum(G*d),abs((f1-f0)/(2*h)-np.sum(G*d)))
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--seed',type=int,default=30928);ap.add_argument('--n',type=int,default=80);ap.add_argument('--steps',type=int,default=1500);ap.add_argument('--trials',type=int,default=1);ap.add_argument('--source',default='primal');ap.add_argument('--epsilon',type=float,default=1e-5);ap.add_argument('--check',action='store_true');a=ap.parse_args()
 if a.check:gradient_check();sys.exit()
 for s in range(a.seed,a.seed+a.trials):
  folder=Path(f'artifacts/vertex_search/{a.source}_{a.n}_{s}');folder.mkdir(exist_ok=False,parents=True)
  trial(s,a.n,a.steps,a.epsilon,folder,a.source)
