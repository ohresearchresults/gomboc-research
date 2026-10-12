"""Finite two-cap mass compensation. All outputs here are numerical diagnostics."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import sys,json,time
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
from scipy.optimize import root,least_squares
sys.set_int_max_str_digits(0)
CAPS={99:[([0,2],[1,3,10,95]),([83,85,87,91,93,96,98,102,105,110,113],[79,90,95,116])],117:[([0,2],[1,3,10,93]),([82,83,85,89,91,94,96,100,103,108,111],[79,88,93,114])]}
CAPS[84]=CAPS[99]
class Mesh:
 def __init__(self,P,faces):
  self.P0=P.copy();self.faces=[list(f) for f in faces];self.n=len(P);self.nf=len(faces)
  self.tri=np.array([[cy[0],cy[k],cy[k+1]] for cy in faces for k in range(1,len(cy)-1)])
  self.ft=np.array([cy[:3] for cy in faces]);self.inc=np.zeros((len(faces),len(P)),bool);ef={}
  for f,cy in enumerate(faces):
   self.inc[f,cy]=True
   for i,j in zip(cy,cy[1:]+cy[:1]):ef.setdefault(tuple(sorted((i,j))),[]).append(f)
  assert all(len(v)==2 for v in ef.values())
  self.ep=np.array(sorted(ef));self.ed=np.array([ef[tuple(e)] for e in self.ep]);self.src=np.r_[self.ep[:,0],self.ep[:,1]];self.dst=np.r_[self.ep[:,1],self.ep[:,0]];self.fs=np.r_[self.ed[:,0],self.ed[:,1]];self.fd=np.r_[self.ed[:,1],self.ed[:,0]]
 def mass(self,P):
  t=P[self.tri];d=np.einsum('ij,ij->i',t[:,0],np.cross(t[:,1],t[:,2]));v=d.sum()/6;M=np.einsum('i,ij->j',d,t.sum(axis=1))/24
  return v,M,M/v
 def state(self,P,c=None):
  v,M,g=self.mass(P)
  if c is None:c=g
  X=P-c;ft=X[self.ft];N=np.cross(ft[:,1]-ft[:,0],ft[:,2]-ft[:,0]);N/=np.linalg.norm(N,axis=1)[:,None];h=np.einsum('ij,ij->i',N,ft[:,0]);Y=N/h[:,None]
  gap=h[:,None]-N@X.T;plan=np.max(abs(gap[self.inc]));gap[self.inc]=np.inf
  e=X[self.dst]-X[self.src];pv=np.einsum('ij,ij->i',X[self.src],e)/(np.linalg.norm(X[self.src],axis=1)*np.linalg.norm(e,axis=1))
  e2=Y[self.fd]-Y[self.fs];dv=np.einsum('ij,ij->i',Y[self.fs],e2)/(np.linalg.norm(Y[self.fs],axis=1)*np.linalg.norm(e2,axis=1))
  ptop=np.full(self.n,-np.inf);dtop=np.full(self.nf,-np.inf);np.maximum.at(ptop,self.src,pv);np.maximum.at(dtop,self.fs,dv)
  U=np.where(ptop<0)[0];S=np.where(dtop<0)[0]
  e=X[self.ep[:,1]]-X[self.ep[:,0]];a=-np.einsum('ij,ij->i',X[self.ep[:,0]],e)/np.einsum('ij,ij->i',e,e);foot=X[self.ep[:,0]]+a[:,None]*e
  n,m=N[self.ed[:,0]],N[self.ed[:,1]];k=np.cross(n,m);kk=np.einsum('ij,ij->i',k,k)
  b=np.einsum('ij,ij->i',np.cross(foot,m),k)/kk;c2=np.einsum('ij,ij->i',np.cross(n,foot),k)/kk
  H=self.ep[(a>0)&(a<1)&(b>0)&(c2>0)]
  return dict(counts=[len(S),len(U),len(H)],S=S.tolist(),U=U.tolist(),H=H.tolist(),volume=float(v),moment=M.tolist(),centroid=g.tolist(),min_gap=float(gap.min()),min_offset=float(h.min()),planarity=float(plan),pv=pv,dv=dv,ptop=ptop,dtop=dtop)
 @staticmethod
 def brief(s):return {k:v for k,v in s.items() if k not in ('pv','dv','ptop','dtop')}
class Compensated:
 def __init__(self,report,deleted,u,w):
  self.d=json.loads(Path(report).read_text());self.P=np.array([[float(Q(x)) for x in row] for row in self.d['raw_vertices']]);self.c=np.array([float(Q(x)) for x in self.d['raw_centroid']]);self.u=u;self.w=w
  faces=[list(f) for f in self.d['faces']];adj={j if i==u else i for i,j in self.d['edges'] if u in (i,j)};assert len(adj)==3 and w in adj;self.ab=sorted(adj-{w});self.deleted=deleted
  f=next(i for i,cy in enumerate(faces) if u in cy and w not in cy);assert len(faces[f])>=4;faces[f].remove(u);tr=[*self.ab,u];P=self.P.copy();P[u]=(P[u]+P[w])/2
  if np.cross(P[tr[1]]-P[tr[0]],P[tr[2]]-P[tr[0]])@(self.P[u]-P[tr[0]])<0:tr.reverse()
  faces.append(tr);self.mesh=Mesh(self.P,faces);self.caps=[]
  for inds,sep in CAPS[deleted]:
   assert u not in inds and u not in sep
   B=np.c_[self.P[sep],np.ones(4)].T;beta=np.c_[self.P[inds],np.ones(len(inds))]@np.linalg.inv(B).T
   self.caps.append((inds,sep,beta))
  # stable normal correction coordinates are eta=lambda-1, not logarithms.
 def points(self,s,z):
  P=self.P.copy();P[self.u]=(1-s)*P[self.u]+s*P[self.w];dens=[]
  for ci,(inds,sep,beta) in enumerate(self.caps):
   eta=np.array([0,0,z[0],0]) if ci==0 else np.array([z[1],z[2],0,0]);d=1+beta@eta;dens.extend(d)
   P[inds]=(P[inds]+(beta*eta)@self.P[sep])/d[:,None]
  return P,np.array(dens)
 def close(self,s,z):
  def fun(z):
   P,den=self.points(s,z);v,M,c=self.mesh.mass(P);return c-self.c
  sol=root(fun,z,method='hybr',options={'xtol':1e-11})
  P,d=self.points(s,sol.x);ans=self.mesh.brief(self.mesh.state(P));ans.update(s=float(s),eta=sol.x.tolist(),min_den=float(d.min()),com_error=float(np.linalg.norm(fun(sol.x))),root_success=bool(sol.success))
  return ans
if __name__=='__main__':
 report,deleted,u,w,out=sys.argv[1:];m=Compensated(report,int(deleted),int(u),int(w));z=np.zeros(3);records=[]
 for s in np.r_[np.logspace(-8,-2,13),np.linspace(.02,.98,49),[.99,.999]]:
  r=m.close(float(s),z);records.append(r)
  if r['com_error']<1e-10:z=np.array(r['eta'])
  print(r['s'],r['counts'],r['com_error'],r['min_gap'],r['eta'],r['min_den'],flush=True)
 Path(out).write_text(json.dumps(records,sort_keys=True,separators=(',',':')))
