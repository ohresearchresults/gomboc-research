"""Exact endpoint exposure and rank-architecture certificate, independently of search tolerances."""
from fractions import Fraction as Q
from math import lcm
import sys
sys.set_int_max_str_digits(0)
from RECONSTRUCT import solve

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def run(g,a):
 n=g['n_supports'];D=g['grid'];X=[[Q(v,D) for v in row] for row in g['controls']];X[n]=[Q(0),Q(0),Q(1)];done={n};free=0;depth={n:0};minors=[]
 for node,adj,axes in g['plan']:
  assert node not in done and set(adj)<=done;free+=3-len(adj);depth[node]=1+max([depth[v] for v in adj],default=-1)
  if adj:
   lhs=[[X[j][k] for k in axes] for j in adj];rhs=[1-sum(X[j][k]*X[node][k] for k in range(3) if k not in axes) for j in adj];vals=solve(lhs,rhs)
   for k,v in zip(axes,vals):X[node][k]=v
  assert all(dot(X[j],X[node])==1 for j in adj);done.add(node)
 assert len(done)==len(X)
 V=[tuple(map(Q,x)) for x in a['raw_vertices']];lookup={p:i for i,p in enumerate(V)};assert len(lookup)==len(V);P=X[n:];active=a['active_input_indices'];assert active==list(range(n));byvertex=[set() for _ in V];degrees=[0]*len(V)
 for i,cy in zip(active,a['faces']):
  for v in cy:byvertex[v].add(i)
 for i,j in a['edges']:degrees[i]+=1;degrees[j]+=1
 report=[];least=None
 for j,p in enumerate(P):
  v=lookup[tuple(p)];actual=byvertex[v];assert actual==set(g['groups'][j]);assert degrees[v]==len(actual)
  for i,q in enumerate(X[:n]):
   t=1-dot(q,p)
   if i in actual:assert t==0
   else:
    assert t>0
    if least is None or t<least[0]:least=(t,j,i)
  report.append(dict(node=j,vertex=v,input_supports=sorted(actual),degree=degrees[v],raw_coordinate=list(map(str,p))))
 nonsimple={i for i,d in enumerate(degrees) if d>3};assert nonsimple=={r['vertex'] for r in report};assert free==a['E']+3
 centre=list(map(Q,a['raw_centroid']));C=lcm(*(v.denominator for v in centre));M=[int(v*C) for v in centre];bs=[lcm(*(v.denominator for v in p)) for p in V];aa=[[int(v*b) for v in p] for p,b in zip(V,bs)];zero=0;adjzero=0;es=set(map(tuple,a['edges']))
 for i,p in enumerate(aa):
  z=[C*p[k]-bs[i]*M[k] for k in range(3)]
  for j,t in enumerate(aa):
   if i==j:continue
   e=[bs[i]*t[k]-bs[j]*p[k] for k in range(3)];sg=dot(z,e)
   if sg==0:zero+=1;adjzero+=tuple(sorted((i,j))) in es
 return dict(tag='ALL_DESIGNATED_CONTACTS_EXPOSED_EXACT',n_supports=n,n_contact_nodes=len(P),free_parameters=free,maximum_reconstruction_depth=max(depth.values()),degree_excess=sum(d-3 for d in degrees),contacts=report,minimum_nonincident_gap=str(least[0]),minimum_gap_contact_node=least[1],minimum_gap_support=least[2],ordered_vertex_pair_zero_count=zero,ordered_adjacent_vertex_zero_count=adjzero)
