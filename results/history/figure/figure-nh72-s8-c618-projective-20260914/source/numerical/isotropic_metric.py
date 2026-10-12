"""Global own-centroid chart with covariance-normalized physical metric.
Numerical discovery; all root/edge declarations require the separate exact auditors.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import numpy as np
from centroid_metric import CentroidOrbit

class IsotropicOrbit(CentroidOrbit):
 def geometry(self,z):
  t,y,g,K,d,V,err=self.invert(z[:3]);Tb=-np.linalg.inv(K)
  dy=-np.einsum('ni,nj->nij',y,y)@Tb
  p=y-g;dp=dy-np.eye(3)[None,:,:]
  n=self.q+t;hh=1-n@g
  if hh.min()<=0:raise ArithmeticError('Bad own polar interior')
  pole=n/hh[:,None];dh=-g@Tb-n
  dpol=Tb[None,:,:]/hh[:,None,None]-n[:,:,None]*dh[:,None,:]/hh[:,None,None]**2
  # Derivative of actual covariance in centroid coordinates, from physical tetrahedra.
  tr=y[self.tri];trj=dy[self.tri];w=self.w0/np.prod(d[self.tri],axis=1);W=w.sum();s=tr.sum(axis=1)
  Jw=-w[:,None]*(s@Tb);Js=trj.sum(axis=1)
  base=np.einsum('ni,nj->nij',s,s)+np.einsum('nai,naj->nij',tr,tr)
  second=np.einsum('n,nij->ij',w,base)/(20*W);cov=second-np.outer(g,g);DC=[]
  for k in range(3):
   term=np.einsum('ni,nj->nij',Js[:,:,k],s)+np.einsum('ni,nj->nij',s,Js[:,:,k])
   term+=np.einsum('nai,naj->nij',trj[:,:,:,k],tr)+np.einsum('nai,naj->nij',tr,trj[:,:,:,k])
   dS=(np.einsum('n,nij->ij',Jw[:,k],base)+np.einsum('n,nij->ij',w,term))/(20*W)-second*Jw[:,k].sum()/W
   DC.append(dS-np.outer(np.eye(3)[k],g)-np.outer(g,np.eye(3)[k]))
  L=np.linalg.cholesky(cov);Li=np.linalg.inv(L);scale=np.linalg.det(L)**(1/3);white=scale*Li;DW=[]
  for Ck in DC:
   Q=Li@Ck@Li.T;Phi=np.tril(Q);Phi[np.diag_indices(3)]*=.5
   DW.append(-Phi@white+np.trace(Q)/6*white)
  a,c=z[3:5];ex=np.exp([a,c,-a-c]);U=np.eye(3);U[0,1]=z[5];U[0,2]=z[6];U[1,2]=z[7]
  M=ex[:,None]*U;DM=np.zeros((5,3,3));DM[0]=np.diag([1,0,-1])@M;DM[1]=np.diag([0,1,-1])@M
  DM[2,0,1]=ex[0];DM[3,0,2]=ex[0];DM[4,1,2]=ex[1]
  A=M@white;B=np.linalg.inv(A).T;DA=np.concatenate(([M@v for v in DW],[v@white for v in DM]))
  DB=np.array([-B@q.T@B for q in DA])
  P=p@A.T;Y=pole@B.T
  JP=np.einsum('kij,nj->nik',DA,p);JP[:,:,:3]+=np.einsum('ij,njk->nik',A,dp)
  JY=np.einsum('kij,nj->nik',DB,pole);JY[:,:,:3]+=np.einsum('ij,njk->nik',B,dpol)
  info=dict(t=t.tolist(),A=A.tolist(),volume=V,centroid_projective=g.tolist(),centroid=(A@g).tolist(),centroid_error=float(err),min_den=float(d.min()),condition=float(np.linalg.cond(A)),relative_metric_condition=float(np.linalg.cond(M)))
  return P,Y,JP,JY,info

if __name__=='__main__':
 import sys
 from pathlib import Path
 import centroid_metric
 centroid_metric.CentroidOrbit=IsotropicOrbit
 centroid_metric.main()
