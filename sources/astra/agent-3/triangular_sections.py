"""Convex translated triangular sections, own uniform mass, full analytic Jacobian.
Mathematical Green-function chart communicated by agent2; this implementation
is independent NumPy differentiation, with an always-convex affine triangle.
L knots give V=3L+2,E=6L+3,F=3L+3,C=12L+6. True side facets are quads.
"""
import argparse,json,time,hashlib
from pathlib import Path
import numpy as np
from scipy.special import softmax
from scipy.optimize import minimize,root
from persistence_birth import bars_loss
from support_geometry import escape

B=np.array([[1.,0.],[-.5,1.],[-.5,-1.]])
class Family:
 def __init__(self,L):
  self.L=L;self.d=4*L+4;self.n=3*L+2;self.faces=[]
  for j in range(3):self.faces.append([0,1+(j+1)%3,1+j])
  for i in range(L-1):
   for j in range(3):self.faces.append([1+3*i+j,1+3*i+(j+1)%3,1+3*(i+1)+(j+1)%3,1+3*(i+1)+j])
  for j in range(3):self.faces.append([1+3*(L-1)+j,1+3*(L-1)+(j+1)%3,self.n-1])
  self.tris=np.array([(f[0],f[i],f[i+1]) for f in self.faces for i in range(1,len(f)-1)]);self.ft=np.array([f[:3] for f in self.faces]);owners={}
  for i,f in enumerate(self.faces):
   for j,k in zip(f,f[1:]+f[:1]):owners.setdefault(tuple(sorted((j,k))),[]).append(i)
  self.pe=np.array(list(owners));self.qe=np.array(list(owners.values()));assert len(self.pe)==6*L+3
 def coordinates(self,q):
  L=self.L;d=self.d;w=softmax(np.r_[q[:L],0.]);Dw=(np.diag(w)-np.outer(w,w))[:,:L];z=-1+2*np.cumsum(w)[:-1];Dz=np.zeros((L,d));Dz[:,:L]=2*np.cumsum(Dw,axis=0)[:-1]
  k=np.exp(q[L:2*L]);Dk=np.zeros((L,d));Dk[:,L:2*L]=np.diag(k);lam=q[2*L:4*L].reshape(L,2);wa=softmax(lam@B.T,axis=1);a=wa@B;Da=np.zeros((L,2,d))
  for i in range(L):Da[i,:,2*L+2*i:2*L+2*i+2]=(B.T*wa[i])@B-np.outer(a[i],a[i])
  ii,jj=np.indices((L,L));mi=np.minimum(ii,jj);ma=np.maximum(ii,jj);G=(z[mi]+1)*(1-z[ma])/2;DG=((1-z[ma])[...,None]*Dz[mi]-(z[mi]+1)[...,None]*Dz[ma])/2
  r=G@k;Dr=np.einsum('ijp,j->ip',DG,k)+G@Dk;v=q[4*L:4*L+2];Dv=np.zeros((2,d));Dv[:,4*L:4*L+2]=np.eye(2)
  mu=(z[:,None]+1)/2*v-G@(k[:,None]*a);Dmu=np.einsum('ip,c->icp',Dz/2,v)+(z[:,None,None]+1)/2*Dv-np.einsum('ijp,j,jc->icp',DG,k,a)-np.einsum('ij,jp,jc->icp',G,Dk,a)-np.einsum('ij,j,jcp->icp',G,k,Da)
  X=np.zeros((self.n,3));DX=np.zeros((self.n,3,d));X[0,2]=-1;X[-1]=np.r_[v,1.];DX[-1,:2]=Dv
  X[1:-1,:2]=(mu[:,None,:]+r[:,None,None]*B).reshape(-1,2);X[1:-1,2]=np.repeat(z,3);DX[1:-1,:2]=(Dmu[:,None,:,:]+Dr[:,None,None,:]*B[None,:,:,None]).reshape(-1,2,d);DX[1:-1,2]=np.repeat(Dz,3,axis=0)
  A=np.array([[np.exp(q[-2]),q[-1]],[0.,np.exp(-q[-2])]]);xy=X[:,:2].copy();DX[:,:2]=np.einsum('ab,nbp->nap',A,DX[:,:2]);DX[:,0,-2]+=A[0,0]*xy[:,0];DX[:,1,-2]-=A[1,1]*xy[:,1];DX[:,0,-1]+=xy[:,1];X[:,:2]=xy@A.T
  return X,DX,dict(z=z,k=k,a=a,r=r,mu=mu,tilt=v,A=A,base=B)
 def physical(self,q):
  X,DX,data=self.coordinates(q);T=self.tris;a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];da,db,dc=DX[T[:,0]],DX[T[:,1]],DX[T[:,2]];v6=np.einsum('ic,ic->i',a,np.cross(b,c));V=v6.sum()/6;assert V>0
  M=np.sum(v6[:,None]*(a+b+c),axis=0)/24;g=M/V;dv=np.einsum('ic,icp->ip',np.cross(b,c),da)+np.einsum('ic,icp->ip',np.cross(c,a),db)+np.einsum('ic,icp->ip',np.cross(a,b),dc);DV=dv.sum(0)/6;DM=(np.einsum('ip,ic->cp',dv,a+b+c)+np.einsum('i,icp->cp',v6,da+db+dc))/24;Dg=(DM-g[:,None]*DV)/V;Z=X-g;DZ=DX-Dg
  H=np.linalg.solve(Z[self.ft],np.ones((len(self.ft),3,1)))[...,0];DH=np.linalg.solve(Z[self.ft],-np.einsum('fc,fvcp->fvp',H,DZ[self.ft]));assert np.isfinite(H).all() and np.isfinite(DH).all()
  return dict(X=X,Z=Z,H=H,g=g,V=V,DX=DX,DZ=DZ,DH=DH,Dg=Dg,construction=data)
 def evaluate(self,q,eta):
  g=self.physical(q);p,GP,P=bars_loss(g['Z'],self.pe,eta);r,GQ,Q=bars_loss(g['H'],self.qe,eta);J=np.einsum('ic,icp->p',GP,g['DZ'])+np.einsum('ic,icp->p',GQ,g['DH']);info=dict(loss=p+r,P=P,Q=Q,Pmax=max(P,default=0.),Qmax=max(Q,default=0.),S=int(np.sum(escape(g['H'])[0]<0)),U=int(np.sum(escape(g['Z'])[0]<0)),V=self.n,E=len(self.pe),F=len(self.faces),C=2*len(self.pe),centroid=g['g'].tolist(),volume=float(g['V']))
  return p+r,J,info,g
 def initial(self,beta,seed):
  L=self.L;z=np.linspace(-1,1,L+2);r=np.sqrt(1-z*z);phase=1.5*np.pi*(z-z**3/3);mu=beta*np.column_stack((np.cos(phase)+1,np.sin(phase)));k=-np.diff(np.diff(r)/np.diff(z));a=np.diff(np.diff(mu,axis=0)/np.diff(z)[:,None],axis=0)/k[:,None];lam=[]
  for ai in a:
   def fun(x):return softmax(B@x)@B-ai
   sol=root(fun,np.zeros(2));assert sol.success and np.linalg.norm(fun(sol.x))<1e-9
   lam.append(sol.x)
  q=np.r_[np.zeros(L),np.log(k),np.array(lam).ravel(),np.zeros(4)];rng=np.random.default_rng(seed)
  if seed:q[L:2*L]+=rng.normal(size=L)*.08;q[2*L:4*L]+=rng.normal(size=2*L)*.2
  return q

