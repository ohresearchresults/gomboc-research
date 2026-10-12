"""PAIR99: six physical critical-disk coordinates plus six local cap controls.
All moments use the actual closed oriented boundary. Numerical discovery only.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import sys,json,heapq
from pathlib import Path
from fractions import Fraction as Q
import numpy as np

import BUILD
from compensate import Mesh
class Patch:
 def __init__(self,path):
  self.base=json.loads(Path(path).read_text());X,keep,faces,labels,beta=BUILD.setup(self.base,'PAIR99')
  self.keep=keep;self.ix={i:j for j,i in enumerate(keep)};self.labels=labels
  self.P=np.array([[float(v) for v in X[i]] for i in keep]);self.c=np.array([float(Q(v)) for v in self.base['raw_centroid']]);self.faces=[[self.ix[i] for i in c] for c in faces];self.mesh=Mesh(self.P,self.faces)
  self.dir=np.zeros((len(keep),3,6));self.moves=[(124,120),(149,150),(112,118),(112,109),(146,118),(146,148)]
  for k,(i,j) in enumerate(self.moves): self.dir[self.ix[i],:,k]=np.array([float(y-x) for x,y in zip(X[i],X[j])])
  self.caps=[]
  for ci,spec in enumerate(BUILD.CASES['PAIR99']['caps']):
   ii=[self.ix[i] for i in spec['vertices']];bd=[self.ix[i] for i in spec['boundary']];B=np.array([[float(v) for v in beta[ci,i][:3]] for i in spec['vertices']]);self.caps.append((ii,bd,B))
  self.tri=self.mesh.tri;self.ft=self.mesh.ft;self.ep=self.mesh.ep;self.ed=self.mesh.ed
  self.src,self.dst=self.mesh.src,self.mesh.dst;self.fs,self.fd=self.mesh.fs,self.mesh.fd
  self.rU=self.ix[95];self.rS=labels.index(3)
  self.triv=np.einsum('ij,ij->i',self.P[self.tri[:,0]],np.cross(self.P[self.tri[:,1]],self.P[self.tri[:,2]]))/6
 def points(self,z):
  z=np.asarray(z);P=self.P.astype(np.result_type(z,float))+np.einsum('ijk,k->ij',self.dir,z[:6]);dens=[]
  for ci,(ii,bd,B) in enumerate(self.caps):
   eta=z[6+3*ci:9+3*ci];den=1+B@eta;dens.extend(den)
   P[ii]=(self.P[ii]+(B*eta)@self.P[bd[:3]])/den[:,None]
  if len(z)>12:
   a,b,c,d,e=z[12:];A=np.array([[np.exp(a),c,d],[0,np.exp(b),e],[0,0,np.exp(-a-b)]]);P=P@A.T
  return P,np.array(dens)
 def calc(self,z,reference=False):
  P,den=self.points(z);T=P[self.tri];vol=np.einsum('ij,ij->i',T[:,0],np.cross(T[:,1],T[:,2]))/6;V=vol.sum();M=np.einsum('i,ij->j',vol,T.sum(axis=1))/4;g=M/V
  X=P-(self.c if reference else g);ft=X[self.ft];n=np.cross(ft[:,1]-ft[:,0],ft[:,2]-ft[:,0]);h=np.einsum('ij,ij->i',n,ft[:,0]);Y=n/h[:,None]
  def norms(x):return np.sqrt((x*x).sum(axis=1))
  e=X[self.dst]-X[self.src];pv=np.einsum('ij,ij->i',X[self.src],e)/(norms(X[self.src])*norms(e))
  ee=Y[self.fd]-Y[self.fs];dv=np.einsum('ij,ij->i',Y[self.fs],ee)/(norms(Y[self.fs])*norms(ee))
  gap=(h[:,None]-n@X.T)/norms(n)[:,None]
  return pv,dv,g,gap,den,vol
 def brief(self,z):
  P,den=self.points(z);s=self.mesh.brief(self.mesh.state(P));s.update(z=np.array(z).tolist(),Uold=[self.keep[i] for i in s['U']],Sold=[self.labels[i] for i in s['S']],Hold=[[self.keep[i] for i in e] for e in s['H']],min_den=float(den.min()));return s

def forest(n,src,dst,val,root):
 rev=[[] for _ in range(n)]
 for e,(i,j) in enumerate(zip(src,dst)):rev[j].append((int(i),e))
 cap=np.full(n,-np.inf);cap[root]=np.inf;par=np.full(n,-1,int);done=set();pq=[(-np.inf,root)]
 while pq:
  neg,j=heapq.heappop(pq)
  if j in done:continue
  done.add(j)
  for i,e in rev[j]:
   if i in done:continue
   v=min(cap[j],val[e])
   if v>cap[i]:cap[i]=v;par[i]=e;heapq.heappush(pq,(-v,i))
 assert len(done)==n
 return par[np.arange(n)!=root]

