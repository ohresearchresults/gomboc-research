#!/usr/bin/env python3
from fractions import Fraction as Q
from pathlib import Path
import csv,json,heapq,math,sys
R=Path(__file__).resolve().parent
X={}
with open(R/'coordinates_active_centered.csv') as f:
 for r in csv.DictReader(f):X[int(r['source_id'])]=tuple(Q(r[k]) for k in ('x_exact','y_exact','z_exact'))
E=[]
with open(R/'true_edges.csv') as f:
 for r in csv.DictReader(f):E.append((int(r['u']),int(r['v'])))
def dot(a,b):return sum(a[k]*b[k] for k in range(3))
def n2(a):return dot(a,a)
rad={i:n2(x) for i,x in X.items()}
N={i:[] for i in X}
for a,b in E:
 d=dot(X[a],X[b])
 if d>0:
  c2=d*d/(rad[a]*rad[b])
  w=-.5*math.log(float(c2))
  N[a].append((b,w,c2));N[b].append((a,w,c2))

def route(s,t):
 dist={s:0.0};prev={};pc={};pq=[(0.,s)]
 while pq:
  d,u=heapq.heappop(pq)
  if d!=dist[u]:continue
  if u==t:break
  for v,w,c2 in N[u]:
   nd=d+w
   if nd<dist.get(v,float('inf')):
    dist[v]=nd;prev[v]=u;pc[v]=c2;heapq.heappush(pq,(nd,v))
 assert t in dist
 path=[];u=t
 while u!=s:path.append(u);u=prev[u]
 path.append(s);path.reverse()
 req2=Q(1);steps=[]
 for a,b in zip(path,path[1:]):
  c2=next(z for v,w,z in N[a] if v==b);req2/=c2
  angle=math.acos(math.sqrt(float(c2)))
  steps.append({'edge':[a,b],'cosine_squared_exact':f'{c2.numerator}/{c2.denominator}','angle_radians':angle,'angle_degrees':angle*180/math.pi,'required_step_ratio':1/math.sqrt(float(c2))})
 act2=rad[t]/rad[s]
 return {'start':s,'target':t,'path':path,'edge_count':len(path)-1,'steps':steps,'required_radius_ratio_squared_exact':f'{req2.numerator}/{req2.denominator}','required_radius_ratio_interval':[math.nextafter(math.sqrt(float(req2)),-math.inf),math.nextafter(math.sqrt(float(req2)),math.inf)],'available_radius_ratio_squared_exact':f'{act2.numerator}/{act2.denominator}','available_radius_ratio_interval':[math.nextafter(math.sqrt(float(act2)),-math.inf),math.nextafter(math.sqrt(float(act2)),math.inf)],'deficit_factor_squared_exact':f'{(req2/act2).numerator}/{(req2/act2).denominator}','deficit_factor_interval':[math.nextafter(math.sqrt(float(req2/act2)),-math.inf),math.nextafter(math.sqrt(float(req2/act2)),math.inf)],'dominant_step':max(steps,key=lambda z:z['angle_radians'])}
out={'version':1,'theorem':'For a nonpositive-support edge step i->j, r_j cos(theta_ij)>=r_i. Therefore any directed witness path requires the product of secants recorded below. Exact squared products are used; float intervals are display-only outward nextafter enclosures.','obstruction_edge':[226,227],'routes':[route(226,8),route(227,8)],'scope':'Necessary fixed-ray/true-edge-graph bounds. They do not exclude a topology change, ray rotation, vertex deactivation, or macroscopic centroid motion.'}
json.dump(out,open(R/'route_bound_certificate.json','w'),indent=2)
for z in out['routes']:
 print(z['start'],'edges',z['edge_count'],'req',z['required_radius_ratio_interval'],'avail',z['available_radius_ratio_interval'],'factor',z['deficit_factor_interval'],'dominant',z['dominant_step']['edge'],z['dominant_step']['angle_degrees'])
