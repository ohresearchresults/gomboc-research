"""Convex variable-aspect rectangle sections with four independent curvatures.
Each signed horizontal bound is a positive Green sum plus endpoint tilt.
This is a larger family than homothetic polygon sections: the two widths vary
independently with height. Quads remain planar. L30 gives trueC488,V122.
"""
import argparse,json
from pathlib import Path
import numpy as np
from scipy.special import softmax
from scipy.optimize import minimize
from triangular_sections import Family,Search

def topology(m,L):
 n=m*L+2;faces=[]
 for j in range(m):faces.append([0,1+(j+1)%m,1+j])
 for i in range(L-1):
  for j in range(m):faces.append([1+m*i+j,1+m*i+(j+1)%m,1+m*(i+1)+(j+1)%m,1+m*(i+1)+j])
 for j in range(m):faces.append([1+m*(L-1)+j,1+m*(L-1)+(j+1)%m,n-1])
 tris=np.array([(f[0],f[i],f[i+1]) for f in faces for i in range(1,len(f)-1)]);ft=np.array([f[:3] for f in faces]);owners={}
 for i,f in enumerate(faces):
  for j,k in zip(f,f[1:]+f[:1]):owners.setdefault(tuple(sorted((j,k))),[]).append(i)
 return faces,tris,ft,np.array(list(owners)),np.array(list(owners.values()))

class RectFamily(Family):
 def __init__(self,L):
  self.L=L;self.d=5*L+4;self.n=4*L+2;self.faces,self.tris,self.ft,self.pe,self.qe=topology(4,L)
 def initial(self,beta,seed):
  L=self.L;z=np.linspace(-1,1,L+2);r=np.sqrt(1-z*z);phase=1.5*np.pi*(z-z**3/3);mu=beta*np.column_stack((np.cos(phase)+1,np.sin(phase)));k=-np.diff(np.diff(r)/np.diff(z));a=np.diff(np.diff(mu,axis=0)/np.diff(z)[:,None],axis=0)/k[:,None];normals=np.array([[1.,0.],[0.,1.],[-1.,0.],[0.,-1.]]);W=k[:,None]*(1-a@normals.T);assert (W>0).all();q=np.r_[np.zeros(L),np.log(W).ravel(),np.zeros(4)];rng=np.random.default_rng(seed)
  if seed:q[L:5*L]+=rng.normal(size=4*L)*.15
  return q
 def coordinates(self,q):
  L=self.L;d=self.d;w=softmax(np.r_[q[:L],0.]);Dw=(np.diag(w)-np.outer(w,w))[:,:L];z=-1+2*np.cumsum(w)[:-1];Dz=np.zeros((L,d));Dz[:,:L]=2*np.cumsum(Dw,axis=0)[:-1];W=np.exp(q[L:5*L]).reshape(L,4);DW=np.zeros((L,4,d));DW[:,:,L:5*L]=np.diag(W.ravel()).reshape(L,4,4*L)
  ii,jj=np.indices((L,L));mi=np.minimum(ii,jj);ma=np.maximum(ii,jj);G=(z[mi]+1)*(1-z[ma])/2;DG=((1-z[ma])[...,None]*Dz[mi]-(z[mi]+1)[...,None]*Dz[ma])/2;values=G@W;Dval=np.einsum('ijp,jc->icp',DG,W)+np.einsum('ij,jcp->icp',G,DW);v=q[-4:-2];Dv=np.zeros((2,d));Dv[:,-4:-2]=np.eye(2);mu=(z[:,None]+1)/2*v;Dmu=np.einsum('ip,c->icp',Dz/2,v)+(z[:,None,None]+1)/2*Dv
  X=np.zeros((self.n,3));DX=np.zeros((self.n,3,d));X[0,2]=-1;X[-1]=np.r_[v,1.];DX[-1,:2]=Dv
  for j,(ix,iy,sx,sy) in enumerate([(0,3,1,-1),(0,1,1,1),(2,1,-1,1),(2,3,-1,-1)]):
   ids=1+4*np.arange(L)+j;X[ids,0]=sx*values[:,ix]+mu[:,0];X[ids,1]=sy*values[:,iy]+mu[:,1];X[ids,2]=z;DX[ids,0]=sx*Dval[:,ix]+Dmu[:,0];DX[ids,1]=sy*Dval[:,iy]+Dmu[:,1];DX[ids,2]=Dz
  A=np.array([[np.exp(q[-2]),q[-1]],[0.,np.exp(-q[-2])]]);xy=X[:,:2].copy();DX[:,:2]=np.einsum('ab,nbp->nap',A,DX[:,:2]);DX[:,0,-2]+=A[0,0]*xy[:,0];DX[:,1,-2]-=A[1,1]*xy[:,1];DX[:,0,-1]+=xy[:,1];X[:,:2]=xy@A.T
  return X,DX,dict(kind=np.array('independent_rectangle_curvatures'),z=z,W=W,tilt=v,A=A,side_supports=values)

class RectSearch(Search):
 def run(self,q,iters):
  L=self.f.L;bounds=[(-4.,4.)]*L+[(-14.,6.)]*(4*L)+[(-3.,3.)]*2+[(-1.5,1.5),(-2.,2.)];r=minimize(self.evaluate,q,jac=True,method='L-BFGS-B',bounds=bounds,options=dict(maxiter=iters,maxls=45,maxcor=25,ftol=1e-14,gtol=1e-10));(self.out/'termination.json').write_text(json.dumps(dict(message=r.message,nit=r.nit,success=bool(r.success)),indent=2));print('RECT_SECTION_DONE',self.out,r.message,flush=True);return np.load(self.out/'best_params.npy')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('out');p.add_argument('--layers',type=int,default=30);p.add_argument('--seed',type=int,default=1);p.add_argument('--beta',type=float,default=.035);p.add_argument('--iterations',type=int,default=3500);p.add_argument('--check',action='store_true');a=p.parse_args();f=RectFamily(a.layers);q=f.initial(a.beta,a.seed);out=Path(a.out);out.mkdir(parents=True,exist_ok=False);np.save(out/'initial_params.npy',q);(out/'input.json').write_text(json.dumps(dict(layers=a.layers,seed=a.seed,beta=a.beta,C=16*a.layers+8,method='independent positive curvature for four rectangle supports')))
 if a.check:
  rng=np.random.default_rng(953);d=rng.normal(size=q.shape);d/=np.linalg.norm(d);v,J,info,g=f.evaluate(q,.01);print('INITIAL',{k:info[k] for k in ['S','U','C','Pmax','Qmax']})
  for h in [1e-4,1e-5,1e-6,1e-7]:print('GRAD',h,(f.evaluate(q+h*d,.01)[0]-f.evaluate(q-h*d,.01)[0])/(2*h),J@d)
  from vertex_geometry import geometry
  gg=geometry(g['X'],False);print('REHULL_MASS_ERROR',np.max(abs(gg['g']-g['g'])),abs(gg['V']-g['V']));print('MAX_SUPPORT_SLACK',np.max(g['H']@g['Z'].T-1));np.savez(out/'initial_construction.npz',**g['construction'])
 else:
  for i,eta in enumerate([.1,.02,.002]):q=RectSearch(f,out/f'stage{i}',eta).run(q,a.iterations)
