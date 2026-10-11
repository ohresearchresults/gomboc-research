"""Centroid-aware physical search with a continuous surface-weighted route objective.
All input points are retained in the primal graph, including nonextreme points.
Polar route costs are weighted by actual triangular facet area; splitting/merging
coplanar facets preserves their total weight. No facet rounding enters the loss.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from pathlib import Path
import json,time,argparse,numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import minimize
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

def routes(A,eps,weights,root=None):
 aa=np.sum(A*A,axis=1);q=A@A.T/aa[:,None]-1;np.fill_diagonal(q,-1e10);root=int(aa.argmax()) if root is None else int(root);res=np.maximum(eps-q,0);cost=res*res+1e-20;np.fill_diagonal(cost,0)
 dist,j=dijkstra(csr_matrix(cost.T),indices=root,return_predecessors=True);j[root]=(root+1)%len(A)
 mult=weights.copy();mult[root]=0
 children=np.bincount(j[np.arange(len(A))!=root],minlength=len(A));queue=[int(i) for i in np.flatnonzero(children==0) if i!=root];processed=0
 while queue:
  i=queue.pop();parent=int(j[i]);mult[parent]+=mult[i];children[parent]-=1;processed+=1
  if children[parent]==0 and parent!=root:queue.append(parent)
 assert processed==len(A)-1,'cyclic Dijkstra predecessor graph'
 mult[root]=0;i=np.arange(len(A));val=q[i,j];rr=np.maximum(eps-val,0)
 gi=(A[j]-2*A)/aa[:,None]-2*val[:,None]*A/aa[:,None];gj=A/aa[:,None]
 coef=-2*mult*rr;G=coef[:,None]*gi;np.add.at(G,j,coef[:,None]*gj)
 return float(weights@dist),G,dist,q.max(axis=1)

def evaluate(X,eps=1e-6,derivative=True):
 hull=ConvexHull(X);T=hull.simplices.copy();a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]]
 flip=np.einsum('ij,ij->i',np.cross(b-a,c-a),hull.equations[:,:3])<0;T[flip]=T[flip][:,[0,2,1]]
 a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];d=np.einsum('ij,ij->i',a,np.cross(b,c));D=d.sum();g=np.sum(d[:,None]*(a+b+c),axis=0)/(4*D);Z=X-g
 N=np.cross(b-a,c-a);twicearea=np.linalg.norm(N,axis=1);area=twicearea*.5;atotal=area.sum()
 H=-hull.equations[:,:3]/(hull.equations[:,3]+hull.equations[:,:3]@g)[:,None]
 lv,G,dv,vp=routes(Z,eps,np.full(len(Z),1/len(Z)));lh,GH,dh,vh=routes(H,eps,area/atotal)
 if derivative:
  w=np.linalg.solve(np.swapaxes(Z[T],1,2),GH[...,None])[...,0];dZT=-w[:,:,None]*H[:,None,:];np.add.at(G,T.reshape(-1),dZT.reshape(-1,3))
  unit=N/twicearea[:,None];gb=.5*np.cross(c-a,unit);gc=.5*np.cross(unit,b-a);coeff=(dh-lh)/atotal
  for k,gg in [(0,-gb-gc),(1,gb),(2,gc)]:np.add.at(G,T[:,k],coeff[:,None]*gg)
  t=-G.sum(axis=0);s=(a+b+c-4*g)@t
  for k,cr in [(0,np.cross(b,c)),(1,np.cross(c,a)),(2,np.cross(a,b))]:np.add.at(G,T[:,k],(d[:,None]*t+s[:,None]*cr)/(4*D))
 # Counts are numerical diagnostics only. Coplanar maximal-face grouping is not used by loss.
 _,inds=np.unique(np.round(H,10),axis=0,return_index=True);Hs=H[inds];hsq=np.sum(Hs*Hs,axis=1);eq=Hs@Hs.T/hsq[:,None]-1;np.fill_diagonal(eq,-np.inf);hq=eq.max(axis=1)
 u=int(np.argmax(np.sum(Z*Z,axis=1)));s=int(hsq.argmax());nf=len(inds);nv=len(hull.vertices)
 info=dict(S=int(np.sum(hq<0)),U=int(np.sum(vp<0)),V=nv,F=nf,E=nv+nf-2,loss=float(lv+lh),p_loss=lv,q_loss=lh,minV=float(np.min(np.delete(vp,u))),minF=float(np.min(np.delete(hq,s))),volume=float(D/6),centroid=g.tolist())
 return lv+lh,G,info

def run(X,out,steps,eps):
 out=Path(out);out.mkdir(exist_ok=False,parents=True);np.save(out/'initial.npy',X);best=1e100;calls=0;start=time.time()
 def fun(z):
  nonlocal best,calls
  calls+=1;x=z.reshape(-1,3);v,G,info=evaluate(x,eps)
  if v<best:
   best=v;np.save(out/'best.npy',x);(out/'best.json').write_text(json.dumps(dict(info,calls=calls,elapsed=time.time()-start),indent=2)+'\n')
  if calls%500==0:print('SURFACE',calls,info,flush=True)
  if info['S']==info['U']==1 and min(info['minV'],info['minF'])>1e-10:
   np.save(out/'potential.npy',x);(out/'potential.json').write_text(json.dumps(info,indent=2));print('POTENTIAL_SURFACE110',out,info,flush=True)
  return v,G.ravel()
 r=minimize(fun,X.ravel(),jac=True,method='L-BFGS-B',options={'maxiter':steps,'maxfun':steps*6,'maxls':50,'maxcor':30,'ftol':1e-16,'gtol':1e-12})
 print('DONE_SURFACE',out,str(r.message),json.load(open(out/'best.json')),flush=True)
 (out/'termination.json').write_text(json.dumps({'message':str(r.message),'nit':int(r.nit),'calls':calls},indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('output');p.add_argument('--steps',type=int,default=10000);p.add_argument('--epsilon',type=float,default=1e-6);p.add_argument('--check',action='store_true');a=p.parse_args()
 if a.check:
  rng=np.random.default_rng(625);X=rng.normal(size=(18,3));d=rng.normal(size=X.shape);d/=np.linalg.norm(d);v,G,i=evaluate(X)
  for eps in [1e-4,1e-5,1e-6,1e-7]:print('GRAD',eps,(evaluate(X+eps*d,derivative=False)[0]-evaluate(X-eps*d,derivative=False)[0])/(2*eps),np.sum(G*d))
 else:run(np.load(a.input),a.output,a.steps,a.epsilon)
