#!/usr/bin/env python3
from fractions import Fraction as Q
from pathlib import Path
from collections import defaultdict
import csv,json,math,mpmath as mp
R=Path(__file__).resolve().parent
X={}
with open(R/'coordinates_active_centered.csv') as f:
 for r in csv.DictReader(f):X[int(r['source_id'])]=tuple(Q(r[k]) for k in ('x_exact','y_exact','z_exact'))
E=[]
with open(R/'true_edges.csv') as f:
 for r in csv.DictReader(f):E.append((int(r['u']),int(r['v'])))
def dot(a,b):return sum(a[k]*b[k] for k in range(3))
def n2(a):return dot(a,a)
def qs(x):return f'{x.numerator}/{x.denominator}'
rad={i:n2(x) for i,x in X.items()};N={i:set() for i in X};acute=[];nonacute=[]
for a,b in E:
 d=dot(X[a],X[b]);(acute if d>0 else nonacute).append((a,b,d))
 if d>0:N[a].add(b);N[b].add(a)
# exact connected components in positive-dot true-edge graph
un=set(X);components=[]
while un:
 s=min(un);seen={s};q=[s]
 while q:
  u=q.pop()
  for v in N[u]:
   if v not in seen:seen.add(v);q.append(v)
 un-=seen;components.append(sorted(seen))
components.sort(key=lambda c:(-len(c),c))
ci={v:k for k,c in enumerate(components) for v in c}
assert len(components)==2 and ci[226]==ci[227] and ci[8]!=ci[227]
cross_edges=[]
for a,b in E:
 if ci[a]!=ci[b]:
  d=dot(X[a],X[b]);assert d<0
  cos=d/math.sqrt(float(rad[a]*rad[b]));angle=math.degrees(math.acos(max(-1,min(1,float(cos)))))
  cross_edges.append({'edge':[a,b],'dot_exact':qs(d),'dot_decimal':float(d),'angle_degrees':angle})
# stronger: every cross-component vertex pair is obtuse, not only existing true edges
cross_pairs=[];maxpair=None
for a in components[ci[227]]:
 for b in components[ci[8]]:
  d=dot(X[a],X[b]);assert d<0,(a,b,d)
  if maxpair is None or d>maxpair[2]:maxpair=(a,b,d)
  cross_pairs.append((a,b,d))
# directed interval equal-angle route lower bound from obstruction endpoints to target
mp.iv.dps=80
def ivq(q):return mp.iv.mpf([str(q.numerator),str(q.numerator)])/mp.iv.mpf([str(q.denominator),str(q.denominator)])
def interval_text(x):return str(x)
def route_min_edges(s,t,maxm=64):
 c=ivq(dot(X[s],X[t]))/mp.iv.sqrt(ivq(rad[s])*ivq(rad[t]))
 theta=mp.iv.atan2(mp.iv.sqrt(1-c*c),c)
 avail=mp.iv.sqrt(ivq(rad[t])/ivq(rad[s]))
 rows=[];first=None
 for m in range(1,maxm+1):
  if float(theta.a)/m>=math.pi/2:
   req=None;excluded=True
  else:
   req=(1/mp.iv.cos(theta/m))**m
   excluded=float(req.a)>float(avail.b)
  rows.append({'edge_count':m,'required_ratio_interval':'infinite (some step must be >= pi/2)' if req is None else interval_text(req),'excluded_by_available_ratio':excluded})
  if not excluded and first is None:first=m;break
 assert first is not None
 return {'start':s,'target':t,'angle_interval_radians':interval_text(theta),'angle_interval_degrees':interval_text(theta*mp.iv.mpf([180,180])/mp.iv.pi),'available_radius_ratio_interval':interval_text(avail),'first_edge_count_not_excluded':first,'largest_excluded_edge_count':first-1,'tested_bounds':rows}
routes=[route_min_edges(226,8),route_min_edges(227,8)]
out={'version':2,'theorem':'A nonpositive-support witness step i->j satisfies x_i.x_j >= ||x_i||^2 > 0, so it can use only a positive-dot (acute) true edge. The exact positive-dot true-edge graph below has two components, with the obstruction endpoints and target 8 in different components. Hence no witness chain exists on the current actual graph, for any regrading of radii that leaves the rays and graph fixed.','actual_vertices':len(X),'true_edges':len(E),'positive_dot_true_edges':len(acute),'nonpositive_dot_true_edges':len(nonacute),'acute_components':components,'obstruction_component_index':ci[227],'target_component_index':ci[8],'cross_component_true_edges':cross_edges,'all_cross_component_vertex_pairs_negative':True,'cross_component_vertex_pair_count':len(cross_pairs),'least_obtuse_cross_pair':{'vertices':[maxpair[0],maxpair[1]],'dot_exact':qs(maxpair[2]),'dot_decimal':float(maxpair[2]),'angle_degrees':math.degrees(math.acos(float(maxpair[2])/math.sqrt(float(rad[maxpair[0]]*rad[maxpair[1]]))))},'endpoint_to_target_equal-angle_bounds':routes,'scope':'The component theorem is exact for the endpoint graph and rays. The edge-count bounds are directed interval necessary bounds even for newly inserted equal-angle chains with the same endpoint rays/radii. Topology change, macroscopic ray rotation, endpoint deactivation, or centroid motion is not excluded.'}
json.dump(out,open(R/'graph_radial_obstruction.json','w'),indent=2)
print('PASS exact acute-component obstruction')
print('components',[(len(c),c[0],c[-1]) for c in components])
print('cross edges',len(cross_edges),'least obtuse',out['least_obtuse_cross_pair'])
for z in routes:print(z['start'],'largest excluded',z['largest_excluded_edge_count'],'first unexcluded',z['first_edge_count_not_excluded'],'avail',z['available_radius_ratio_interval'])
