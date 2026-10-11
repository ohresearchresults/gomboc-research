"""Full contact equations and analytic own-filled-mass derivatives; no fixed drawing."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import numpy as np,json,copy
import sys
sys.set_int_max_str_digits(0)
from pathlib import Path
from scipy.optimize import least_squares
ROOT=Path(__file__).parent

def contact(data,coordinates,free,derivatives=True):
 Y=np.array(data['controls'],float)/data['grid'];n=len(free);DY=np.zeros((len(Y),3,n));Y[137]=[0,0,1]
 for k,(i,a) in enumerate(free):Y[i,a]=coordinates[k];DY[i,a,k]=1
 for i,deps,axes in data['plan']:
  if not deps:continue
  rest=[k for k in range(3) if k not in axes];A=Y[np.ix_(deps,axes)]
  Y[i,axes]=np.linalg.solve(A,1-Y[np.ix_(deps,rest)]@Y[i,rest])
  if derivatives:
   rhs=-np.einsum('c,acp->ap',Y[i],DY[deps])
   if rest:rhs-=Y[np.ix_(deps,rest)]@DY[i,rest]
   DY[i,axes]=np.linalg.solve(A,rhs)
 return Y,DY

import itertools

class Atlas:
 def escape(self,A,DA,forced=None):
  e=A[None,:,:]-A[:,None,:];aa=np.sum(A*A,axis=1);ee=np.sum(e*e,axis=2);den=np.sqrt(np.maximum(aa[:,None]*ee,1e-40));vals=np.einsum('ik,ijk->ij',A,e)/den;np.fill_diagonal(vals,-1e10)
  js=np.argmax(vals,axis=1)
  for ii,jj in (forced or {}).items():js[ii]=jj
  i=np.arange(len(A));v=vals[i,js];d=A[js]-A;dd=np.sum(d*d,axis=1);de=DA[js]-DA;den=np.sqrt(np.maximum(aa*dd,1e-40))
  Dv=(np.einsum('ic,icp->ip',d,DA)+np.einsum('ic,icp->ip',A,de))/den[:,None]-v[:,None]*(np.einsum('ic,icp->ip',A,DA)/aa[:,None]+np.einsum('ic,icp->ip',d,de)/np.maximum(dd[:,None],1e-40))
  return v,Dv
 def evaluate(self,z,refresh=False):
  if not refresh and self.last is not None and np.array_equal(z,self.last[0]):return self.last[1:]
  Y,DY=contact(self.G,self.base+self.scale*z,self.free);DY=DY*self.scale[None,None,:];Q=Y[:137];DQ=DY[:137]
  X=np.empty((self.nv,3));DX=np.empty((self.nv,3,self.n));ix=self.direct>=0;X[ix]=Y[self.direct[ix]];DX[ix]=DY[self.direct[ix]]
  As=Q[self.trip];X[self.simple]=np.linalg.solve(As,np.ones((len(self.simple),3,1)))[:,:,0]
  DX[self.simple]=np.linalg.solve(As,-np.einsum('nc,nacp->nap',X[self.simple],DQ[self.trip]))
  a,b,c=X[self.tris[:,0]],X[self.tris[:,1]],X[self.tris[:,2]];da,db,dc=DX[self.tris[:,0]],DX[self.tris[:,1]],DX[self.tris[:,2]]
  v6=np.einsum('ic,ic->i',a,np.cross(b,c));dv6=np.einsum('ic,icp->ip',np.cross(b,c),da)+np.einsum('ic,icp->ip',np.cross(c,a),db)+np.einsum('ic,icp->ip',np.cross(a,b),dc)
  V=v6.sum()/6;DV=dv6.sum(axis=0)/6;M=(v6[:,None]*(a+b+c)).sum(axis=0)/24;DM=(np.einsum('ip,ic->cp',dv6,a+b+c)+np.einsum('i,icp->cp',v6,da+db+dc))/24;g=M/V;Dg=(DM-g[:,None]*DV)/V
  Z=X-g;DZ=DX-Dg;h=1-Q@g;Dh=-np.einsum('icp,c->ip',DQ,g)-Q@Dg;H=Q/h[:,None];DH=DQ/h[:,None,None]-Q[:,:,None]*Dh[:,None,:]/h[:,None,None]**2
  ep,dep=self.escape(Z,DZ,self.forcedp);eq,deq=self.escape(H,DH,self.forcedq)
  mech=np.r_[ep[self.keptp],eq[self.keptq],-ep[self.U],-eq[3]];dmech=np.vstack((dep[self.keptp],deq[self.keptq],-dep[self.U],-deq[3]))
  slack=1-Q@X.T;masked=np.where(self.mask,slack,np.inf);arg=masked.argmin(axis=1);cs=slack[np.arange(137),arg];dcs=-np.einsum('icp,ic->ip',DQ,X[arg])-np.einsum('ic,icp->ip',Q,DX[arg])
  val=np.r_[mech,cs,v6/self.tscale,h,V];jac=np.vstack((dmech,dcs,dv6/self.tscale[:,None],Dh,DV))
  geo=dict(Q=Q,X=X,V=V,g=g,M=M,v6=v6,slack=masked,Y=Y)
  self.last=(np.array(z).copy(),val,jac,geo);return val,jac,geo
 def residual(self,z):
  v,J,g=self.evaluate(z);active=v<self.floor
  return np.maximum(self.floor-v,0)/self.rescale
 def derivative(self,z):
  v,J,g=self.evaluate(z);return -J/self.rescale[:,None]*(v<self.floor)[:,None]


def install(s,Q):
 def point(ids):
  tri=max(itertools.combinations(ids,3),key=lambda p:abs(np.linalg.det(Q[list(p)])))
  return np.linalg.solve(Q[list(tri)],np.ones(3))
 shift=np.array([0.,0.,1.])-point(s.G['groups'][0]);Q=Q/(1+Q@shift)[:,None]
 X=np.array([point(g) for g in s.G['groups']]);Y=np.vstack((Q,X));s.base=np.array([Y[i,a] for i,a in s.free]);s.last=None
 YY,DY=contact(s.G,s.base,s.free);s.scale=1/np.maximum(1.,np.linalg.norm(DY[:137].reshape(-1,s.n),axis=0));s.tscale=np.ones(len(s.tris));s.last=None
 v,J,g=s.evaluate(np.zeros(s.n));s.tscale=np.maximum(abs(g['v6']),1e-10);s.last=None
 return Y

