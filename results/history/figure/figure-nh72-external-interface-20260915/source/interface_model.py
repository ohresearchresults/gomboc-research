"""S8 contact-preserving exterior motion coupled to PAIR99 critical surgery.
13 exterior control coordinates + 12 critical coordinates + optional metric5.
All labels in physical patch are after explicit removal of S8 support99.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import json
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import numpy as np
from patch_model import Patch
EDIT=[(i,k) for i in [154,177] for k in range(3)]+[(71,0)]+[(i,k) for i in [69,70] for k in range(3)]
class Interface(Patch):
 def __init__(self,base,generator):
  super().__init__(base);self.gen=json.loads(Path(generator).read_text());self.control=np.array(self.gen['controls'],float)/self.gen['grid'];self.plan=self.gen['plan']
  q=np.array([[float(Q(v,h)) for v in nn] for nn,h in zip(self.base['normals'],self.base['offsets'])]);q=np.insert(q,99,np.nan,axis=0)
  labels=[i for i in range(137) if i!=99];faces=self.base['faces'];self.triples=[]
  for i in range(175):
   owners=[labels[k] for k,c in enumerate(faces) if i in c]
   self.triples.append(max(combinations(owners,3),key=lambda c:abs(np.linalg.det(q[list(c)]))))
  self.triples=np.array(self.triples);self.n=25
  self.free73=[0,2];self.fa={124:[0],112:[0,1],146:[0,1],148:[1],149:[0]}
 def points(self,z):
  z=np.asarray(z);dtype=np.result_type(z,float);v=self.control.astype(dtype)
  for (i,k),d in zip(EDIT,z[:13]):v[i,k]+=.01*d
  v[137]=[0,0,1]
  for i,dep,axes in self.plan:
   if dep:
    rest=[k for k in range(3) if k not in axes];bb=np.ones(len(dep),dtype=dtype)-v[np.ix_(dep,rest)]@v[i,rest]
    v[i,axes]=np.linalg.solve(v[np.ix_(dep,axes)],bb)
  q=v[:137].copy();PP=np.linalg.solve(q[self.triples],np.ones((175,3,1),dtype=dtype)).squeeze(-1);P=PP[self.keep].copy()
  u0=np.r_[q[72],q[73,self.free73],*[PP[i,self.fa[i]] for i in [124,112,146,148,149]]];u=u0+.01*z[13:25]
  q[72]=u[:3];q[73,self.free73]=u[3:5];q[73,1]=(1-q[73,self.free73]@PP[69,self.free73])/PP[69,1]
  for i,nn in [(106,[15,71,72]),(109,[15,72,75]),(114,[17,71,73]),(117,[71,72,73]),(120,[3,72,73])]:P[self.ix[i]]=np.linalg.solve(q[nn],np.ones(3,dtype=dtype))
  k=5
  for i,nn in [(124,[3,72]),(112,[75]),(146,[80]),(148,[69,80]),(149,[3,69])]:
   free=self.fa[i];axes=[a for a in range(3) if a not in free];p=P[self.ix[i]];p[free]=u[k:k+len(free)];k+=len(free)
   p[axes]=np.linalg.solve(q[np.ix_(nn,axes)],np.ones(len(nn),dtype=dtype)-q[np.ix_(nn,free)]@p[free])
  if len(z)>25:
   a,b,c,d,e=z[25:];A=np.array([[np.exp(a),c,d],[0,np.exp(b),e],[0,0,np.exp(-a-b)]]);P=P@A.T
  return P,np.ones(1)
