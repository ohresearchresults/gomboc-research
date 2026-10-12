"""Minimum summed path-cost witnesses; fixed-forest derivatives need multiplicity.
For c_ij=max(epsilon-angular_escape_ij,0), Dijkstra gives each point's
minimum cost to an allowed root. Reverse settlement accumulates the number of
source paths using each selected arc. Their weighted arc cost equals sum distances.
"""
import numpy as np
from geometry import angular_scores

def forest(A,mask,roots,epsilon,metric="angular"):
 if metric=="relative_chord":
  q=(A@A.T)/np.sum(A*A,axis=1)[:,None]-1;np.fill_diagonal(q,-np.inf)
 elif metric=="angular":q=angular_scores(A)
 else:raise ValueError("unknown explicit path metric")
 q[:,mask==0]=-np.inf;c=np.maximum(epsilon-q,0);dist=np.full(len(A),np.inf);dist[roots]=0;used=mask==0;pa=np.full(len(A),roots[0],int);order=[]
 for _ in range(int(mask.sum())):
  j=int(np.argmin(np.where(~used,dist,np.inf)));used[j]=True;order.append(j);candidate=dist[j]+c[:,j];take=(~used)&(candidate<dist);dist[take]=candidate[take];pa[take]=j
 weights=mask.copy();rs=set(roots)
 for j in reversed(order):
  if j not in rs:weights[pa[j]]+=weights[j]
 for j in roots:pa[j]=int(q[j].argmax());weights[j]=1
 sg=mask.copy();sg[roots]=-1
 total=float(np.sum(dist[mask>0]));arc=float(np.sum(weights[[i for i in order if i not in rs]]*c[[i for i in order if i not in rs],pa[[i for i in order if i not in rs]]]))
 assert abs(total-arc)<1e-7*max(1,total),(total,arc)
 return pa,sg,weights
