"""Finite multivertex deletion with physical two-cap compensation (numerical search)."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import sys,json,math
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import root,least_squares
from compensate import Mesh,CAPS
sys.path.insert(0,str(Path(__file__).parent/'coord_source'))
from check_A import polygon,sub,cross,dot

def exact_topology(P):
 X=[tuple(map(Q,p)) for p in P];F=np.array([[float(v) for v in p] for p in X]);ch=ConvexHull(F);planes=set()
 for tri in ch.simplices:
  a,b,c=(X[k] for k in tri);n=cross(sub(b,a),sub(c,a));h=dot(n,a)
  if h<0:n=tuple(-v for v in n);h=-h
  assert h>0
  dd=math.lcm(*(v.denominator for v in (*n,h)));row=[int(v*dd) for v in (*n,h)];gg=math.gcd(*row);r=tuple(v//gg for v in row)
  assert all(dot(r[:3],p)<=r[3] for p in X)
  planes.add(r)
 faces=[]
 for r in sorted(planes):
  ids=[i for i,p in enumerate(X) if dot(r[:3],p)==r[3]];cy=polygon(X,ids,r[:3]);assert set(cy)==set(ids);faces.append(cy)
 return faces

class Cluster:
 def __init__(self,report,deleted,remove):
  self.d=json.loads(Path(report).read_text());self.keep=[i for i in range(self.d['V']) if i not in remove];self.index={i:j for j,i in enumerate(self.keep)};self.c=np.array([float(Q(x)) for x in self.d['raw_centroid']]);self.P=np.array([[float(Q(x)) for x in self.d['raw_vertices'][i]] for i in self.keep]);self.faces=exact_topology([self.d['raw_vertices'][i] for i in self.keep]);self.mesh=Mesh(self.P,self.faces);self.caps=[]
  for ids,sep in CAPS[deleted]:
   assert not (set(ids)|set(sep))&set(remove)
   ids=[self.index[i] for i in ids];sep=[self.index[i] for i in sep]
   B=np.c_[self.P[sep],np.ones(4)].T;beta=np.c_[self.P[ids],np.ones(len(ids))]@np.linalg.inv(B).T
   self.caps.append((ids,sep,beta))
 def points(self,z):
  P=self.P.copy();dens=[]
  for ci,(ids,sep,beta) in enumerate(self.caps):
   eta=np.r_[z[ci*3:(ci+1)*3],0];d=1+beta@eta;dens.extend(d);P[ids]=(P[ids]+(beta*eta)@self.P[sep])/d[:,None]
  return P,np.array(dens)
 def close(self):
  def fun(z):
   full=np.array([0,0,z[0],z[1],z[2],0]);P,d=self.points(full);v,M,c=self.mesh.mass(P);return c-self.c
  sol=root(fun,[0,0,0],tol=1e-11);z=np.array([0,0,sol.x[0],sol.x[1],sol.x[2],0]);P,d=self.points(z);r=self.mesh.brief(self.mesh.state(P));r.update(eta=z.tolist(),min_den=float(d.min()),com_error=float(np.linalg.norm(fun(sol.x))),source_keep=self.keep,faces=self.faces)
  for k in ('U',):r['original_'+k]=[self.keep[i] for i in r[k]]
  r['original_H']=[[self.keep[i] for i in e] for e in r['H']]
  return r
if __name__=='__main__':
 report,j,remove_text,output=sys.argv[1:];remove=remove_text.split(',');m=Cluster(report,int(j),list(map(int,remove)));r=m.close();P,_=m.points(np.zeros(6));ref=m.mesh.state(P,m.c)
 print('remove',remove,'VEF',len(P),len(m.mesh.ep),len(m.faces),'ref',ref['counts'],[m.keep[i] for i in ref['U']]);print(json.dumps({k:v for k,v in r.items() if k not in ('faces','source_keep')},sort_keys=True));Path(output).write_text(json.dumps(r,sort_keys=True))
