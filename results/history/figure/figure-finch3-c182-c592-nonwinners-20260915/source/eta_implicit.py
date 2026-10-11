"""Dimensionless edge-projection fractions, including the centred polar.
For each true primal or dual edge i->j, eta=i.(j-i)/|j-i|^2;
eta(i,j)+eta(j,i)=-1 exactly. Small angles from a short edge are
therefore not mistaken for simultaneous endpoint cancellation."""
import implicit as engine
from implicit import Manifold
from model import dot,cross,divide,HERE
import numpy as np,argparse
class Eta(Manifold):
 def __init__(self,P,q,faces):
  super().__init__(P,q,faces);owners={tuple(e):[] for e in self.E.tolist()}
  for f,c in enumerate(self.F):
   for i,j in zip(c,c[1:]+c[:1]):owners[tuple(sorted((i,j)))].append(f)
  self.fe=np.array([(a,b) for fs in owners.values() for a,b in [fs,fs[::-1]]]);self.fi=[np.flatnonzero(self.fe[:,0]==f) for f in range(self.n)]
 def evaluate(self,z,T=None):
  if T is None:T=np.eye(self.K)
  R=super().evaluate(z,T);K=T.shape[1];P=R['P'];q=R['q'];DP=T[:3*self.V].reshape(self.V,3,K);DQ=T[3*self.V:].reshape(self.n,3,K);X=P[self.tris];DX=DP[self.tris];cr,dcr=cross(X[:,1],X[:,2],DX[:,1],DX[:,2]);dt,ddt=dot(X[:,0],cr,DX[:,0],dcr);D=dt.sum();dD=ddt.sum(axis=0);B=np.einsum('n,ni->i',dt,X.sum(axis=1));dB=np.einsum('nk,ni->ik',ddt,X.sum(axis=1))+np.einsum('n,nik->ik',dt,DX.sum(axis=1));g=R['g'];dg=(dB-4*g[:,None]*dD)/(4*D);Z=P-g;DZ=DP-dg;i,j=self.ue.T;e=P[j]-P[i];de=DP[j]-DP[i];a,da=dot(Z[i],e,DZ[i],de);b,db=dot(e,e,de,de);R['u'],R['du']=divide(a,b,da,db)
  h=1-q@g;dh=-np.einsum('nik,i->nk',DQ,g)-q@dg;Q=q/h[:,None];dQ=(DQ-Q[:,:,None]*dh[:,None,:])/h[:,None,None];i,j=self.fe.T;e=Q[j]-Q[i];de=dQ[j]-dQ[i];a,da=dot(Q[i],e,dQ[i],de);b,db=dot(e,e,de,de);R['f'],R['df']=divide(a,b,da,db);return R
engine.Manifold=Eta
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--start',default='QUOT_11_1.json');p.add_argument('--tag',default='ETA1');p.add_argument('--steps',type=int,default=60);p.add_argument('--mu',type=float,default=1e-10);p.add_argument('--lam',type=float,default=.001);a=p.parse_args();engine.run(a.tag,a.start,a.steps,a.mu,a.lam)
