"""Independent integer audit from maximal face cycles, not display triangles.
Uses an interior barycentre tetrahedralization and Gram-system edge cones.
"""
from pathlib import Path
from collections import defaultdict, Counter
from itertools import combinations
from math import gcd
import json,gzip,csv,sys
sys.set_int_max_str_digits(0)

def d(a,b):return sum(a[i]*b[i] for i in range(3))
def minus(a,b):return tuple(a[i]-b[i] for i in range(3))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def determinant(a,b,c):return d(a,cross(b,c))
def primitive(v):
 g=gcd(*v);assert g>0;return tuple(x//g for x in v)
def rows(p):
 with gzip.open(p,'rt') as f:return [tuple(map(int,r)) for r in csv.reader(f)]
def run(folder):
 p=Path(folder);I=rows(p/'raw_vertices.csv.gz');R=json.loads((p/'exact_report.json').read_text());cycles=R['maximal_cycles'];D=int(R['raw_denominator']);N=len(I);s=tuple(sum(v[i] for v in I) for i in range(3));J=[tuple(N*v[i]-s[i] for i in range(3)) for v in I]
 edges=defaultdict(list);planes=[];W=0;M=[0]*3
 for f,cy in enumerate(cycles):
  assert len(cy)>=3 and len(set(cy))==len(cy)
  a,b,c=[I[i] for i in cy[:3]];n=primitive(cross(minus(b,a),minus(c,a)));h=d(n,a);assert n!=(0,0,0)
  vals=[h-d(n,v) for v in I];assert all(v>=0 for v in vals)
  assert {i for i,v in enumerate(vals) if v==0}==set(cy),'maximal facet'
  # Full polygon convexity, not merely three consecutive corners.
  for a,b in zip(cy,cy[1:]+cy[:1]):
   inward=cross(n,primitive(minus(I[b],I[a])))
   assert all(d(inward,primitive(minus(I[k],I[a])))>0 for k in cy if k not in(a,b))
  planes.append(n)
  for i,j in zip(cy,cy[1:]+cy[:1]):edges[tuple(sorted((i,j)))].append((f,i,j))
  # The interior reference is arithmetic vertex barycentre, NOT own COM.
  for k in range(1,len(cy)-1):
   a,b,c=[J[i] for i in [cy[0],cy[k],cy[k+1]]];v=determinant(a,b,c);assert v>0;W+=v
   for j in range(3):M[j]+=v*(a[j]+b[j]+c[j])
 # Independently build contact-set intersections and compare true edges.
 contact=[set(cy)for cy in cycles];edge_from_planes={}
 for f,g in combinations(range(len(cycles)),2):
  common=contact[f]&contact[g]
  if len(common)==2:
   e=tuple(sorted(common));assert e not in edge_from_planes
   edge_from_planes[e]=(f,g)
  else:assert len(common)<2
 assert set(edge_from_planes)==set(edges)
 for e,inc in edges.items():
  assert set(edge_from_planes[e])=={z[0]for z in inc}
 # Rank three at every actual vertex; connected degree-two links.
 adj=defaultdict(set)
 for a,b in edges:adj[a].add(b);adj[b].add(a)
 assert len(adj)==N
 connected=set();todo=[0]
 while todo:
  v=todo.pop()
  if v not in connected:connected.add(v);todo.extend(adj[v]-connected)
 assert len(connected)==N
 for v in range(N):
  ff=[f for f,cy in enumerate(cycles)if v in cy]
  assert any(determinant(planes[a],planes[b],planes[c])!=0 for a,b,c in combinations(ff,3))
  link=defaultdict(set)
  for f in ff:
   cy=cycles[f];k=cy.index(v);a,b=cy[k-1],cy[(k+1)%len(cy)];link[a].add(b);link[b].add(a)
  assert set(link)==adj[v] and all(len(x)==2 for x in link.values())
  seen=set();todo=[next(iter(link))]
  while todo:
   j=todo.pop()
   if j not in seen:seen.add(j);todo.extend(link[j]-seen)
  assert seen==set(link)
 assert W==int(R['W'])*N**3,'independent volume'
 assert all((M[j]+4*W*s[j])*4*int(R['W'])==int(R['M'][j])*4*W*N for j in range(3)),'independent ordinary centroid'
 K=[tuple(4*W*v[i]-M[i] for i in range(3)) for v in J];A=4*W*N
 assert all(K[i][j]*int(R['centroid_multiplier'])==A*(int(R['centroid_multiplier'])*I[i][j]-int(R['centroid_subtract'][j])) for i in range(N) for j in range(3))
 # Positive scale reduction changes no exact feature predicate.
 kg=gcd(*(x for row in K for x in row));assert kg>0
 K=[tuple(x//kg for x in row) for row in K]
 S=[];U=[];H=[];deg=[];zero_primitives=0
 for f,cy in enumerate(cycles):
  n=planes[f];nn=d(n,n);h=d(n,K[cy[0]]);assert h>0
  # Foot numerator is h*n; denom n*n. Test all polygon edge inward normals.
  values=[]
  for i,j in zip(cy,cy[1:]+cy[:1]):
   inward=cross(n,primitive(minus(I[j],I[i])));foot_minus=tuple(h*n[a]-nn*K[i][a] for a in range(3));values.append(d(inward,foot_minus))
  if min(values)>0:S.append(cy)
  elif min(values)==0:deg.append(['face',cy])
 for i in range(N):
  # Global all-point condition, independent of any neighbor/witness choices.
  vals=[d(K[i],primitive(minus(I[j],I[i]))) for j in range(N) if i!=j]
  if max(vals)<0:U.append(i)
  elif max(vals)==0:deg.append(['vertex',i])
 for key,inc in edges.items():
  assert len(inc)==2;f,i,j=inc[0];g,jj,ii=inc[1];assert i==ii and j==jj
  a=K[i];v=primitive(minus(I[j],I[i]));L=d(v,v);t=-d(a,v);end=d(K[j],v);n=planes[f];m=planes[g];nn=d(n,n);mm=d(m,m);nm=d(n,m);gram=nn*mm-nm*nm;assert gram>0
  z=tuple(L*a[q]+t*v[q] for q in range(3));alpha=d(z,n)*mm-d(z,m)*nm;beta=d(z,m)*nn-d(z,n)*nm
  vals=(t,end,alpha,beta);zero_primitives+=sum(z==0 for z in vals)
  if min(vals)>0:H.append(list(key))
  elif min(vals)==0:deg.append(['edge',list(key)])
 assert N-len(edges)+len(cycles)==2
 assert len(S)+len(U)-len(H)==2 or deg
 result=dict(V=N,E=len(edges),F=len(cycles),class_SUH=[len(S),len(U),len(H)],stable=S,unstable=U,saddles=H,degeneracies=deg,zero_edge_primitives=zero_primitives,complete_contact_sets=True,global_polygon_convexity=True,edge_contact_intersections=True,rank_three_vertices=True,connected_cyclic_links=True,facet_sizes=dict(Counter(map(len,cycles))))
 assert result['class_SUH']==R['class_SUH'];assert set(map(frozenset,S))==set(map(frozenset,R['stable']));assert U==R['unstable'];assert set(map(frozenset,H))==set(map(frozenset,R['saddles']));assert not deg
 (p/'independent_report.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2));return result
if __name__=='__main__':run(sys.argv[1])
