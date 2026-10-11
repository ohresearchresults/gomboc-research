"""Root-connected cut expansion: share every already-positive upstream path before
paying for a new negative bridge. A finite heuristic, not a minimum-cost theorem."""
import numpy as np
from forest_implicit import Forest,run
import forest_implicit as engine

def forest(edges,values,root,N):
 incoming=[[] for _ in range(N)]
 for k,(i,j) in enumerate(edges):incoming[j].append((int(i),k))
 seen={root};out={}
 while len(seen)<N:
  change=True
  while change:
   change=False
   for j in sorted(seen):
    for i,k in incoming[j]:
     if i not in seen and values[k]>1e-9:
      seen.add(i);out[i]=k;change=True
  if len(seen)==N:break
  eligible=[(float(values[k]),-k,int(i),k) for k,(i,j) in enumerate(edges) if i not in seen and j in seen]
  assert eligible
  _,_,i,k=max(eligible);seen.add(i);out[i]=k
 assert len(out)==N-1
 for i in out:
  v=i;used=set()
  while v!=root:
   assert v not in used;used.add(v);v=int(edges[out[v],1])
 return np.array([out[i] for i in range(N) if i!=root])
engine.forest=forest
if __name__=='__main__':
 import argparse
 p=argparse.ArgumentParser();p.add_argument('--tag',default='CUT1');p.add_argument('--start',required=True);p.add_argument('--steps',type=int,default=40);p.add_argument('--mu',type=float,default=1e-11);p.add_argument('--lam',type=float,default=.0001);a=p.parse_args();run(a.tag,a.start,a.steps,a.mu,a.lam)
