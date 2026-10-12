"""PAIR99 enlarged external fan: 20 physical coordinates, optional 5 metric.
The frozen interface of the parent is not preserved: 103,107,111,150,151,152 move.
All remaining points are unchanged; both compensating caps remain identity.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np
from external_model import External
class Fan(External):
 def __init__(self,path):
  super().__init__(path)
  self.u0=np.r_[self.u0[:12],*[self.P[self.ix[i],[0,2]] for i in [103,107,111]],self.P[self.ix[114],0],self.P[self.ix[150],0]]
  self.fa.update({103:[0,2],107:[0,2],111:[0,2],114:[0],150:[0]})
  self.ax.update({103:[1],107:[1],111:[1],114:[1,2],150:[1,2]})
  self.n=20
 def points(self,z):
  z=np.asarray(z);dtype=np.result_type(z,float);P=self.P.astype(dtype);q=self.q.astype(dtype);u=self.u0+.01*z[:20]
  q[72]=u[:3];q[73,self.free73]=u[3:5]
  x=P[self.ix[69]];q[73,self.j73]=(1-q[73,self.free73]@x[self.free73])/x[self.j73]
  for i,nn in [(106,[15,71,72]),(109,[15,72,75]),(117,[71,72,73]),(120,[3,72,73])]:P[self.ix[i]]=np.linalg.solve(q[nn],np.ones(3))
  k=5
  for i,nn in [(124,[3,72]),(112,[75]),(146,[80]),(148,[69,80]),(149,[3,69]),(103,[71]),(107,[71]),(111,[71]),(114,[71,73]),(150,[3,69])]:
   free=self.fa[i];ax=self.ax[i];p=P[self.ix[i]];p[free]=u[k:k+len(free)];k+=len(free);p[ax]=np.linalg.solve(q[np.ix_(nn,ax)],np.ones(len(nn))-q[np.ix_(nn,free)]@p[free])
  assert k==20
  q[70]=np.linalg.solve(P[[self.ix[i] for i in [126,128,150]]],np.ones(3))
  for i,nn in [(151,[3,70,101]),(152,[43,70,101])]:P[self.ix[i]]=np.linalg.solve(q[nn],np.ones(3))
  if len(z)>20:
   a,b,c,d,e=z[20:];A=np.array([[np.exp(a),c,d],[0,np.exp(b),e],[0,0,np.exp(-a-b)]]);P=P@A.T
  return P,np.ones(1)
