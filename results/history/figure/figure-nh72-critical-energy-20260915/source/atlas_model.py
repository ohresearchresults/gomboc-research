"""A 12-coordinate physical critical patch and two independent local caps.
Facet labels refer to S8 after deletion99. All non-triangular facet contacts are
satisfied by construction, not by a numerical planarity penalty.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import sys,json
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
from patch_model import Patch
class Atlas(Patch):
 def __init__(self,path):
  super().__init__(path)
  self.q=np.array([[float(Q(v,h)) for v in n] for n,h in zip(self.base['normals'],self.base['offsets'])]);self.q=np.insert(self.q,99,np.nan,axis=0)
  P=lambda i:self.P[self.ix[i]]
  self.j73=int(np.argmax(abs(P(69))));self.free73=[k for k in range(3) if k!=self.j73]
  self.fa={};self.ax={}
  for i,nn in [(124,[3,72]),(112,[75]),(146,[80]),(148,[69,80]),(149,[3,69])]:
   if len(nn)==2:
    f=int(np.argmax(abs(np.cross(*self.q[nn]))));self.fa[i]=[f];self.ax[i]=[k for k in range(3) if k!=f]
   else:
    a=int(np.argmax(abs(self.q[nn[0]])));self.ax[i]=[a];self.fa[i]=[k for k in range(3) if k!=a]
  self.u0=np.r_[self.q[72],self.q[73,self.free73],*[P(i)[self.fa[i]] for i in [124,112,146,148,149]]]
  assert len(self.u0)==12
  self.n=18
 def points(self,z):
  z=np.asarray(z);dtype=np.result_type(z,float);P=self.P.astype(dtype);q=self.q.astype(dtype);u=self.u0+.01*z[:12]
  q[72]=u[:3];q[73,self.free73]=u[3:5]
  x=P[self.ix[69]];q[73,self.j73]=(1-q[73,self.free73]@x[self.free73])/x[self.j73]
  for i,nn in [(106,[15,71,72]),(109,[15,72,75]),(114,[17,71,73]),(117,[71,72,73]),(120,[3,72,73])]:P[self.ix[i]]=np.linalg.solve(q[nn],np.ones(3))
  k=5
  for i,nn in [(124,[3,72]),(112,[75]),(146,[80]),(148,[69,80]),(149,[3,69])]:
   free=self.fa[i];axes=self.ax[i];p=P[self.ix[i]];p[free]=u[k:k+len(free)];k+=len(free);p[axes]=np.linalg.solve(q[np.ix_(nn,axes)],np.ones(len(nn))-q[np.ix_(nn,free)]@p[free])
  assert k==12
  dens=[]
  for ci,(ii,bd,B) in enumerate(self.caps):
   eta=z[12+3*ci:15+3*ci];den=1+B@eta;dens.extend(den);P[ii]=(self.P[ii]+(B*eta)@self.P[bd[:3]])/den[:,None]
  if len(z)>18:
   a,b,c,d,e=z[18:];A=np.array([[np.exp(a),c,d],[0,np.exp(b),e],[0,0,np.exp(-a-b)]]);P=P@A.T
  return P,np.array(dens)
