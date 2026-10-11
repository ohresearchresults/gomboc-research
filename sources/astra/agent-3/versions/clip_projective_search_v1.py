"""One genuine plane cut plus a physical projective/affine deformation.
A cut of an n-vertex triangulated convex hull has E_new<=E_old+(2n-4),
since crossing edges form a planar bipartite graph. For this n=50 seed C<=480.
All retained maximal facets and the cap are explicit, not an integration triangulation.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,time,argparse,itertools
from pathlib import Path
from fractions import Fraction as R
from scipy.optimize import differential_evolution,minimize
from persistence_birth import bars_loss

def clip(X,faces,n,h,B,r):
 signed=X@n-h;inside=signed<=0;points=[];deriv=[];old={};crossings={}
 for i in np.flatnonzero(inside):old[int(i)]=len(points);points.append(X[i]);deriv.append(np.zeros((3,3)))
 def intersection(i,j):
  if signed[i]==0:return old[i]
  if signed[j]==0:return old[j]
  key=tuple(sorted((i,j)))
  if key in crossings:return crossings[key]
  e=X[j]-X[i];den=n@e;t=(h-n@X[i])/den;p=X[i]+t*e;D=np.column_stack((-e*(p@B[0])/den,-e*(p@B[1])/den,e*r/den));k=len(points);points.append(p);deriv.append(D);crossings[key]=k;return k
 newfaces=[]
 for cy in faces:
  out=[]
  for i,j in zip(cy,cy[1:]+cy[:1]):
   if inside[i]:out.append(old[i])
   if inside[i]!=inside[j]:out.append(intersection(i,j))
  if len(out)>=3:newfaces.append(out)
 if crossings:
  ids=sorted(set(crossings.values())|{old[i] for i in old if signed[i]==0});P=np.array([points[i] for i in ids]);center=P.mean(axis=0);unit=n/np.linalg.norm(n);e=np.zeros(3);e[np.argmin(abs(unit))]=1;u=np.cross(e,unit);u/=np.linalg.norm(u);v=np.cross(unit,u);order=np.argsort(np.arctan2((P-center)@v,(P-center)@u));newfaces.append([ids[i] for i in order])
 return np.array(points),newfaces,np.array(deriv)

def loss_vf(X,faces,eta=.01):
 tris=np.array([(cy[0],cy[k],cy[k+1]) for cy in faces for k in range(1,len(cy)-1)]);a,b,c=X[tris[:,0]],X[tris[:,1]],X[tris[:,2]];vol6=np.einsum('ic,ic->i',a,np.cross(b,c));D=vol6.sum();assert D>0;g=np.sum(vol6[:,None]*(a+b+c),axis=0)/(4*D);Z=X-g
 reps=[]
 for cy in faces:
  # Choose a numerically separated representative plane triple within this known facet.
  a0=cy[0];j,k=max(itertools.combinations(cy[1:],2),key=lambda p:np.linalg.norm(np.cross(X[p[0]]-X[a0],X[p[1]]-X[a0])));reps.append([a0,j,k])
 reps=np.array(reps);H=np.linalg.solve(Z[reps],np.ones((len(reps),3,1)))[:,:,0]
 edge={}
 for fi,cy in enumerate(faces):
  for i,j in zip(cy,cy[1:]+cy[:1]):edge.setdefault(tuple(sorted((i,j))),[]).append(fi)
 assert all(len(v)==2 for v in edge.values());assert len(X)-len(edge)+len(faces)==2
 pe=np.array(list(edge));qe=np.array(list(edge.values()));lp,GP,P=bars_loss(Z,pe,eta);lq,GQ,Q=bars_loss(H,qe,eta);G=GP.copy()
 w=np.linalg.solve(np.swapaxes(Z[reps],1,2),GQ[...,None])[...,0];dZT=-w[:,:,None]*H[:,None,:];np.add.at(G,reps.reshape(-1),dZT.reshape(-1,3));tg=-G.sum(axis=0);s=(a+b+c-4*g)@tg
 for k,cr in [(0,np.cross(b,c)),(1,np.cross(c,a)),(2,np.cross(a,b))]:np.add.at(G,tris[:,k],(vol6[:,None]*tg+s[:,None]*cr)/(4*D))
 info=dict(V=len(X),E=len(edge),F=len(faces),C=2*len(edge),loss=lp+lq,P=P,Q=Q,Pmax=max(P,default=0.),Qmax=max(Q,default=0.),centroid=g.tolist(),volume=float(D/6))
 return lp+lq,G,info

class Family:
 def __init__(self):
  self.source='artifacts/projected_pflow1/exact_g9/audit.json';a=json.load(open(self.source));X=np.array([[float(R(v)) for v in row] for row in a['raw_vertices']]);g=np.array([float(R(v)) for v in a['raw_centroid']]);self.X=X-g;self.faces=a['faces'];rr=a['unstable_vertices'];radii=np.sum(self.X[rr]**2,axis=1);self.target=int(rr[np.argmin(radii)]);v=self.X[self.target];self.r=np.linalg.norm(v);self.n0=v/self.r;e=np.zeros(3);e[np.argmin(abs(self.n0))]=1;b=np.cross(e,self.n0);b/=np.linalg.norm(b);self.B=np.array([b,np.cross(self.n0,b)]);self.pscale=.8/np.max(np.sum(abs(self.X),axis=1))
 def evaluate(self,t):
  n=self.n0+t[:2]@self.B;h=t[2]*self.r;X,faces,DX=clip(self.X,self.faces,n,h,self.B,self.r);a,b,c,d,e=t[3:8];p=t[8:]*self.pscale;A=np.array([[np.exp(a),c,d],[0,np.exp(b),e],[0,0,np.exp(-a-b)]]);den=1+X@p;assert den.min()>0;Y=X/den[:,None];Z=Y@A.T;val,G,info=loss_vf(Z,faces)
  GA=G.T@Y;Gy=G@A;inner=np.sum(Gy*X,axis=1);Gx=Gy/den[:,None]-inner[:,None]*p/den[:,None]**2;gc=np.einsum('ic,icp->p',Gx,DX);ga=np.array([GA[0,0]*A[0,0]-GA[2,2]*A[2,2],GA[1,1]*A[1,1]-GA[2,2]*A[2,2],GA[0,1],GA[0,2],GA[1,2]]);gp=-self.pscale*np.sum((inner/den**2)[:,None]*X,axis=0);grad=np.r_[gc,ga,gp]
  return val,grad,info,Z,dict(n=n.tolist(),h=float(h),A=A.tolist(),p=p.tolist(),faces=faces,source=self.source)

def run(out,seed,iters):
 out=Path(out);out.mkdir(exist_ok=False,parents=True);f=Family();calls=0;best=1e100;start=time.time()
 def fun(t,jac=False):
  nonlocal calls,best
  calls+=1;val,grad,info,Z,meta=f.evaluate(t)
  if val<best:
   best=val;np.save(out/'best_params.npy',t);np.save(out/'best.npy',Z);(out/'best.json').write_text(json.dumps(dict(info,calls=calls,elapsed=time.time()-start),indent=2));(out/'embedding.json').write_text(json.dumps(meta,indent=2))
  if calls%10000==0:print('CUT_PROJECTIVE',out,calls,{k:info[k] for k in ['V','E','F','Pmax','Qmax','loss']},flush=True)
  if max(info['Pmax'],info['Qmax'])<1e-11:
   np.save(out/'potential.npy',Z);np.save(out/'potential_params.npy',t);(out/'potential.json').write_text(json.dumps(info,indent=2));(out/'potential_embedding.json').write_text(json.dumps(meta,indent=2));print('POTENTIAL_CUT_PROJECTIVE110',out,info,flush=True)
  return (val,grad) if jac else val
 bounds=[(-4,4)]*2+[(.01,1.05)]+[(-.8,.8)]*5+[(-1,1)]*3;rng=np.random.default_rng(seed);initial=np.array([[rng.uniform(lo,hi) for lo,hi in bounds] for _ in range(176)]);initial[0]=0;initial[0,2]=1.01
 de=differential_evolution(fun,bounds,init=initial,maxiter=iters,seed=seed,polish=False,tol=1e-8,atol=1e-9);res=minimize(lambda t:fun(t,True),np.load(out/'best_params.npy'),jac=True,method='L-BFGS-B',bounds=bounds,options={'maxiter':4000,'maxls':50,'ftol':1e-15,'gtol':1e-11});print('CUT_PROJECTIVE_DONE',out,de.message,res.message,json.load(open(out/'best.json')),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--out',default='artifacts/cut_projective1');p.add_argument('--seed',type=int,default=39001);p.add_argument('--iterations',type=int,default=1200);p.add_argument('--check',action='store_true');a=p.parse_args()
 if a.check:
  f=Family();t=np.zeros(11);t[:3]=[.37,-.13,.72];d=np.random.default_rng(443).normal(size=11);d/=np.linalg.norm(d);v,G,*_=f.evaluate(t)
  for h in [1e-4,1e-5,1e-6]:print('CUT_GRAD',h,(f.evaluate(t+h*d)[0]-f.evaluate(t-h*d)[0])/(2*h),G@d)
 else:run(a.out,a.seed,a.iterations)
