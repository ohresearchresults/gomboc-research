"""Exact whole-boundary sublevels and complete witness forests.
Radial levels are multiplied by the common squared centroid denominator.
That positive scale cancels from every persistence ratio and graph ordering.
"""
from fractions import Fraction as F
from math import lcm
import sys,json,hashlib
from pathlib import Path
sys.set_int_max_str_digits(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(x,a):return tuple(x*y for y in a)
def floor(x):return (x*10**12).numerator//(x*10**12).denominator

def extras(raw,A,B):
 for key in A:
  if key!='triangles':assert A[key]==B[key],key
 assert A['weak']==[0,0,0]
 counts=A['counts'];faces=A['faces'];edges=[tuple(e) for e in A['edges']]
 X=[tuple(map(F,p)) for p in A['raw_vertices']];g=tuple(map(F,A['raw_centroid']))
 dc=lcm(*(v.denominator for v in g));mc=tuple(int(dc*v) for v in g)
 bs=[lcm(*(v.denominator for v in p)) for p in X];aa=[tuple(int(b*v) for v in p) for b,p in zip(bs,X)]
 zi=[sub(mul(dc,a),mul(b,mc)) for a,b in zip(aa,bs)]
 norms=[tuple(p) for p in raw['I']];hc=[raw['D']*dc-dot(n,mc) for n in norms];assert min(hc)>0
 edgefaces={};emin={};edge_signs=[]
 for fi,cy in enumerate(faces):
  for a,b in zip(cy,cy[1:]+cy[:1]):edgefaces.setdefault(tuple(sorted((a,b))),[]).append(fi)
 assert sorted(edgefaces)==edges
 for i,j in edges:
  e=sub(mul(bs[i],aa[j]),mul(bs[j],aa[i]));ee=dot(e,e);z=zi[i];ze=dot(z,e);tn=-ze*bs[j];td=dc*ee
  if tn<=0:v=F(dot(z,z),bs[i]**2)
  elif tn>=td:v=F(dot(zi[j],zi[j]),bs[j]**2)
  else:v=F(dot(z,z)*ee-ze*ze,bs[i]**2*ee)
  assert v>0;emin[i,j]=v
 for er in A['edge_cone']:
  signs=[(F(v)>0)-(F(v)<0) for v in er[2]];assert 0 not in signs;edge_signs.append([*er[0],*signs])
 assert len(edge_signs)==A['E']
 births=[]
 for fi,cy in enumerate(faces):
  inside=min(A['face_signs'][fi])>=0
  assert inside==(fi in A['stable_face_ids'])
  v=F(hc[fi]**2,dot(norms[fi],norms[fi])) if inside else min(emin[tuple(sorted(e))] for e in zip(cy,cy[1:]+cy[:1]))
  births.append(v)
 events=[(v,0,i) for i,v in enumerate(births)]+[(v,1,e) for e,v in emin.items()]
 par=list(range(len(faces)));active=set();bars=[]
 def root(i):
  while par[i]!=i:par[i]=par[par[i]];i=par[i]
  return i
 for v,kind,key in sorted(events):
  if kind==0:active.add(key);continue
  f,h=edgefaces[key];assert f in active and h in active;u,w=root(f),root(h)
  if u==w:continue
  live,dead=sorted((u,w),key=lambda i:(births[i],i));assert v>=births[dead]
  if v>births[dead]:
   assert list(key) in A['saddle_edges'];assert dead in A['stable_face_ids']
   Bbar=1-births[dead]/v;bars.append(dict(stable_face_id=dead,stable_face=faces[dead],saddle_edge=list(key),relative_squared_bar=str(Bbar),bar_floor_1e12=floor(Bbar)))
  par[dead]=live
 surv={root(i) for i in range(len(faces))};assert len(surv)==1
 assert len(bars)==counts[0]-1==len(A['saddle_edges'])
 assert {tuple(v['saddle_edge']) for v in bars}=={tuple(e) for e in A['saddle_edges']}
 def paths(parent,roots):
  out=[]
  for i in range(len(parent)):
   path=[i]
   while parent[path[-1]]!=-1:
    j=parent[path[-1]];assert j not in path;path.append(j)
   assert path[-1] in roots;out.append(path)
  return out
 # Use the auditor's exact maximum escape choices for the physical forest.
 pu=[];um=[]
 for i,(j,v) in enumerate(A['vertex_max_escape']):
  if i in A['unstable_vertices']:assert F(v)<0;pu.append(-1);continue
  e=sub(mul(bs[i],aa[j]),mul(bs[j],aa[i]));num=dot(zi[i],e);assert num>0
  margin=F(dc*num,bs[j]*dot(zi[i],zi[i]));um.append(margin);pu.append(j)
 # A finite pole forest need not use maximum arrows. Fast numerical selection is
 # deliberately absent: test short-to-long exact norm order until a witness is found.
 ps=[];sm=[]
 for i,n in enumerate(norms):
  nn=dot(n,n);chosen=None
  if i in A['stable_face_ids']:
   assert all(dot(n,m)*hc[i]-nn*hc[j]<0 for j,m in enumerate(norms) if j!=i)
   ps.append(-1);continue
  for j,m in enumerate(norms):
   if j==i:continue
   num=dot(n,m)*hc[i]-nn*hc[j]
   if num>0:
    margin=F(num,nn*hc[j]);
    if chosen is None or margin>chosen[0]:chosen=(margin,j)
  assert chosen is not None;sm.append(chosen[0]);ps.append(chosen[1])
 upaths=paths(pu,A['unstable_vertices']);spaths=paths(ps,A['stable_face_ids'])
 return dict(V=A['V'],E=A['E'],F=A['F'],counts=counts,weak=A['weak'],edge_primitive_zero_count=0,edge_primitive_count=4*A['E'],edge_signs=edge_signs,
  ordinary_volume=A['volume'],raw_first_moments=A['raw_first_moments'],raw_centroid=A['raw_centroid'],centred_first_moments=A['first_moments'],
  stable_face_ids=A['stable_face_ids'],stable_faces=A['stable_faces'],unstable_vertices=A['unstable_vertices'],saddle_edges=A['saddle_edges'],
  whole_boundary_sublevels=dict(method='All exact maximal-facet ball-intersections, true-edge adjacency; scaled by the common centroid denominator squared',persistent_stable_face_id=next(iter(surv)),finite_bars=bars,facet_scaled_minima=list(map(str,births)),edge_scaled_minima=[[i,j,str(v)] for (i,j),v in sorted(emin.items())]),
  primal_forest=dict(parents=pu,roots=A['unstable_vertices'],paths=upaths,min_relative_dot=str(min(um)),min_relative_dot_floor_1e12=floor(min(um))),
  polar_forest=dict(parents=ps,roots=A['stable_face_ids'],paths=spaths,min_relative_dot=str(min(sm)),min_relative_dot_floor_1e12=floor(min(sm))))

if __name__=='__main__':
 raw=json.loads(Path(sys.argv[1]).read_text());A=json.loads(Path(sys.argv[2]).read_text());B=json.loads(Path(sys.argv[3]).read_text());r=extras(raw,A,B)
 bb=json.dumps(r,sort_keys=True,separators=(',',':')).encode();Path(sys.argv[4]).write_bytes(bb)
 print('EXACT_BOTH_AUDITS_ALL_COMMON_FIELDS_MATCH_FULL_BOUNDARY_AND_FORESTS_PASS',r['V'],r['E'],r['F'],r['counts'],r['weak'],'zeros',r['edge_primitive_zero_count'],flush=True)
 print('EXTRA_SHA',len(bb),hashlib.sha256(bb).hexdigest(),flush=True)
 print('FINITE_BARS',[b['bar_floor_1e12'] for b in r['whole_boundary_sublevels']['finite_bars']],'FOREST_RESERVES',r['primal_forest']['min_relative_dot_floor_1e12'],r['polar_forest']['min_relative_dot_floor_1e12'],flush=True)
 print('CRITICALS',r['stable_face_ids'],r['stable_faces'],r['unstable_vertices'],r['saddle_edges'],flush=True)
 print('V_COM_FLOAT',float(F(r['ordinary_volume'])),list(map(lambda x:float(F(x)),r['raw_centroid'])),flush=True)
