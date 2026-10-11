"""Exact fixed-fan obstruction after changing the old external interface.
A mandatory connector lies on the intersection of two fixed support planes;
two other supporting inequalities bound its entire allowed segment below inlet.
No fixed value of that connector or any other internal vertex is assumed.
"""
import json,sys,math
from pathlib import Path
from fractions import Fraction as Q
import BUILD as B,NEW_BUILD
sys.set_int_max_str_digits(0)
J=[106,109,112,114,117,120,124,146,148,149]
LOW=[69,99,115,118,123]
def encode(x):
 if isinstance(x,Q):return str(x)
 if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [encode(v) for v in x]
 return x

def run(base,gen,param,a):
 P,keep,faces,labels,_=NEW_BUILD.coordinates(base,gen,param);g=tuple(map(Q,a['raw_centroid']));rho=Q(1,10**6)
 q={l:tuple(Q(v,h) for v in n) for l,n,h in zip(labels,a['normals'],a['offsets'])}
 p0=tuple(NEW_BUILD.solve([q[i] for i in [15,75,76]],[Q(1)]*3));p1=tuple(NEW_BUILD.solve([q[i] for i in [15,75,71]],[Q(1)]*3));e=B.sub(p1,p0)
 assert B.dot(e,e)>0
 assert B.dot(q[76],p0)==1 and B.dot(q[76],e)<0
 assert B.dot(q[71],p1)==1 and B.dot(q[71],e)>0
 assert all(B.dot(q[i],p)==1 for i in [15,75] for p in [p0,p1])
 assert B.dot(B.cross(q[15],q[75]),B.cross(q[15],q[75]))>0
 u=B.sub(P[111],g);z=B.sub(P[150],g);D=B.dot(B.sub(z,u),B.sub(z,u));delta=B.dot(z,z)-B.dot(u,u)
 assert 9*delta<D<10*delta
 margins={}
 def lower_point(name,p):
  gap=B.dot(u,u)-B.dot(B.sub(p,g),B.sub(p,g));robust=gap-2*rho*sum(map(abs,B.sub(P[111],p)));assert robust>0;margins[name]=robust
 for i in LOW:lower_point('LOW_'+str(i),P[i])
 lower_point('LINE_ENDPOINT_0',p0);lower_point('LINE_ENDPOINT_1',p1)
 for i in [69,107]:
  ee=B.sub(P[i],P[111]);v=-B.dot(u,ee)-rho*sum(map(abs,ee));assert v>0;margins['EXTERIOR_'+str(i)]=v
 eigen=NEW_BUILD.solve([[q[j][i] for j in [0,2,35]] for i in range(3)],B.sub(P[95],g))
 inverse=B.inverse([[q[j][i] for j in [0,2,35]] for i in range(3)])
 for k in range(3):
  v=eigen[k]-rho*sum(map(abs,inverse[k]));assert v>0;margins['APEX_'+str(k)]=v
 edges={tuple(sorted((i,j))) for cy in faces for i,j in zip(cy,cy[1:]+cy[:1])};allowed=set(J)|{111,150};adj={i:[] for i in allowed}
 for i,j in edges:
  if i in allowed and j in allowed:adj[i].append(j);adj[j].append(i)
 paths=[]
 def visit(path):
  if path[-1]==150:paths.append(path);return
  for j in sorted(adj[path[-1]]):
   if j not in path:visit(path+[j])
 visit([111]);avoiding=[p for p in paths if 109 not in p];assert avoiding
 maxn=max(len(p)-1 for p in avoiding);assert maxn==9
 energy=D-maxn*delta;robust_energy=energy-2*maxn*rho*sum(map(abs,B.sub(P[150],P[111])));assert robust_energy>0;margins['NINE_LINK_ENERGY']=robust_energy
 assert set(j for i,j in edges if i in J and j not in J)|set(i for i,j in edges if j in J and i not in J)==set(LOW)|{111,150}
 return encode(dict(status='NEW_INTERFACE_LOW_SEGMENT_FIXED_FAN_EXCLUSION_PASS',internal_labels=J,boundary_labels=sorted(set(LOW)|{111,150}),fixed_support_labels=[0,2,15,35,71,75,76],line_equalities=[15,75],line_bounds=[76,71],inlet=111,outlet=150,excluded_low_connector=109,own_centroid_centre=g,own_centroid_cube_radius=rho,physical_metric='identity',segment_endpoints=[p0,p1],apex_cone_coefficients=eigen,all_paths=paths,paths_avoiding_109=avoiding,max_links_avoiding_109=maxn,positive_robust_margins=margins,old_energy_test_10_delta_minus_D=10*delta-D,nine_delta_minus_D=9*delta-D))
if __name__=='__main__':
 b,g,p,a,out=map(Path,sys.argv[1:]);r=run(*[json.loads(s.read_text()) for s in [b,g,p,a]]);out.write_text(json.dumps(r,sort_keys=True,separators=(',',':')));print(r['status'],'paths',len(r['all_paths']),'avoiding',len(r['paths_avoiding_109']),'maxlinks',r['max_links_avoiding_109']);print('margin_min',float(min(map(Q,r['positive_robust_margins'].values()))))
