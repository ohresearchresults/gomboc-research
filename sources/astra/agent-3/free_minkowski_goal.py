"""Vary every base vertex and the segment generators of a bounded Minkowski body.

The base hull and complete common normal fan are rebuilt after every proposal.
All resulting physical faces, mass and centroid participate in derivatives.
"""
import argparse,json,time,hashlib
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import minimize
from gmpy2 import mpq
from minkowski_goal_search import Family


class FreeFamily(Family):
 def __init__(self,source,segments_count):
  super().__init__(source,False,segments_count);self.base_d=3*self.n;self.d=self.base_d+3*self.k
 def parameters(self,t):
  self.X=t[:self.base_d].reshape(self.n,3);h=ConvexHull(self.X);T=h.simplices.copy();a,b,c=self.X[T[:,0]],self.X[T[:,1]],self.X[T[:,2]];flip=np.einsum('ic,ic->i',np.cross(b-a,c-a),h.equations[:,:3])<0;T[flip]=T[flip][:,[0,2,1]]
  self.oldfaces=T.tolist();self.N=h.equations[:,:3];self.oldedges=np.unique(np.sort(np.concatenate([T[:,[0,1]],T[:,[1,2]],T[:,[2,0]]]),axis=1),axis=0)
  A=np.eye(3);DA=np.zeros((3,3,self.d));seg=t[self.base_d:].reshape(self.k,3);Dseg=np.zeros((self.k,3,self.d))
  for i in range(self.k):
   for j in range(3):Dseg[i,j,self.base_d+3*i+j]=1
  return A,DA,seg,Dseg
 def base_derivatives(self,t,ids):
  D=np.zeros((len(ids),3,self.d))
  for k,i in enumerate(ids):
   for j in range(3):D[k,j,3*i+j]=1
  return D
 def freeze(self,t,out):
  self.exactX=[tuple(mpq(float(v))for v in row)for row in t[:self.base_d].reshape(self.n,3)]
  return super().freeze(t,out)


def run(source,parameters,out,segments,iterations):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);fixed=Family(source,False,segments);t=np.load(parameters)
 if len(t)!=fixed.d:raise ValueError('this start must be an affine segment-family parameter vector')
 A,_,seg,_=fixed.parameters(t);X=fixed.X@A.T;seg=seg@A.T;q=np.r_[X.ravel(),seg.ravel()];c=FreeFamily(source,segments);np.save(out/'initial.npy',q)
 (out/'definition.json').write_text(json.dumps(dict(source=str(Path(source).resolve()),starting_parameters=str(Path(parameters).resolve()),starting_sha256=hashlib.sha256(Path(parameters).read_bytes()).hexdigest(),segments=segments,controls=len(q),scope='full physical base vertex and segment coordinates; common normal fan rebuilt; exact audit for every numerical110'),indent=2))
 value,G,cl,g=c.score(q,True)
 # Persistence is nonsmooth when births/deaths tie. Validate the full chain
 # in a separate generic cell, retaining the chosen optimization start.
 generic=np.array([.06,-.03,.03,-.02,.04,-2.7,1.1,.7,-2.9,2.,-.5])[:fixed.d]
 Ag,_,sg,_=fixed.parameters(generic);qg=np.r_[(fixed.X@Ag.T).ravel(),(sg@Ag.T).ravel()]
 _,Gg,cg,_=c.score(qg,True);direction=np.random.default_rng(97911).normal(size=len(q));direction/=np.linalg.norm(direction);h=1e-6;fd=(c.score(qg+h*direction)[0]-c.score(qg-h*direction)[0])/(2*h);check=dict(finite_difference=fd,analytic=float(Gg@direction),initial_census=cl,validation_census=cg,scope='generic-cell derivative check; search starts can lie on nonsmooth persistence events');(out/'gradient_check.json').write_text(json.dumps(check,indent=2));assert abs(fd-Gg@direction)<2e-4
 calls=0;best=np.inf;start=time.time();errors={}
 def fun(x):
  nonlocal calls,best
  calls+=1
  try:v,G,cl,g=c.score(x,True)
  except(ValueError,AssertionError,np.linalg.LinAlgError)as err:
   key=str(err);errors[key]=errors.get(key,0)+1;return 1e5,np.zeros_like(x)
  if v<best:
   best=v;np.save(out/'best.npy',x);(out/'best.json').write_text(json.dumps(dict(loss=v,calls=calls,seconds=time.time()-start,**cl),indent=2))
  if cl['S']==cl['U']==1:c.freeze(x,out/f'exact_nomination{calls}')
  if calls%100==0:print('FREE_MINKOWSKI_GOAL',calls,best,cl,flush=True)
  return v,G
 r=minimize(fun,q,jac=True,method='L-BFGS-B',bounds=[(-3.,3.)]*len(q),options=dict(maxiter=iterations,maxls=60,ftol=1e-15,gtol=1e-10,maxcor=25))
 np.save(out/'returned.npy',r.x);(out/'termination.json').write_text(json.dumps(dict(message=str(r.message),calls=calls,iterations=int(r.nit),best=best,rejected=errors),indent=2));print('FREE_MINKOWSKI_FINITE_STOP',best,str(r.message),flush=True)


if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('parameters');p.add_argument('out');p.add_argument('--segments',type=int,choices=[1,2],default=2);p.add_argument('--iterations',type=int,default=2000);a=p.parse_args();run(a.source,a.parameters,a.out,a.segments,a.iterations)
