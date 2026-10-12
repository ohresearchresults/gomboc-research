"""Exact incremental hull extension of the C602 nonwinner by four frozen rational points.

The four controls were proposed by equal-angle/equal-log-radius interpolation from
old vertex 7 to old vertex 85 about the old own-volume centroid and rounded to the
nearest 1e-12 coordinate.  Frozen integer controls below, not trigonometric library
rounding, define the canonical experiment.  Input PARENT_COMPLEX.json contains
literal rational vertices and maximal supporting facet cycles.  No approximate
geometry is accepted: every new support and all horizon incidences are checked
exactly.  This unit deliberately rejects zero-visibility insertion degeneracies.
It does not infer an own-centroid equilibrium census from the old centre.
"""
import hashlib, json, math, sys
from fractions import Fraction as F
from pathlib import Path
sys.set_int_max_str_digits(0)
assert __debug__, 'Run with assertions enabled'
ROOT=Path(__file__).resolve().parent
NEW_NUMERATORS=[
 [-652386830976,-278549019006,-59994875610],
 [-673052036488,-291747836672,247470117785],
 [-570437000458,-249889387058,566581053189],
 [-339758403441,-150071123912,838060234941],
]
GRID=10**12

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(s,a):return tuple(s*x for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def canon(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def sha(x):return hashlib.sha256(x).hexdigest()
def encode(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,(list,tuple)):return [encode(v) for v in x]
 if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
 return x

def homogeneous(p):
 d=math.lcm(*(x.denominator for x in p));return tuple(int(x*d) for x in p)+(d,)
def primitive_plane(a,b,c):
 n=cross(sub(b,a),sub(c,a));assert n!=(0,0,0)
 h=dot(n,a);assert h!=0
 if h<0:n=mul(-1,n);h=-h
 d=math.lcm(*(x.denominator for x in n+(h,)))
 row=tuple(int(x*d) for x in n+(h,));gg=math.gcd(*row);return tuple(x//gg for x in row)
def slack(row,p):return row[3]*p[3]-dot(row[:3],p[:3])
def poly_cycle(X,ids,n):
 axis=max(range(3),key=lambda k:abs(n[k]));a,b=[k for k in range(3) if k!=axis]
 order=sorted(ids,key=lambda i:(X[i][a],X[i][b]));lo=[];hi=[]
 def turn(i,j,k):return (X[j][a]-X[i][a])*(X[k][b]-X[i][b])-(X[j][b]-X[i][b])*(X[k][a]-X[i][a])
 for seq,out in ((order,lo),(order[::-1],hi)):
  for i in seq:
   while len(out)>1 and turn(out[-2],out[-1],i)<=0:out.pop()
   out.append(i)
 cy=lo[:-1]+hi[:-1];assert len(cy)>=3
 if dot(n,cross(sub(X[cy[1]],X[cy[0]]),sub(X[cy[2]],X[cy[0]])))<0:cy.reverse()
 k=cy.index(min(cy));return cy[k:]+cy[:k]

def full_complex(X,H):
 HP=[homogeneous(p) for p in X];faces=[]
 assert len(set(H))==len(H) and all(h[3]>0 for h in H)
 for row in H:
  vals=[slack(row,p) for p in HP];assert min(vals)>=0
  ids=[i for i,s in enumerate(vals) if s==0];assert len(ids)>=3
  faces.append(poly_cycle(X,ids,row[:3]))
 edges={}
 for fi,cy in enumerate(faces):
  for i,j in zip(cy,cy[1:]+cy[:1]):edges.setdefault(tuple(sorted((i,j))),[]).append((fi,i,j))
 assert all(len(v)==2 and v[0][1:]==v[1][1:][::-1] for v in edges.values())
 active=sorted({i for cy in faces for i in cy});assert len(active)-len(edges)+len(faces)==2
 adj={i:set() for i in active}
 for i,j in edges:adj[i].add(j);adj[j].add(i)
 seen=set();todo=[active[0]]
 while todo:
  i=todo.pop()
  if i not in seen:seen.add(i);todo.extend(adj[i]-seen)
 assert seen==set(active)
 for i in active:
  normals=[H[k][:3] for k,cy in enumerate(faces) if i in cy]
  assert any(det(a,b,c)!=0 for ia,a in enumerate(normals) for ib,b in enumerate(normals) if ib>ia for c in normals[ib+1:])
 return faces,edges,active

def mass(X,faces):
 D=F(0);M=(F(0),)*3;nt=0
 for cy in faces:
  for j in range(1,len(cy)-1):
   a,b,c=[X[k] for k in (cy[0],cy[j],cy[j+1])]
   d=det(a,b,c);assert d>0;D+=d;M=add(M,mul(d,add(add(a,b),c)));nt+=1
 return D/6,mul(F(1,24),M),mul(F(1,4)/D,M),nt

def main():
 raw=(ROOT/'PARENT_COMPLEX.json').read_bytes()
 assert sha(raw)=='20024df3ddf7d5a5915fe06e6039838e7727dbdfe23bb2d6d291eeb9596d139c'
 z=json.loads(raw);X=[tuple(map(F,p)) for p in z['vertices']];H=[tuple(map(int,h)) for h in z['H']]
 assert len(X)==167 and len(H)==136
 faces,edges,active=full_complex(X,H);assert faces==z['faces'] and len(edges)==301 and len(active)==167
 V0,M0,g0,_=mass(X,faces);ledger=[];print('PARENT_GEOMETRY_AND_MASS',flush=True)
 for nums in NEW_NUMERATORS:
  p=tuple(F(x,GRID) for x in nums);hp=homogeneous(p);vis=[slack(row,hp)<0 for row in H]
  assert all(slack(row,hp)!=0 for row in H),'This fixed experiment assumes no zero visibility'
  assert any(vis) and not all(vis);idx=len(X);X.append(p)
  horizon=[(i,j) for (i,j),pair in edges.items() if vis[pair[0][0]]!=vis[pair[1][0]]]
  assert len(horizon)>=3
  HH=[row for row,v in zip(H,vis) if not v]+[primitive_plane(X[i],X[j],p) for i,j in horizon]
  H=sorted(set(HH));faces,edges,active=full_complex(X,H)
  ledger.append(dict(new_input_vertex=idx,visible_old_facets=sum(vis),horizon_edges=len(horizon),V=len(active),E=len(edges),F=len(faces)));print(ledger[-1],flush=True)
 V1,M1,g1,nt=mass(X,faces)
 route=[7,167,168,169,170,85]
 assert all(tuple(sorted((i,j))) in edges for i,j in zip(route,route[1:])), 'Free route not fully exposed'
 old_esc=[dot(sub(X[i],g0),sub(X[j],X[i])) for i,j in zip(route,route[1:])]
 new_esc=[dot(sub(X[i],g1),sub(X[j],X[i])) for i,j in zip(route,route[1:])]
 assert min(old_esc)>0
 C0=math.lcm(*(v.denominator for v in g0));G0=tuple(int(C0*v) for v in g0)
 HP=[homogeneous(p) for p in X[:167]];Z=[sub(mul(C0,p[:3]),mul(p[3],G0)) for p in HP]
 norms=[dot(p,p) for p in Z]
 safe=[i for i,p in enumerate(HP) if norms[i]*HP[7][3]**2>norms[7]*p[3]**2]
 print('SAFE_OLD_TARGETS',safe,'g0',list(map(float,g0)),flush=True)
 assert safe==[85,91,145,147,150]
 result=dict(status='COORD_C602_FIVE_LINK_EXACT_HULL_NOT_A_WINNER',VEF=[len(active),len(edges),len(faces)],C=2*len(edges),insertion_ledger=ledger,old_vertices_not_extreme=sorted(set(range(167))-set(active)),new_vertices_extreme=[i for i in range(167,171) if i in active],route=route,route_old_centre_escapes=old_esc,route_new_centre_escapes=new_esc,strictly_greater_old_radii=safe,old_volume=V0,new_volume=V1,old_centroid=g0,new_centroid=g1,centroid_delta=sub(g1,g0),new_first_moment=M1,integration_triangles=nt)
 (ROOT/'HULL_RAW.json').write_bytes(canon(dict(H=H)))
 (ROOT/'HULL_COMPLEX.json').write_bytes(canon(encode(dict(vertices=X,H=H,faces=faces,edges=sorted(edges),active=active))))
 (ROOT/'BUILD_REPORT.json').write_bytes(canon(encode(result)))
 print(result['status'],result['VEF'],result['C'],flush=True)
 print('old-route',list(map(float,old_esc)),'own-route',list(map(float,new_esc)),flush=True)
 print('old-g',list(map(float,g0)),'new-g',list(map(float,g1)),'volume',float(V1),flush=True)
 print('H bits',max(abs(i).bit_length() for h in H for i in h),flush=True)

if __name__=='__main__':main()
