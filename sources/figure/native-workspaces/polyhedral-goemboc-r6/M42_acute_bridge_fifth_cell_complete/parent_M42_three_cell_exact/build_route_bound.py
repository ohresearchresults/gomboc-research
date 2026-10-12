#!/usr/bin/env python3
"""Build an exact fixed-direction acute-edge witness-route certificate."""
from fractions import Fraction as Q
from pathlib import Path
from decimal import Decimal, getcontext
import csv,json,sys,hashlib
sys.set_int_max_str_digits(1000000)
R=Path(__file__).resolve().parent

def dot(a,b):return sum(a[k]*b[k] for k in range(3))
def n2(a):return dot(a,a)
def qs(x):return f'{x.numerator}/{x.denominator}'
def bracket(x,n=12):
 d=10**n;k=(x.numerator*d)//x.denominator
 return [f'{k}/{d}',f'{k+1}/{d}']
def sqrt_bracket(x,n=12):
 getcontext().prec=100
 z=(Decimal(x.numerator)/Decimal(x.denominator)).sqrt();d=10**n;k=int(z*Decimal(d))
 lo=Q(k,d);hi=Q(k+1,d);assert lo*lo<=x<=hi*hi
 return [qs(lo),qs(hi)]
X={}
with open(R/'coordinates_active_centered.csv') as f:
 for r in csv.DictReader(f):X[int(r['source_id'])]=tuple(Q(r[k]) for k in ('x_exact','y_exact','z_exact'))
edges=[]
with open(R/'true_edges.csv') as f:
 for r in csv.DictReader(f):edges.append((int(r['u']),int(r['v'])))
adj={i:[] for i in X};acute=[]
for u,v in edges:
 d=dot(X[u],X[v])
 if d>0:
  w=n2(X[u])*n2(X[v])/(d*d)
  adj[u].append((v,w));adj[v].append((u,w));acute.append((u,v,w))
start,target=153,8
# Exact O(V^2) multiplicative Dijkstra. Every multiplier is >=1.
dist={start:Q(1)};prev={};unvisited=set(X)
settled=[]
while unvisited:
 avail=[i for i in unvisited if i in dist]
 if not avail:break
 u=min(avail,key=lambda i:dist[i]);unvisited.remove(u);settled.append(u)
 if u==target:break
 for v,w in adj[u]:
  if v not in unvisited:continue
  z=dist[u]*w
  if v not in dist or z<dist[v]:dist[v]=z;prev[v]=u
assert target in dist
path=[];u=target
while True:
 path.append(u)
 if u==start:break
 u=prev[u]
path.reverse()
prod=Q(1);per=[]
for u,v in zip(path,path[1:]):
 d=dot(X[u],X[v]);w=n2(X[u])*n2(X[v])/(d*d);prod*=w
 per.append({'edge':[u,v],'secant_squared_exact':qs(w),'secant_squared_bracket':bracket(w,15)})
assert prod==dist[target]
actual=n2(X[target])/n2(X[start]);gap=prod/actual
assert prod>actual
big=qs(prod);dig=hashlib.sha256(big.encode()).hexdigest()
out={
 'version':1,
 'scope':'Exact necessary bound for a nonpositive-support witness chain from vertex 153 to protected target 8 when the current centered ray directions and current true-edge graph are fixed and the endpoint radii remain those of the exact endpoint. Intermediate radial heights may vary arbitrarily. This is not a global obstruction after new directions, new edges, or macroscopic endpoint/centroid motion.',
 'lemma':'For a directed step i->j, sigma(i->j)=-x_i·(x_j-x_i)<=0 implies r_j cos(theta_ij)>=r_i. Multiplication along a path gives (r_end/r_start)^2 >= product_edges sec(theta)^2. Exact multiplicative Dijkstra minimizes that product over every acute true-edge path.',
 'start':start,'target':target,'true_edges':len(edges),'acute_edges':len(acute),
 'shortest_path':path,'edge_count':len(path)-1,
 'path_edges':per,
 'shortest_required_radius_ratio_squared_exact':big,
 'shortest_required_radius_ratio_squared_sha256':dig,
 'shortest_required_radius_ratio_squared_bracket':bracket(prod,12),
 'shortest_required_radius_ratio_bracket':sqrt_bracket(prod,12),
 'actual_endpoint_radius_ratio_squared_exact':qs(actual),
 'actual_endpoint_radius_ratio_squared_bracket':bracket(actual,12),
 'actual_endpoint_radius_ratio_bracket':sqrt_bracket(actual,12),
 'exact_squared_gap_factor':qs(gap),
 'squared_gap_factor_bracket':bracket(gap,12),
 'largest_path_angles_by_secant':[x['edge'] for x in sorted(per,key=lambda r:Q(r['secant_squared_exact']),reverse=True)[:6]],
 'dominant_gap_edge':[176,182],
 'conclusion':'The globally cheapest acute-edge route needs radius ratio >2.009856231268, while the exact endpoint supplies <1.006567220149. Thus no regrading of intermediate radii on the existing edge-direction graph can route the 153 maximum to vertex 8. New cross-gap incidence/directions or macroscopic endpoint/centroid reordering is necessary.'
}
json.dump(out,open(R/'route_bound_certificate.json','w'),indent=2)
print('WROTE exact route certificate; path edges',len(path)-1,'required ratio bracket',out['shortest_required_radius_ratio_bracket'],'actual',out['actual_endpoint_radius_ratio_bracket'])
