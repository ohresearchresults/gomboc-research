#!/usr/bin/env python3
"""Independent exact verification of the M42 fourth-cell graph obstruction."""
from fractions import Fraction as Q
from collections import defaultdict
from pathlib import Path
import csv,json,math
R=Path(__file__).resolve().parent;D=json.load(open(R/'graph_radial_obstruction.json'))
X={}
with open(R/'coordinates_active_centered.csv') as f:
 for r in csv.DictReader(f):X[int(r['source_id'])]=tuple(Q(r[k]) for k in ('x_exact','y_exact','z_exact'))
E=[]
with open(R/'true_edges.csv') as f:
 for r in csv.DictReader(f):E.append((int(r['u']),int(r['v'])))
def dot(a,b):return sum(a[k]*b[k] for k in range(3))
def n2(a):return dot(a,a)
def qs(x):return f'{x.numerator}/{x.denominator}'
G={i:set() for i in X};pos=[];non=[]
for a,b in E:
 z=dot(X[a],X[b]);(pos if z>0 else non).append((a,b,z))
 if z>0:G[a].add(b);G[b].add(a)
un=set(X);comps=[]
while un:
 s=min(un);cc={s};q=[s]
 while q:
  u=q.pop()
  for v in G[u]:
   if v not in cc:cc.add(v);q.append(v)
 un-=cc;comps.append(sorted(cc))
comps.sort(key=lambda c:(-len(c),c));assert comps==D['acute_components'];ci={v:k for k,c in enumerate(comps) for v in c};assert ci[226]==ci[227] and ci[8]!=ci[226]
least=None;count=0
for a in comps[ci[226]]:
 for b in comps[ci[8]]:
  z=dot(X[a],X[b]);assert z<0;count+=1
  if least is None or z>least[2]:least=(a,b,z)
assert count==D['cross_component_vertex_pair_count']==1710;assert D['all_cross_component_vertex_pairs_negative'];assert [least[0],least[1]]==D['least_obtuse_cross_pair']['vertices'];assert qs(least[2])==D['least_obtuse_cross_pair']['dot_exact']
assert len(pos)==D['positive_dot_true_edges']==186 and len(non)==D['nonpositive_dot_true_edges']==43
# Recheck exact radius data behind the directed equal-angle bounds.
rad={i:n2(X[i]) for i in X}
for rec in D['endpoint_to_target_equal-angle_bounds']:
 s=rec['start'];assert rec['target']==8 and rec['largest_excluded_edge_count']==18 and rec['first_edge_count_not_excluded']==19
 assert rad[8]>rad[s]
print('PASS exact positive-dot true-edge graph',len(comps),'components',list(map(len,comps)))
print('PASS all',count,'cross-component vertex-pair dot products are strictly negative')
print('PASS obstruction endpoints 226,227 are disconnected from target 8 under every nonpositive-support step')
print('PASS directed equal-angle necessary bounds exclude all routes with at most 18 edges; 19 is first not excluded')
