from fractions import Fraction as Q
from math import lcm
from collections import Counter
import sys
sys.set_int_max_str_digits(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(s,a):return tuple(s*x for x in a)
def finish(A,B):
 assert A==B
 X=[tuple(map(Q,p)) for p in A['raw_vertices']];c=tuple(map(Q,A['raw_centroid']));C=lcm(*(v.denominator for v in c));M=tuple(int(v*C) for v in c);bs=[lcm(*(v.denominator for v in p)) for p in X];aa=[tuple(int(b*v) for v in p) for p,b in zip(X,bs)];zz=[sub(mul(C,a),mul(b,M)) for a,b in zip(aa,bs)];normal=A['normals'];hc=[h*C-dot(n,M) for h,n in zip(A['offsets'],normal)];assert min(hc)>0
 pu=[];up=[]
 for i,(j,sg) in enumerate(A['vertex_max_escape_signs']):
  if i in A['unstable_vertices']:assert sg<0;pu.append(-1);continue
  e=sub(mul(bs[i],aa[j]),mul(bs[j],aa[i]));num=C*dot(zz[i],e);den=bs[j]*dot(zz[i],zz[i]);assert num>0 and den>0;up.append(Q(num,den));pu.append(j)
 ps=[];sp=[]
 for i,n in enumerate(normal):
  nn=dot(n,n);bestdot=None;jbest=None
  for j,m in enumerate(normal):
   if i==j:continue
   nd=dot(n,m)
   if jbest is None or nd*hc[jbest]>=bestdot*hc[j]:bestdot=nd;jbest=j
  best=Q(bestdot*hc[i]-nn*hc[jbest],nn*hc[jbest])
  if i in A['stable_face_ids']:assert best<0;ps.append(-1)
  else:
   assert best>0;sp.append(best);ps.append(jbest);assert dot(normal[jbest],normal[jbest])*hc[i]**2>nn*hc[jbest]**2
 def paths(par,roots):
  out=[]
  for i in range(len(par)):
   p=[i]
   while par[p[-1]]!=-1:
    j=par[p[-1]];assert j not in p;p.append(j)
   assert p[-1] in roots;out.append(p)
  return out
 ppaths=paths(pu,A['unstable_vertices']);spaths=paths(ps,A['stable_face_ids']);degrees=Counter(v for e in A['edges'] for v in e);excess=sum(d-3 for d in degrees.values());assert A['E']==3*A['F']-6-excess
 def floor(q):return q.numerator*10**12//q.denominator
 return dict(V=A['V'],E=A['E'],F=A['F'],C=A['V']+A['E']+A['F']-2,counts=A['counts'],weak=A['weak'],degree_histogram=sorted(Counter(degrees.values()).items()),facet_size_histogram=sorted(Counter(map(len,A['faces'])).items()),nonsimple_vertices=[dict(vertex=i,degree=d,incident_input_rows=[A['active_input_indices'][j] for j,cy in enumerate(A['faces']) if i in cy]) for i,d in sorted(degrees.items()) if d>3],stable_face_ids=A['stable_face_ids'],stable_input_rows=[A['active_input_indices'][j] for j in A['stable_face_ids']],unstable_vertices=A['unstable_vertices'],unstable_raw_coordinates=[A['raw_vertices'][i] for i in A['unstable_vertices']],saddle_edges=A['saddle_edges'],primal_parent=pu,primal_paths=ppaths,polar_parent=ps,polar_paths=spaths,primal_relative_margin_floor_1e12=floor(min(up)),polar_relative_margin_floor_1e12=floor(min(sp)),edge_primitive_count=A['edge_primitive_count'],edge_primitive_zero_count=A['edge_primitive_zero_count'],face_primitive_zero_count=A['face_primitive_zero_count'],vertex_max_zero_count=A['vertex_max_zero_count'],centred_first_moments=A['centred_first_moments'],ordinary_volume=A['ordinary_volume'],raw_first_moments=A['raw_first_moments'],raw_centroid=A['raw_centroid'])
