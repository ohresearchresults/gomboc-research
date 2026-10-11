"""Deterministic exact primal/dual three/four-cycle separator inventory."""
import json,sys,itertools
from pathlib import Path

def components(adj,sep):
 un=set(range(len(adj)))-set(sep);out=[]
 while un:
  stack=[min(un)];un.remove(stack[0]);cc=[]
  while stack:
   v=stack.pop();cc.append(v);new=adj[v]&un;un-=new;stack.extend(sorted(new))
  out.append(sorted(cc))
 return sorted(out,key=lambda x:(len(x),x))

def run(data):
 ef={}
 for f,cy in enumerate(data['faces']):
  for a,b in zip(cy,cy[1:]+cy[:1]):ef.setdefault(tuple(sorted((a,b))),[]).append(f)
 result={}
 for side,n,edges in [('primal',data['V'],data['edges']),('dual',data['F'],list(ef.values()))]:
  adj=[set() for _ in range(n)]
  for a,b in edges:adj[a].add(b);adj[b].add(a)
  triangles=sorted({tuple(sorted((a,b,c))) for a in range(n) for b in adj[a] for c in adj[a]&adj[b]});fours=set()
  for a in range(n):
   for c in range(a+1,n):
    for b,d in itertools.combinations(adj[a]&adj[c],2):fours.add(tuple(sorted((a,b,c,d))))
  for k,candidates in [(3,triangles),(4,sorted(fours))]:
   arr=[]
   for sep in candidates:
    cc=components(adj,sep)
    if len(cc)>1:arr.append(dict(separator=list(sep),components=cc))
   result[side+str(k)]=dict(candidate_sets=len(candidates),separators=arr)
 return result
if __name__=='__main__':
 data=json.loads(Path(sys.argv[1]).read_text());Path(sys.argv[2]).write_text(json.dumps(run(data),sort_keys=True,separators=(',',':')))
