"""Regular blow-up chart for a vanishing edge between two free contact nodes.
Write B=A+epsilon*r, r[k]=sign. Common supports impose q.A=1,q.r=0.
No numerical inverse of an almost repeated A/B incidence is used.
"""
import sys,json,time,argparse,itertools
from pathlib import Path
import numpy as np
from scipy.linalg import svd
R=Path(__file__).resolve().parent;sys.path[:0]=[str(R/'parent/parent/mechanism'),str(R/'parent/parent/mechanism/parent_sources')]
from atlas_opt import Atlas
from minnorm_qp import solve
from numeric import recover,merge_faces,mechanics
class Model(Atlas):
 def __init__(self,data,fs,a,b):
  self.aa=a;self.bb=b;self.blowup=False
  super().__init__(data,fs,stable=3)
  assert a==self.n or next(z for z in self.plan if z[0]==a)[1].size==0
  assert next(z for z in self.plan if z[0]==b)[1].size==0
  X=recover(data);diff=X[b]-X[a];self.axis=int(np.argmax(abs(diff)));self.sgn=float(np.sign(diff[self.axis]));self.eps0=abs(diff[self.axis]);rv=diff/self.eps0
  par=rv.copy();par[self.axis]=self.eps0
  for j,(i,k) in enumerate(self.free):
   if i==b:self.u0[j]=par[k]/self.scale[j]
  self.blowup=True
  self.ai=next(i for i,o in enumerate(self.owners) if set(o)==set(data['groups'][a-self.n]));self.bi=next(i for i,o in enumerate(self.owners) if set(o)==set(data['groups'][b-self.n]))
  self.ui=np.array([i for i in range(len(self.owners)) if i not in (self.Uroot,self.bi)])
  s=self.state(self.u0,False);self.sparent=s['cs'].argmax(1);self.uparent=s['cu'].argmax(1)
  v=s['cu'][self.ai].copy();v[self.bi]=-np.inf;self.uparent[self.ai]=v.argmax()
  s=self.state(self.u0,False);self.floor=np.maximum(5e-10,np.minimum(1e-5,s['vals']*.4));assert np.all(s['vals']>self.floor),(s['vals'].min(),self.ai,self.bi)
  self.guard=~self.inc.copy();uni=set(self.owners[self.ai])|set(self.owners[self.bi])
  for i in [self.ai,self.bi]:self.guard[i,list(uni)]=False
  self.geo0=s['gaps'].copy();self.vanish=np.array([self.ai in t and self.bi in t for t in self.tri]);self.epindex=next(j for j,(i,k) in enumerate(self.free) if i==b and k==self.axis)
  print('BLOWUP',self.ai,self.bi,a,b,self.axis,self.sgn,self.eps0,'vanishing fans',int(self.vanish.sum()),flush=True)
 def chart(self,u,jac=True):
  if not self.blowup:return super().chart(u,jac)
  X=self.fixed.copy();X[self.free[:,0],self.free[:,1]]=u*self.scale
  if jac:
   DX=np.zeros((self.M,3,self.np));DX[self.free[:,0],self.free[:,1],np.arange(self.np)]=self.scale
  eps=X[self.bb,self.axis];r=X[self.bb].copy();r[self.axis]=self.sgn
  if jac:dr=DX[self.bb].copy();dr[self.axis]=0;de=DX[self.bb,self.axis].copy()
  X[self.bb]=X[self.aa]+eps*r
  if jac:DX[self.bb]=DX[self.aa]+r[:,None]*de[None,:]+eps*dr
  for i,deps,ax,rest in self.plan:
   if len(deps):
    V=X[deps].copy();rhs=np.ones(len(deps));special=self.aa in deps and self.bb in deps
    if jac:DV=DX[deps].copy()
    if special:
     row=int(np.flatnonzero(deps==self.bb)[0]);V[row]=r;rhs[row]=0
     if jac:DV[row]=dr
    mat=V[:,ax];val=np.linalg.solve(mat,rhs-V[:,rest]@X[i,rest]);X[i,ax]=val
    if jac:
     rr=-np.einsum('rcp,c->rp',DV,X[i])
     if len(rest):rr-=V[:,rest]@DX[i,rest]
     DX[i,ax]=np.linalg.solve(mat,rr)
  return (X,DX) if jac else X
 def state(self,u,jac=True):
  if not hasattr(self,'ai'):return super().state(u,jac)
  for key in ['sparent','uparent']:
   if hasattr(self,key):delattr(self,key)
  prelim=super().state(u,False);self.sparent=prelim['cs'].argmax(1);self.uparent=prelim['cu'].argmax(1)
  vv=prelim['cu'][self.ai].copy();vv[self.bi]=-np.inf;self.uparent[self.ai]=vv.argmax()
  return super().state(u,jac)
 def epsilon(self,u):return u[self.epindex]*self.scale[self.epindex]
 def allstate(self,u,jac=True):
  s=self.state(u,jac)
  if jac:
   mat=np.r_[s['dq'].reshape(-1,self.np)/2,s['dP'].reshape(-1,self.np)];_,d,Vt=svd(mat,full_matrices=False,check_finite=False);s['W']=Vt.T/np.maximum(d,1e-10)
  return s
 def rows(self,s):
  vi,qi=np.where(self.guard&(s['gaps']<.04));gf=np.maximum(1e-9,np.minimum(1e-6,self.geo0[vi,qi]*.01))
  return np.r_[s['J'],self.gap_jac(s,vi,qi)]@s['W'],np.r_[1.1*self.floor-s['vals'],gf-s['gaps'][vi,qi]]
 def valid(self,s):
  return np.isfinite(s['vals']).all() and (s['vals']-self.floor).min()>-1e-12 and s['vals'].min()>0 and s['gaps'][self.guard].min()>1e-10 and s['det'][~self.vanish].min()>1e-12 and s['det'][self.vanish].min()>-1e-11 and s['h'].min()>0
 def endpoint(self,u):
  d=json.loads(json.dumps(self.data));X=self.chart(u,False);a=self.aa;b=self.bb;d['controls']=np.rint(X*d['grid']).astype(np.int64).tolist();d['controls'].pop(b)
  d['groups'][a-self.n]=sorted(set(d['groups'][a-self.n])|set(d['groups'][b-self.n]));d['groups'].pop(b-self.n)
  alias=lambda i:(a if i==b else i)-(i>b)
  plan=[]
  for i,deps,axes in d['plan']:
   if i==b:continue
   ds=list(dict.fromkeys(a if j==b else j for j in deps))
   if len(ds)!=len(deps):axes=list(max(itertools.combinations(range(3),len(ds)),key=lambda ax:abs(np.linalg.det(X[np.ix_(ds,ax)]))))
   plan.append([alias(i),[alias(j) for j in ds],axes])
  d['plan']=plan;return d,merge_faces(self.faces,self.ai,self.bi)
