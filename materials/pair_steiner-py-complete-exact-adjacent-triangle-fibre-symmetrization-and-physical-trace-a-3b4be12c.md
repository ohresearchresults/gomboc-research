# material-3b4be12cda6d

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""Exact fibre Steiner symmetrization for a root facet containing C,D.
python -S pair_steiner.py build|check
No numerical library, optimization, metric substitution or random input.
The construction preserves the selected actual pair trace, not complexity/SUH.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
from math import gcd,lcm
import hashlib,json,sys
assert __debug__
HERE=Path(__file__).resolve().parent
ID='ACTUAL_ADJACENT_TRIANGLE_PAIR_STEINER_CHART_V1'
def enc(x):return (json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode()
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def scale(a,s):return tuple(x*s for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def plane(n,h):
 z=list(n)+[h];m=1
 for q in z:m=lcm(m,F(q).denominator)
 z=[int(q*m) for q in z];g=0
 for q in z:g=gcd(g,abs(q))
 assert g and any(z[:3]);return tuple(q//g for q in z)
def facet_planes(v):
 found=set()
 for a,b,c in combinations(v,3):
  n=cross(sub(b,a),sub(c,a))
  if not any(n):continue
  h=dot(n,a);s=[dot(n,w)-h for w in v]
  if max(s)<=0 and min(s)<0:found.add(plane(n,h))
  elif min(s)>=0 and max(s)>0:found.add(plane(scale(n,-1),-h))
 assert len(found)>=4;return sorted(found)
def intersections(H):
 out=set()
 for a,b,c in combinations(H,3):
  d=det(a[:3],b[:3],c[:3])
  if not d:continue
  v=scale(add(add(scale(cross(b[:3],c[:3]),a[3]),scale(cross(c[:3],a[:3]),b[3])),scale(cross(a[:3],b[:3]),c[3])),F(1,d))
  if all(dot(h[:3],v)<=h[3] for h in H):out.add(v)
 assert len(out)>=4;return sorted(out)
def steiner_H(H):
 upper=[];lower=[];out=set()
 for n in H:
  a=n[0]-n[1]
  if a:
   f=(F(n[3],a),F(-n[1],a),F(-n[2],a))
   (upper if a>0 else lower).append(f)
  else:out.add(tuple(n))
 assert upper and lower
 for u in upper:
  for l in lower:
   c,b,d=sub(u,l)
   for s in (-1,1):out.add(plane((s-b,-s-b,-d),c))
 return sorted(out)
def physical(v):
 v=sorted(v);H=facet_planes(v)
 assert intersections(H)==v
 faces=[sorted(i for i,w in enumerate(v) if dot(h[:3],w)==h[3]) for h in H]
 edges=set()
 for a,b in combinations(faces,2):
  c=tuple(sorted(set(a)&set(b)))
  if len(c)>=2:assert len(c)==2;edges.add(c)
 edges=sorted(edges);cycles=[];centres=[];area_scaled=[];N=F(0);first=(F(0),)*3
 for h,face in zip(H,faces):
  adj={i:sorted(j for j in face if tuple(sorted((i,j))) in edges) for i in face}
  assert all(len(q)==2 for q in adj.values());cy=[min(face)]
  while len(cy)<len(face):
   todo=[j for j in adj[cy[-1]] if j not in cy];assert todo;cy.append(todo[0])
  assert cy[0] in adj[cy[-1]]
  if dot(h[:3],cross(sub(v[cy[1]],v[cy[0]]),sub(v[cy[2]],v[cy[0]])))<0:cy=cy[::-1]
  ar=F(0);af=(F(0),)*3
  for k in range(1,len(cy)-1):
   a,b,c=[v[cy[j]] for j in (0,k,k+1)];w=dot(h[:3],cross(sub(b,a),sub(c,a)));assert w>0
   ar+=w;af=add(af,scale(add(add(a,b),c),w/F(3)))
   d=det(a,b,c);N+=d;first=add(first,scale(add(add(a,b),c),d))
  centres.append(scale(af,1/ar));area_scaled.append(ar);cycles.append(cy)
 assert N>0;V=N/6;g=scale(first,1/(4*N));q=[];mass=[]
 for h,ar in zip(H,area_scaled):
  n=h[:3];height=h[3]-dot(n,g);assert height>0
  q.append(scale(n,1/height));mass.append(ar*height/(2*V*dot(n,n)))
 assert sum(mass)==3 and all(dot(n,g)<h for *n,h in H)
 assert all(sum(m*q[j] for m,q in zip(mass,q))==0 for j in range(3))
 assert all(sum(m*(c[j]-g[j]) for m,c in zip(mass,centres))==0 for j in range(3))
 A=[[mass[i]*(h[3]-dot(h[:3],centres[i]))/(h[3]-dot(h[:3],g)) for i in range(len(H))] for h in H]
 for a in range(len(H)):
  assert A[a][a]==0 and sum(A[a])==3
  assert all(A[a][i]>0 for i in range(len(H)) if i!=a)
  for b in range(len(H)):
   assert sum(A[a][i]*A[i][b] for i in range(len(H)))+A[a][b]==4*mass[b]
  assert all(sum(A[a][i]*q[i][j] for i in range(len(H)))==-q[a][j] for j in range(3))
 root=H.index((5,5,4,5));bx=H.index((-1,0,0,0));by=H.index((0,-1,0,0))
 ABC={(F(0),F(0),F(0)),(F(0),F(0),F(1)),(F(0),F(1),F(0))}
 ABD={(F(0),F(0),F(0)),(F(0),F(0),F(1)),(F(1),F(0),F(0))}
 assert {v[i] for i in faces[bx]}==ABC and {v[i] for i in faces[by]}==ABD
 pair=A[root][bx]+A[root][by]
 ellg=1-g[0]-g[1]-F(4,5)*g[2]
 formula=F(6,5)*(g[0]+g[1])/(6*V*ellg)
 assert pair==formula
 return {'vertices':[[str(x) for x in w] for w in v],'facet_planes':H,'facet_cycles':cycles,'true_edges':edges,
 'f_vector':[len(v),len(edges),len(H)],'volume':str(V),'centroid':list(map(str,g)),
 'facet_centres':[[str(x) for x in c] for c in centres],'cone_masses_d':list(map(str,mass)),
 'actual_Lambda':[[str(x) for x in row] for row in A],'selected_indices':[root,bx,by],
 'selected_pair':str(pair),'pair_formula':str(formula),'selected_column_values':[str(A[root][bx]),str(A[root][by])]}
def main():
 assert len(sys.argv)==2 and sys.argv[1] in ('build','check')
 original=[(0,0,0),(0,0,1),(0,1,0),(1,0,0),(F(1,100),F(4,5),F(19,80)),(F(3,4),F(1,50),F(23,80))]
 original=[tuple(map(F,v)) for v in original];raw=facet_planes(original);imageH=steiner_H(raw);image=intersections(imageH)
 a=physical(original);b=physical(image)
 assert a['volume']==b['volume'] and a['selected_pair']==b['selected_pair']
 g=list(map(F,a['centroid']));h=list(map(F,b['centroid']))
 assert h[0]==h[1] and g[0]+g[1]==h[0]+h[1] and g[2]==h[2]
 assert all((y,x,z) in image for x,y,z in image)
 assert b['selected_column_values'][0]==b['selected_column_values'][1]
 assert F(a['selected_pair'])>2
 out={'identity':ID,'input':a,'steiner_image':b,'complete_image_inequalities':imageH,
 'preserved':['volume','centroid_x_plus_y','centroid_z','both_actual_triangular_axis_facets','actual_pair_trace'],
 'not_asserted':['complexity_preservation','S_U_H_preservation','FULL_TREE253_preservation','universal_pair_maximum','C_improvement'],
 'source_pin':pin(Path(__file__).read_bytes())}
 data=enc(out);p=HERE/'pair_steiner.json'
 if sys.argv[1]=='check' or p.exists():assert p.read_bytes()==data
 else:p.write_bytes(data)
 print('ACTUAL_TRIANGLE_PAIR_STEINER_EXACT_PASS',a['f_vector'],b['f_vector'],a['selected_pair'],*pin(data),flush=True)
if __name__=='__main__':main()
