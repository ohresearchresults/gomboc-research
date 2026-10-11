#!/usr/bin/env python3
"""Independent exact verifier for the fixed-direction route bound."""
from fractions import Fraction as Q
from pathlib import Path
import csv,json,sys,hashlib
sys.set_int_max_str_digits(1000000)
R=Path(__file__).resolve().parent;D=json.load(open(R/'route_bound_certificate.json'))
def dot(a,b):return sum(a[k]*b[k] for k in range(3))
def n2(a):return dot(a,a)
def qs(x):return f'{x.numerator}/{x.denominator}'
X={}
with open(R/'coordinates_active_centered.csv') as f:
 for r in csv.DictReader(f):X[int(r['source_id'])]=tuple(Q(r[k]) for k in ('x_exact','y_exact','z_exact'))
E=[]
with open(R/'true_edges.csv') as f:
 for r in csv.DictReader(f):E.append((int(r['u']),int(r['v'])))
adj={i:[] for i in X};acute=0
for u,v in E:
 d=dot(X[u],X[v])
 if d>0:
  w=n2(X[u])*n2(X[v])/(d*d);assert w>=1;adj[u].append((v,w));adj[v].append((u,w));acute+=1
start,target=D['start'],D['target'];dist={start:Q(1)};prev={};unvisited=set(X)
while unvisited:
 avail=[i for i in unvisited if i in dist]
 if not avail:break
 u=min(avail,key=lambda i:dist[i]);unvisited.remove(u)
 if u==target:break
 for v,w in adj[u]:
  if v not in unvisited:continue
  z=dist[u]*w
  if v not in dist or z<dist[v]:dist[v]=z;prev[v]=u
path=[];u=target
while True:
 path.append(u)
 if u==start:break
 u=prev[u]
path.reverse();assert path==D['shortest_path'];prod=dist[target]
assert qs(prod)==D['shortest_required_radius_ratio_squared_exact']
assert hashlib.sha256(qs(prod).encode()).hexdigest()==D['shortest_required_radius_ratio_squared_sha256']
actual=n2(X[target])/n2(X[start]);assert qs(actual)==D['actual_endpoint_radius_ratio_squared_exact'];assert prod>actual
for key,x in [('shortest_required_radius_ratio_squared_bracket',prod),('actual_endpoint_radius_ratio_squared_bracket',actual),('squared_gap_factor_bracket',prod/actual)]:
 lo,hi=map(Q,D[key]);assert lo<x<hi
for key,x in [('shortest_required_radius_ratio_bracket',prod),('actual_endpoint_radius_ratio_bracket',actual)]:
 lo,hi=map(Q,D[key]);assert lo*lo<x<hi*hi
# Every stored path multiplier is exact, and the dominant gap is an actual path edge.
for r,(u,v) in zip(D['path_edges'],zip(path,path[1:])):
 assert r['edge']==[u,v];d=dot(X[u],X[v]);w=n2(X[u])*n2(X[v])/(d*d);assert qs(w)==r['secant_squared_exact']
assert tuple(D['dominant_gap_edge']) in list(zip(path,path[1:]))
print('PASS exact multiplicative Dijkstra over',len(E),'true edges and',acute,'acute edges')
print('PASS globally minimum route',path,'edges',len(path)-1)
print('PASS exact route deficit: required squared ratio >',float(prod),'actual',float(actual),'gap factor',float(prod/actual))
print('PASS no fixed-direction radial regrading of the existing graph can route 153 to target 8')
