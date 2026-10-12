"""Continuous shortest escape-path deficit represented by a weighted forest.

Edge cost is exactly max(floor-W_ij,0), without an added hop penalty.
The sum of shortest root-path costs is a minimum of finitely many continuous
path costs. A shortest-path forest represents that sum by weighting each edge
by the number of descendant starting points. Each edge deficit remains an LP
hinge; a selected path's newly negative edge is therefore constrained too.
"""
import numpy as np
from geometry import arrows

def shortest_forest(A,roots,floor=2e-9):
    W=arrows(A);n=len(A);cost=np.maximum(floor-W,0);dist=np.full(n,np.inf);dist[roots]=0;done=np.zeros(n,bool);parent=np.full(n,-1,int);order=[]
    for _ in range(n):
        j=int(np.argmin(np.where(done,np.inf,dist)))
        if not np.isfinite(dist[j]):raise ValueError('No finite root path in full physical escape graph')
        done[j]=True;order.append(j);trial=dist[j]+cost[:,j];take=(trial<dist)&(~done);dist[take]=trial[take];parent[take]=j
    weights=np.ones(n);rootset=set(map(int,roots))
    for i in reversed(order):
        if i not in rootset:weights[parent[i]]+=weights[i]
    for r in roots:parent[r]=int(np.argmax(W[r]));weights[r]=1
    signs=np.ones(n);signs[roots]=-1
    nonroot=np.array([i for i in range(n) if i not in rootset],int)
    edge_deficit=float(np.sum(weights[nonroot]*np.maximum(floor-W[nonroot,parent[nonroot]],0)))
    path_deficit=float(np.sum(dist[nonroot]))
    if abs(edge_deficit-path_deficit)>1e-9*max(1.,abs(path_deficit)):raise ValueError('Shortest path/weighted forest identity failed')
    return parent,weights,signs,dict(path_deficit=path_deficit,weighted_edge_deficit=edge_deficit)
