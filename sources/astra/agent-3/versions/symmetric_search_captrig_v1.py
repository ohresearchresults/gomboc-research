"""Half-turn symmetric physical hull with a guaranteed stable cap and unstable apex.
Density is uniformly one; symmetry forces centroid y=z=0. All counts audited at its
computed centroid. Only rationalization/exact audit could promote a candidate.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,time,argparse
from pathlib import Path
from scipy.optimize import minimize
from scipy.spatial import ConvexHull
from search_surface import routes

def shape(params,K,m,a):
 P=params[:-1].reshape(K,3);r=params[-1];ph=2*np.pi*np.arange(m)/m;U=np.column_stack((np.cos(ph),np.sin(ph)))
 X=np.concatenate([[[1.,0,0]],P,P*[1,-1,-1],np.column_stack((np.full(m,-a),r*U))])
 return X,U

def evaluate(X,eps):
 hull=ConvexHull(X);T=hull.simplices.copy();a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];flip=np.einsum('ij,ij->i',np.cross(b-a,c-a),hull.equations[:,:3])<0;T[flip]=T[flip][:,[0,2,1]]
 a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];d=np.einsum('ij,ij->i',a,np.cross(b,c));D=d.sum();g=np.sum(d[:,None]*(a+b+c),axis=0)/(4*D);Z=X-g
 assert max(abs(g[1:]))<1e-10
 N=np.cross(b-a,c-a);A=np.linalg.norm(N,axis=1)*.5;AT=A.sum();H=-hull.equations[:,:3]/(hull.equations[:,3]+hull.equations[:,:3]@g)[:,None]
 roots=np.where(hull.equations[:,0]<-1+1e-12)[0];assert len(roots)>0;s=int(roots[0]);lv,G,dv,pv=routes(Z,eps,np.ones(len(Z))/len(Z),root=0);lh,GH,dh,qv=routes(H,eps,A/AT,root=s)
 w=np.linalg.solve(np.swapaxes(Z[T],1,2),GH[...,None])[...,0];dZT=-w[:,:,None]*H[:,None,:];np.add.at(G,T.reshape(-1),dZT.reshape(-1,3))
 unit=N/(2*A)[:,None];gb=.5*np.cross(c-a,unit);gc=.5*np.cross(unit,b-a);coef=(dh-lh)/AT
 for k,gg in [(0,-gb-gc),(1,gb),(2,gc)]:np.add.at(G,T[:,k],coef[:,None]*gg)
 t=-G.sum(axis=0);ss=(a+b+c-4*g)@t
 for k,cr in [(0,np.cross(b,c)),(1,np.cross(c,a)),(2,np.cross(a,b))]:np.add.at(G,T[:,k],(d[:,None]*t+ss[:,None]*cr)/(4*D))
 _,inds=np.unique(np.round(H,10),axis=0,return_index=True);Hs=H[inds];aa=np.sum(Hs*Hs,axis=1);q=Hs@Hs.T/aa[:,None]-1;np.fill_diagonal(q,-np.inf);qmax=q.max(axis=1);s0=int(np.argmin(Hs[:,0]));nv=len(hull.vertices);nf=len(Hs)
 info=dict(S=int(np.sum(qmax<0)),U=int(np.sum(pv<0)),V=nv,F=nf,E=nv+nf-2,loss=lv+lh,p_loss=lv,q_loss=lh,minV=float(np.min(pv[1:])),minF=float(np.min(np.delete(qmax,s0))),centroid=g.tolist(),volume=float(D/6))
 return lv+lh,G,info

def run(seed,K,m,a,steps,source):
 rng=np.random.default_rng(seed);out=Path(f'artifacts/symmetric/{source}_k{K}_m{m}_a{a:g}_s{seed}');out.mkdir(parents=True,exist_ok=False)
 if source=='c622':
  Y=np.load('artifacts/c622/seed.npz')['X'];u=Y[np.argmax(np.sum(Y*Y,axis=1))];u/=np.linalg.norm(u);v=np.cross(u,[1,0,0]);v/=np.linalg.norm(v);w=np.cross(u,v);Y=Y@np.array([u,v,w]).T;Y/=Y[:,0].max();Y=Y[Y[:,0]<.99];Y[:,0]=np.clip(Y[:,0],-a+.02,.98)
  ids=[int(rng.integers(len(Y)))];dist=np.linalg.norm(Y-Y[ids[0]],axis=1)
  while len(ids)<K:
   k=int(np.argmax(dist*(.8+.4*rng.random(len(Y)))));ids.append(k);dist=np.minimum(dist,np.linalg.norm(Y-Y[k],axis=1))
  P=Y[ids].copy();P+=rng.normal(size=P.shape)*.001;P[:,0]=np.clip(P[:,0],-a+.01,.98);r=.35
 else:
  z=rng.uniform(-.96,.96,K);phi=rng.uniform(0,2*np.pi,K);beta=.12;phase=1.5*np.pi*(z-z**3/3);rr=np.sqrt(1-z*z);P=np.column_stack((beta*np.cos(phase)+rr*np.cos(phi),beta*np.sin(phase)+rr*np.sin(phi),z))/(1+beta);P[:,0]=np.clip(P[:,0],-a+.01,.99);r=.4
 p=np.r_[P.ravel(),r];np.save(out/'initial_params.npy',p);(out/'input.json').write_text(json.dumps({'K':K,'m':m,'a':a,'seed':seed,'source':source},indent=2));calls=0;best=1e100;t0=time.time()
 def fun(x):
  nonlocal calls,best
  calls+=1;X,U=shape(x,K,m,a);val,G,ci=evaluate(X,1e-7);GP=G[1:1+K]+G[1+K:1+2*K]*[1,-1,-1];gr=np.sum(G[-m:,1:]*U);grad=np.r_[GP.ravel(),gr]
  if val<best:
   best=val;np.save(out/'best_params.npy',x);np.save(out/'best.npy',X);(out/'best.json').write_text(json.dumps(dict(ci,calls=calls,elapsed=time.time()-t0),indent=2))
  if calls%1000==0:print('SYM',out,calls,ci,flush=True)
  if ci['S']==ci['U']==1 and min(ci['minV'],ci['minF'])>1e-10:
   np.save(out/'potential_params.npy',x);np.save(out/'potential.npy',X);(out/'potential.json').write_text(json.dumps(ci,indent=2));print('POTENTIAL_SYMMETRIC110',out,ci,flush=True)
  return val,grad
 bounds=[b for _ in range(K) for b in [(-a+1e-5,.99999),(-2,2),(-2,2)]]+[(.02,2)]
 res=minimize(fun,p,jac=True,method='L-BFGS-B',bounds=bounds,options={'maxiter':steps,'maxfun':steps*5,'maxls':50,'maxcor':30,'ftol':1e-16,'gtol':1e-11})
 (out/'termination.json').write_text(json.dumps({'message':str(res.message),'nit':int(res.nit),'calls':calls},indent=2));print('DONE_SYM',out,res.message,json.load(open(out/'best.json')),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--steps',type=int,default=10000);p.add_argument('--seed',type=int,default=33928);p.add_argument('--trials',type=int,default=2);a=p.parse_args()
 for source in ['c622','sloan']:
  for cap in [.4,.7]:
   for seed in range(a.seed,a.seed+a.trials):run(seed,38,8,cap,a.steps,source)
