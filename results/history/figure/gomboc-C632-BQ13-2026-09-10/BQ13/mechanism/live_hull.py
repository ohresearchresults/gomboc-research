"""Floating exposed-complex reconstruction: discovery, never exact acceptance."""
import numpy as np,itertools
from scipy.spatial import ConvexHull,cKDTree

def rebuild(q,eps=1e-8):
 q=np.asarray(q);h=ConvexHull(q);active=np.array(sorted(h.vertices));qa=q[active];old2new={v:i for i,v in enumerate(active)}
 assert np.max(h.equations[:,3])<-1e-8,'origin not interior'
 P=-h.equations[:,:3]/h.equations[:,3,None];uf=list(range(len(P)))
 def find(i):
  while uf[i]!=i:uf[i]=uf[uf[i]];i=uf[i]
  return i
 for i,j in cKDTree(P).query_pairs(eps):uf[find(i)]=find(j)
 groups={}
 for i,t in enumerate(h.simplices):groups.setdefault(find(i),set()).update(map(int,t))
 owners=sorted([sorted(g) for g in groups.values()]);p=[]
 for o in owners:
  cs=np.array(list(itertools.combinations(o,3)),dtype=int)
  t=cs[np.argmax(np.abs(np.linalg.det(q[cs])))]
  p.append(np.linalg.solve(q[list(t)],np.ones(3)))
 p=np.array(p);faces=[]
 for i in active:
  ids=np.array([j for j,g in enumerate(owners) if i in g]);assert len(ids)>=3
  n=q[i]/np.linalg.norm(q[i]);e=np.cross(n,np.eye(3)[np.argmin(abs(n))]);e/=np.linalg.norm(e);f=np.cross(n,e);d=p[ids]-np.mean(p[ids],axis=0);order=np.argsort(np.arctan2(d@f,d@e));faces.append(ids[order].tolist())
 return qa,p,faces,active,owners

def census(q,P,faces,centre):
 from numeric import topology
 x=P-centre;h=1-q@centre;nn=q/h[:,None]
 def ex(z):
  vals=z@z.T-np.einsum('ic,ic->i',z,z)[:,None];np.fill_diagonal(vals,-np.inf);return vals.max(1)
 se=ex(nn);ue=ex(x);S=np.flatnonzero(se<0);U=np.flatnonzero(ue<0)
 own,edges=topology(faces);H=[];weak=[]
 for (i,j),(fi,fj) in edges.items():
  d=x[j]-x[i];ell=d@d;t=-x[i]@d;Q=ell*x[i]+t*d;n,m=nn[[fi,fj]];A=n@n;B=n@m;C=m@m;vv=[t,ell-t,Q@(C*n-B*m),Q@(A*m-B*n)]
  if min(vv)>0:H.append([i,j])
  elif min(vv)>=0:weak.append([i,j])
 return dict(counts=[len(S),len(U),len(H)],S=S.tolist(),U=U.tolist(),H=H,weak=weak,se=se,ue=ue)
