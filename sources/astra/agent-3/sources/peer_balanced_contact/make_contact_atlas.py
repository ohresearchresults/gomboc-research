"""Build the peer-shared full contact plan from this agent's exact audit schema.
Algorithm and deterministic peeling choices adapted from the complete pinned
peer2 contact_atlas.py source; only the input-schema bridge differs.
"""
import json,itertools,numpy as np
from pathlib import Path
from gmpy2 import mpq
def make(path,out,balanced=False,quality_first=False):
 r=json.loads(path.read_text());X=np.array([[float(mpq(v)) for v in row] for row in r["raw_vertices"]]);H=r["raw_halfspaces"];Y=np.array([[float(mpq(x)/mpq(row[3])) for x in row[:3]] for row in H])[r["active"]];tri=np.array([[cy[0],cy[k],cy[k+1]] for cy in r["faces"] for k in range(1,len(cy)-1)]);eu=np.array(r["edges"]);incid={tuple(e):[] for e in eu};
 for f,cy in enumerate(r["faces"]):
  for i,j in zip(cy,cy[1:]+cy[:1]):incid[tuple(sorted((i,j)))].append(f)
 es=np.array(list(incid.values()));F=len(Y);A=np.r_[Y,X];N=len(A);adj=[set() for _ in range(N)]
 for f,vs in enumerate(r['faces']):
  for v in vs:adj[f].add(F+v);adj[F+v].add(f)
 rem=set(range(N));peel=[];arrival={i:0 for i in rem if len(adj[i])<=3}
 while rem:
  poss=[i for i in rem if len(adj[i]&rem)<=3];assert poss,'not3degenerate'
  # Prefer a well-conditioned local minor among equal degree candidates.
  options=[]
  for i in poss:
   deps=sorted(adj[i]&rem);degree=len(deps);quality=1. if not deps else np.linalg.svd(A[deps],compute_uv=False)[-1]/max(np.linalg.norm(A[deps]),1e-30);options.append(((-quality if quality_first else (arrival[i] if balanced else 0)),-degree,-quality,i,deps))
  _,_,_,i,deps=min(options);peel.append((i,deps));rem.remove(i)
  for j in adj[i]&rem:
   if j not in arrival and len(adj[j]&rem)<=3:arrival[j]=arrival[i]+1
 plan=[];free=[];layers={};depth={}
 for i,deps in reversed(peel):
  d=len(deps)
  if d:
   axes=max(itertools.combinations(range(3),d),key=lambda a:abs(np.linalg.det(A[np.ix_(deps,a)])));quality=abs(np.linalg.det(A[np.ix_(deps,axes)]));assert quality>1e-14
  else:axes=()
  rest=[k for k in range(3) if k not in axes];indices=list(range(len(free),len(free)+len(rest)));free.extend((i,k) for k in rest);lev=0 if not deps else 1+max(depth[j] for j in deps);depth[i]=lev;layers.setdefault((lev,d),[]).append((i,deps,list(axes),rest,indices));plan.append(dict(node=i,deps=deps,axes=list(axes),free_axes=rest,free_indices=indices))
 levels=[]
 for key,group in sorted(layers.items()):
  level,degree=key;levels.append(dict(level=level,degree=degree,nodes=[g[0] for g in group],deps=[g[1] for g in group],axes=[g[2] for g in group],rest=[g[3] for g in group],indices=[g[4] for g in group]))
 incidence=np.zeros((F,len(X)),bool)
 for f,vs in enumerate(r['faces']):incidence[f,vs]=True
 meta=dict(source=str(path),V=len(X),F=F,E=r['E'],nodes=N,free_coordinates=len(free),max_depth=max(depth.values()),balanced_peeling=balanced,quality_first_peeling=quality_first,plan=plan,levels=levels,faces=r['faces'])
 out.mkdir(exist_ok=True,parents=True);(out/'chart.json').write_text(json.dumps(meta,indent=2)+'\n');q=np.array([A[i,k] for i,k in free]);np.savez(out/'data.npz',q=q,A=A,tri=tri,eu=eu,es=es,incidence=incidence);print('CONTACT_CHART',dict(V=len(X),F=F,E=r['E'],nodes=N,free=len(free),depth=max(depth.values()),levels=len(levels)),flush=True)
 return meta,q,A,tri,eu,es,incidence

if __name__=="__main__":
 import sys
 make(Path(sys.argv[1]),Path(sys.argv[2]),'--balanced' in sys.argv[3:],'--quality' in sys.argv[3:])
