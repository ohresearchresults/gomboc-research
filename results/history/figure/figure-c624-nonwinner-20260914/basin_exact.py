"""Exact actual-edge ascent basin at the body's own filled-volume centroid."""
import json,sys,math
from fractions import Fraction as F
from collections import deque
from pathlib import Path
sys.set_int_max_str_digits(0)
a=json.loads(Path(sys.argv[1]).read_text());p=[list(map(F,row)) for row in a['raw_vertices']];g=list(map(F,a['raw_centroid']));D=math.lcm(*(v.denominator for x in p for v in x),*(v.denominator for v in g));X=[[int(v*D)-int(g[k]*D) for k,v in enumerate(x)] for x in p]
def dot(x,y):return sum(v*w for v,w in zip(x,y))
E=a['edges'];graph=[[] for _ in X];reverse=[[] for _ in X]
for i,j in E:
 e=[y-x for x,y in zip(X[i],X[j])]
 if dot(X[i],e)>0:graph[i].append(j);reverse[j].append(i)
 if dot(X[j],e)<0:graph[j].append(i);reverse[i].append(j)
root=max(range(len(X)),key=lambda i:dot(X[i],X[i]));seen={root};q=deque([root])
while q:
 v=q.popleft()
 for u in reverse[v]:
  if u not in seen:seen.add(u);q.append(u)
bad=sorted(set(range(len(X)))-seen);boundary=[e for e in E if (e[0] in seen)!=(e[1] in seen)]
# Radial edge path from new saddle neighbour to the apex, deterministic BFS.
q=deque([166]);previous={166:None}
while q:
 v=q.popleft()
 if v==root:break
 for u in sorted(graph[v]):
  if u not in previous:previous[u]=v;q.append(u)
path=[];v=root
if v in previous:
 while v is not None:path.append(v);v=previous[v]
 path=path[::-1]
r=dict(root=root,actual_edge_root_reaching=len(seen),closed_unwanted=bad,boundary_edges=boundary,remaining_unstable=a['unstable_vertices'],exit_path_166_to_root=path)
print(json.dumps(r,sort_keys=True,separators=(',',':')))
