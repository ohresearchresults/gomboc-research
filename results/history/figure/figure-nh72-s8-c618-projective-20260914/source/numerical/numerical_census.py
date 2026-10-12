"""Complete floating screen of a finite transform, not an exact acceptance audit."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import numpy as np
from centroid_metric import CentroidOrbit

def census(m,t,A):
 t=np.array(t);A=np.array(A);y,g,K,d,V=m.state(t);P=(y-g)@A.T;N=(m.q+t)@np.linalg.inv(A);off=1-(m.q+t)@g;Y=N/off[:,None]
 Ns=N/np.linalg.norm(N,axis=1)[:,None]
 sides=[];graphs=[];roots=[];rad=[];minabs=[]
 for X,(src,dst),n in zip((P,Y),m.edges,m.ns):
  e=X[dst]-X[src];v=np.einsum('ni,ni->n',X[src],e)/(np.linalg.norm(X[src],axis=1)*np.linalg.norm(e,axis=1))
  top=np.full(n,-np.inf);np.maximum.at(top,src,v);root=np.where(top<0)[0].tolist();roots.append(root);rad.append(np.sum(X*X,axis=1))
  graph=[[] for _ in range(n)]
  for a,b,x in zip(src,dst,v):
   if x>0:graph[a].append(b)
  graphs.append(graph);minabs.append(float(np.min(abs(v))))
 def reaches(graph,start):
  seen=set();q=[start]
  while q:
   v=q.pop()
   if v not in seen:seen.add(v);q.extend(graph[v])
  return seen
 H=[];barriers=[]
 for (i,j),(f,h) in zip(m.ep,m.ed):
  e=P[j]-P[i];u=-P[i]@e/(e@e);foot=P[i]+u*e;n,nn=Ns[[f,h]];k=np.cross(n,nn);kk=k@k
  vals=[u,1-u,np.cross(foot,nn)@k/kk,np.cross(n,foot)@k/kk]
  if min(vals)>0:
   rr=foot@foot;pu=sorted((reaches(graphs[0],int(i))|reaches(graphs[0],int(j)))&set(roots[0]));ps=sorted((reaches(graphs[1],int(f))|reaches(graphs[1],int(h)))&set(roots[1]))
   H.append([int(i),int(j)]);barriers.append(dict(edge=[int(i),int(j)],facets=[int(f),int(h)],saddle_radius2=float(rr),primal={str(k):float(1-rr/rad[0][k]) for k in pu},polar={str(k):float(1-1/(rr*rad[1][k])) for k in ps}))
 good=[];bad=[]
 for graph,rr in zip(graphs,rad):
  root=int(np.argmax(rr));reach=[i for i in range(len(graph)) if root in reaches(graph,i)];good.append(reach);bad.append(sorted(set(range(len(graph)))-set(reach)))
 return dict(counts=[len(roots[1]),len(roots[0]),len(H)],S=roots[1],U=roots[0],H=H,basin_sizes=[len(v) for v in bad],basins=bad,barriers=barriers,directed_minabs=minabs,volume=float(V*np.linalg.det(A)),centroid=(A@g).tolist(),min_den=float(d.min()),condition=float(np.linalg.cond(A)))
