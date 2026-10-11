"""Nonhomothetic m-gon sections with independent concave side supports.
All side planes share fixed horizontal normal directions. Vertices are exact
adjacent-plane intersections; validity requires every side to remain active.
Convexity is global because all m signed support functions are concave.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.special import softmax
from scipy.optimize import minimize,LinearConstraint
from triangular_sections import Family,Search
from rectangular_sections import topology

class PolygonFamily(Family):
 def __init__(self,m,L):
  self.m=m;self.L=L;self.d=(m+1)*L+4;self.n=m*L+2;self.faces,self.tris,self.ft,self.pe,self.qe=topology(m,L);ang=2*np.pi*np.arange(m)/m;self.normals=np.column_stack((np.cos(ang),np.sin(ang)));self.R=np.zeros((m,2,m))
  for j in range(m):
   rows=[(j-1)%m,j];self.R[j][:,rows]=np.linalg.inv(self.normals[rows])
  # W-polytope validity: all candidate adjacent intersections obey all sides.
  self.K=np.array([np.eye(m)[k]-self.normals[k]@self.R[j] for j in range(m) for k in range(m) if k not in [(j-1)%m,j]])
 def initial(self,beta,seed):
  L=self.L;m=self.m;z=np.linspace(-1,1,L+2);r=np.sqrt(1-z*z);phase=1.5*np.pi*(z-z**3/3);mu=beta*np.column_stack((np.cos(phase)+1,np.sin(phase)));k=-np.diff(np.diff(r)/np.diff(z));a=np.diff(np.diff(mu,axis=0)/np.diff(z)[:,None],axis=0)/k[:,None];W=k[:,None]*(1-a@self.normals.T);assert (W>0).all() and min((W@self.K.T).ravel())>0;q=np.r_[np.zeros(L),W.ravel(),np.zeros(4)];rng=np.random.default_rng(seed)
  if seed:q[:L]+=rng.normal(size=L)*.1
  return q
 def coordinates(self,q):
  L=self.L;m=self.m;d=self.d;w=softmax(np.r_[q[:L],0.]);Dw=(np.diag(w)-np.outer(w,w))[:,:L];z=-1+2*np.cumsum(w)[:-1];Dz=np.zeros((L,d));Dz[:,:L]=2*np.cumsum(Dw,axis=0)[:-1];W=q[L:(m+1)*L].reshape(L,m);DW=np.zeros((L,m,d));DW[:,:,L:(m+1)*L]=np.eye(m*L).reshape(L,m,m*L)
  ii,jj=np.indices((L,L));mi=np.minimum(ii,jj);ma=np.maximum(ii,jj);G=(z[mi]+1)*(1-z[ma])/2;DG=((1-z[ma])[...,None]*Dz[mi]-(z[mi]+1)[...,None]*Dz[ma])/2;values=G@W;Dval=np.einsum('ijp,jc->icp',DG,W)+np.einsum('ij,jcp->icp',G,DW);v=q[-4:-2];Dv=np.zeros((2,d));Dv[:,-4:-2]=np.eye(2);mu=(z[:,None]+1)/2*v;Dmu=np.einsum('ip,c->icp',Dz/2,v)+(z[:,None,None]+1)/2*Dv
  X=np.zeros((self.n,3));DX=np.zeros((self.n,3,d));X[0,2]=-1;X[-1]=np.r_[v,1.];DX[-1,:2]=Dv;X[1:-1,:2]=(np.einsum('jck,ik->ijc',self.R,values)+mu[:,None,:]).reshape(-1,2);X[1:-1,2]=np.repeat(z,m);DX[1:-1,:2]=(np.einsum('jck,ikp->ijcp',self.R,Dval)+Dmu[:,None,:,:]).reshape(-1,2,d);DX[1:-1,2]=np.repeat(Dz,m,axis=0)
  A=np.array([[np.exp(q[-2]),q[-1]],[0.,np.exp(-q[-2])]]);xy=X[:,:2].copy();DX[:,:2]=np.einsum('ab,nbp->nap',A,DX[:,:2]);DX[:,0,-2]+=A[0,0]*xy[:,0];DX[:,1,-2]-=A[1,1]*xy[:,1];DX[:,0,-1]+=xy[:,1];X[:,:2]=xy@A.T
  return X,DX,dict(kind=np.array('independent_polygon_curvatures'),z=z,W=W,normals=self.normals,tilt=v,A=A)

class PolygonSearch(Search):
 def run(self,q,iters):
  f=self.f;L=f.L;m=f.m;mat=np.zeros((L*len(f.K),len(q)));mat[:,L:(m+1)*L]=np.kron(np.eye(L),f.K);ineq=LinearConstraint(mat,1e-7,np.inf);bounds=[(-4.,4.)]*L+[(1e-6,100.)]*(m*L)+[(-3.,3.)]*2+[(-1.5,1.5),(-2.,2.)]
  r=minimize(self.evaluate,q,jac=True,method='SLSQP',bounds=bounds,constraints=[ineq],options=dict(maxiter=iters,ftol=1e-11));(self.out/'termination.json').write_text(json.dumps(dict(message=r.message,nit=r.nit,success=bool(r.success)),indent=2));print('POLYGON_SECTION_DONE',self.out,r.message,flush=True);return np.load(self.out/'best_params.npy')

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('out');p.add_argument('--sides',type=int,default=5);p.add_argument('--layers',type=int,default=24);p.add_argument('--seed',type=int,default=1);p.add_argument('--beta',type=float,default=.025);p.add_argument('--iterations',type=int,default=3000);p.add_argument('--check',action='store_true');a=p.parse_args();f=PolygonFamily(a.sides,a.layers);q=f.initial(a.beta,a.seed);out=Path(a.out);out.mkdir(parents=True,exist_ok=False);np.save(out/'initial_params.npy',q);(out/'input.json').write_text(json.dumps(dict(sides=a.sides,layers=a.layers,seed=a.seed,beta=a.beta,C=2*a.sides*(2*a.layers+1),method='independent positive side curvatures constrained to common polygon normal fan')))
 if a.check:
  rng=np.random.default_rng(1023);d=rng.normal(size=q.shape);d/=np.linalg.norm(d);v,J,info,g=f.evaluate(q,.01);print('INITIAL',{k:info[k] for k in ['S','U','C','Pmax','Qmax']})
  for h in [1e-4,1e-5,1e-6,1e-7]:print('GRAD',h,(f.evaluate(q+h*d,.01)[0]-f.evaluate(q-h*d,.01)[0])/(2*h),J@d)
  from vertex_geometry import geometry
  gg=geometry(g['X'],False);print('REHULL_MASS_ERROR',np.max(abs(gg['g']-g['g'])),abs(gg['V']-g['V']));print('MAX_SUPPORT_SLACK',np.max(g['H']@g['Z'].T-1));np.savez(out/'initial_construction.npz',**g['construction'])
 else:
  for i,eta in enumerate([.1,.02,.002]):q=PolygonSearch(f,out/f'stage{i}',eta).run(q,a.iterations)
