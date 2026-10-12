"""Independent positive concavity for all three triangular side supports.
Equivalent geometric class to translated homothetic triangles; avoids the
coupled total-curvature/softmax coordinates. Every physical side stays convex.
"""
import argparse,json
from pathlib import Path
import numpy as np
from scipy.special import softmax
from scipy.optimize import minimize
from triangular_sections import Family,Search,B

class SideFamily(Family):
 def __init__(self,L):
  super().__init__(L);e=np.roll(B,-1,axis=0)-B;self.normals=np.column_stack((e[:,1],-e[:,0]));self.h=np.sum(self.normals*B,axis=1);self.M=np.column_stack((self.h,self.normals));self.I=np.linalg.inv(self.M)
 def initial(self,beta,seed):
  old=Family(self.L);q=old.initial(beta,seed);g=old.coordinates(q)[2];W=g['k'][:,None]*(self.h-g['a']@self.normals.T);assert (W>0).all();return np.r_[q[:self.L],np.log(W).ravel(),q[-4:]]
 def coordinates(self,q):
  L=self.L;d=self.d;w=softmax(np.r_[q[:L],0.]);Dw=(np.diag(w)-np.outer(w,w))[:,:L];z=-1+2*np.cumsum(w)[:-1];Dz=np.zeros((L,d));Dz[:,:L]=2*np.cumsum(Dw,axis=0)[:-1];W=np.exp(q[L:4*L]).reshape(L,3);DW=np.zeros((L,3,d));DW[:,:,L:4*L]=np.diag(W.ravel()).reshape(L,3,3*L)
  ii,jj=np.indices((L,L));mi=np.minimum(ii,jj);ma=np.maximum(ii,jj);G=(z[mi]+1)*(1-z[ma])/2;DG=((1-z[ma])[...,None]*Dz[mi]-(z[mi]+1)[...,None]*Dz[ma])/2
  values=G@W;Dval=np.einsum('ijp,jc->icp',DG,W)+np.einsum('ij,jcp->icp',G,DW);sec=values@self.I.T;Dsec=np.einsum('ac,icp->iap',self.I,Dval);r=sec[:,0];Dr=Dsec[:,0];v=q[-4:-2];Dv=np.zeros((2,d));Dv[:,-4:-2]=np.eye(2);mu=sec[:,1:]+(z[:,None]+1)/2*v;Dmu=Dsec[:,1:]+np.einsum('ip,c->icp',Dz/2,v)+(z[:,None,None]+1)/2*Dv
  X=np.zeros((self.n,3));DX=np.zeros((self.n,3,d));X[0,2]=-1;X[-1]=np.r_[v,1.];DX[-1,:2]=Dv;X[1:-1,:2]=(mu[:,None,:]+r[:,None,None]*B).reshape(-1,2);X[1:-1,2]=np.repeat(z,3);DX[1:-1,:2]=(Dmu[:,None,:,:]+Dr[:,None,None,:]*B[None,:,:,None]).reshape(-1,2,d);DX[1:-1,2]=np.repeat(Dz,3,axis=0)
  A=np.array([[np.exp(q[-2]),q[-1]],[0.,np.exp(-q[-2])]]);xy=X[:,:2].copy();DX[:,:2]=np.einsum('ab,nbp->nap',A,DX[:,:2]);DX[:,0,-2]+=A[0,0]*xy[:,0];DX[:,1,-2]-=A[1,1]*xy[:,1];DX[:,0,-1]+=xy[:,1];X[:,:2]=xy@A.T
  return X,DX,dict(z=z,W=W,side_normals=self.normals,side_offsets=self.h,section_matrix=self.M,r=r,mu=mu,tilt=v,A=A,base=B)

class SideSearch(Search):
 def run(self,q,iters):
  L=self.f.L;bounds=[(-4.,4.)]*L+[(-14.,6.)]*(3*L)+[(-3.,3.)]*2+[(-1.5,1.5),(-2.,2.)];r=minimize(self.evaluate,q,jac=True,method='L-BFGS-B',bounds=bounds,options=dict(maxiter=iters,maxls=45,maxcor=25,ftol=1e-14,gtol=1e-10));(self.out/'termination.json').write_text(json.dumps(dict(message=r.message,nit=r.nit,success=bool(r.success)),indent=2));print('SIDE_SECTION_DONE',self.out,r.message,flush=True);return np.load(self.out/'best_params.npy')

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('out');p.add_argument('--layers',type=int,default=40);p.add_argument('--seed',type=int,default=2);p.add_argument('--beta',type=float,default=.015);p.add_argument('--iterations',type=int,default=3000);p.add_argument('--check',action='store_true');a=p.parse_args();f=SideFamily(a.layers);q=f.initial(a.beta,a.seed);out=Path(a.out);out.mkdir(parents=True,exist_ok=False);np.save(out/'initial_params.npy',q);(out/'input.json').write_text(json.dumps(dict(layers=a.layers,seed=a.seed,beta=a.beta,C=12*a.layers+6,method='independent positive side curvature')))
 if a.check:
  rng=np.random.default_rng(812);d=rng.normal(size=q.shape);d/=np.linalg.norm(d);v,J,info,g=f.evaluate(q,.01);print('INITIAL',{k:info[k] for k in ['S','U','C','Pmax','Qmax']})
  for h in [1e-4,1e-5,1e-6,1e-7]:print('GRAD',h,(f.evaluate(q+h*d,.01)[0]-f.evaluate(q-h*d,.01)[0])/(2*h),J@d)
  old=Family(a.layers);oldq=old.initial(a.beta,a.seed);print('EQUIVALENT_INITIAL_MAX_ERROR',np.max(abs(g['X']-old.coordinates(oldq)[0])))
 else:
  for i,eta in enumerate([.1,.02,.002]):q=SideSearch(f,out/f'stage{i}',eta).run(q,a.iterations)