class Search:
 def __init__(self,f,out,eta):
  self.f=f;self.out=Path(out);self.out.mkdir(parents=True,exist_ok=False);self.eta=eta;self.best=np.inf;self.calls=0;self.start=time.time()
 def evaluate(self,q):
  self.calls+=1;v,J,info,g=self.f.evaluate(q,self.eta);info.update(calls=self.calls,seconds=time.time()-self.start)
  if v<self.best:
   self.best=v;np.save(self.out/'best_params.npy',q);np.save(self.out/'best_vertices.npy',g['X']);(self.out/'best.json').write_text(json.dumps(info,indent=2));np.savez(self.out/'construction.npz',**g['construction']);(self.out/'incidence.json').write_text(json.dumps(dict(faces=self.f.faces,edges=self.f.pe.tolist(),dual_edges=self.f.qe.tolist())))
  if self.calls%1000==0:print('TRI_SECTIONS',self.out,{k:info[k] for k in ['calls','S','U','Pmax','Qmax','loss','seconds']},flush=True)
  if info['S']==info['U']==1:
   np.save(self.out/f'potential_params_{self.calls}.npy',q);np.savez(self.out/f'potential_construction_{self.calls}.npz',**g['construction']);(self.out/f'potential_{self.calls}.json').write_text(json.dumps(info,indent=2));print('SECTION_POTENTIAL_NEEDS_EXACT_CONSTRUCTION_AUDIT',info,flush=True)
  return v,J
 def run(self,q,iters):
  L=self.f.L;bounds=[(-4.,4.)]*L+[(-10.,5.)]*L+[(-6.,6.)]*(2*L)+[(-3.,3.)]*2+[(-1.5,1.5),(-2.,2.)];r=minimize(self.evaluate,q,jac=True,method='L-BFGS-B',bounds=bounds,options=dict(maxiter=iters,maxls=45,maxcor=25,ftol=1e-14,gtol=1e-10));(self.out/'termination.json').write_text(json.dumps(dict(message=r.message,nit=r.nit,success=bool(r.success)),indent=2));print('SECTION_DONE',self.out,r.message,flush=True);return np.load(self.out/'best_params.npy')

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('out');p.add_argument('--layers',type=int,default=40);p.add_argument('--seed',type=int,default=1);p.add_argument('--beta',type=float,default=.015);p.add_argument('--iterations',type=int,default=3000);p.add_argument('--check',action='store_true');a=p.parse_args();f=Family(a.layers);q=f.initial(a.beta,a.seed);out=Path(a.out);out.mkdir(parents=True,exist_ok=False);np.save(out/'initial_params.npy',q);(out/'input.json').write_text(json.dumps(dict(layers=a.layers,seed=a.seed,beta=a.beta,C=12*a.layers+6,mathematical_source='agent2 Green-function section chart; independent NumPy analytic Jacobians and fixed affine triangular section')))
 if a.check:
  rng=np.random.default_rng(753);d=rng.normal(size=q.shape);d/=np.linalg.norm(d);v,J,info,g=f.evaluate(q,.01);print('INITIAL',info)
  for h in [1e-4,1e-5,1e-6,1e-7]:print('GRAD',h,(f.evaluate(q+h*d,.01)[0]-f.evaluate(q-h*d,.01)[0])/(2*h),J@d)
  from vertex_geometry import geometry
  gg=geometry(g['X'],False);print('REHULL_MASS_ERROR',np.max(abs(gg['g']-g['g'])),abs(gg['V']-g['V']));print('MAX_SUPPORT_SLACK',np.max(g['H']@g['Z'].T-1))
 else:
  for i,eta in enumerate([.1,.02,.002]):q=Search(f,out/f'stage{i}',eta).run(q,a.iterations)
