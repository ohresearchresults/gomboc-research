"""15-coordinate external-interface-changing PAIR99 chart; numerical only.
Canonical exact construction is supplied separately. All moments are filled volume.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import sys,json
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
from atlas_model import Atlas
class External(Atlas):
 def __init__(self,path):
  super().__init__(path)
  self.fa.update({111:[0],114:[0],150:[0]})
  self.ax.update({111:[1,2],114:[1,2],150:[1,2]})
  self.u0=np.r_[self.u0,*[self.P[self.ix[i],0] for i in [111,114,150]]]
  self.n=21
 def points(self,z):
  z=np.asarray(z);dtype=np.result_type(z,float);P=self.P.astype(dtype);q=self.q.astype(dtype);u=self.u0+.01*z[:15]
  q[72]=u[:3];q[73,self.free73]=u[3:5]
  x=P[self.ix[69]];q[73,self.j73]=(1-q[73,self.free73]@x[self.free73])/x[self.j73]
  for i,nn in [(106,[15,71,72]),(109,[15,72,75]),(117,[71,72,73]),(120,[3,72,73])]:P[self.ix[i]]=np.linalg.solve(q[nn],np.ones(3))
  k=5
  for i,nn in [(124,[3,72]),(112,[75]),(146,[80]),(148,[69,80]),(149,[3,69]),(111,[71,136]),(114,[71,73]),(150,[3,69])]:
   free=self.fa[i];ax=self.ax[i];p=P[self.ix[i]];p[free]=u[k:k+len(free)];k+=len(free);p[ax]=np.linalg.solve(q[np.ix_(nn,ax)],np.ones(len(nn))-q[np.ix_(nn,free)]@p[free])
  assert k==15
  q[70]=np.linalg.solve(P[[self.ix[i] for i in [126,128,150]]],np.ones(3))
  for i,nn in [(151,[3,70,101]),(152,[43,70,101])]:P[self.ix[i]]=np.linalg.solve(q[nn],np.ones(3))
  dens=[]
  for ci,(ii,bd,B) in enumerate(self.caps):
   eta=z[15+3*ci:18+3*ci] if len(z)>=21 else np.zeros(3);den=1+B@eta;dens.extend(den);P[ii]=(self.P[ii]+(B*eta)@self.P[bd[:3]])/den[:,None]
  if len(z)>21:
   a,b,c,d,e=z[21:];AA=np.array([[np.exp(a),c,d],[0,np.exp(b),e],[0,0,np.exp(-a-b)]]);P=P@AA.T
  return P,np.array(dens)
