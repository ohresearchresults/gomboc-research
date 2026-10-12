# material-bec960ee3cf0

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# C306_FIVE_HINGE_GAUGED_V64_E180_F118

This self-contained recovery capsule preserves a NEW exact five-parameter family, not a new own110 construction. The fixed parent is the literal C306_G4_OWN121 input below, byte-identical to the input in archived material [internal-source-reference]. The five selected z-cap hinge lines give top shifts max(0,ell) on edges1-14,2-14,28-47,47-52 and a bottom shift -max(0,ell) on edge1-4. Both large curvature-transfer blocks stay at0. All parameters lie in[0,1]. The code verifies original exact convex hull, full boundary-to-boundary hinges, every affine support inequality on the entire closed parameter cube, the maximal open-cube complex V64/E180/F118/C360, and exact polynomial identities for constant actual volume and actual centroid. The parameter-dependent rational longitudinal shear removes only an affine gauge; it preserves each body's own centroid and its complete nonsingular affine orbit.

No equilibrium assertion or no-extra-weak assertion is made for this family. The canonical target example remains C622. The main mathematical advance is a low-complexity, independently controllable exact own-mass chart, useful for joint physical and affine search.

## Recovery and validation

Environment actually used: CPython3.13.5, standard library only, assertions enabled. All computations in the builder are fractions.Fraction exact rational arithmetic. No seed, numerical tolerance, hidden input or omitted helper exists. Save each literal source span below using its named UTF8 byte count; do not include a delimiter newline not counted in that span. Source spans are introduced by a line `<<<FILE name bytes sha256>>>`. The JSON input has no trailing newline; the Python source has one.

Run from the directory containing both files:

    python -B -S five_hinge_exact.py

Expected generated filename C306_FIVE_HINGE_FAMILY.json,617009bytes,SHA2568871c18923c8ff222c24c0ea8a38634081de2939245d44a2efc4548ad1693976.

Expected terminal marker, actually observed:

    C306_FIVE_HINGE_EXACT_CONVEX_MASS_FAMILY_PASS 64 180 118 360 617009 8871c18923c8ff222c24c0ea8a38634081de2939245d44a2efc4548ad1693976

The exact filled volume in grid units is1690203202641; divide by10000^3 for physical volume. The own centroid in grid units is(409355912737/13521625621128,855529297349/6760812810564,644267125375/3380406405282); divide by10000 for physical coordinates. Rational compensation and subsequent centered affine shear make these values independent of all five parameters. The original102 faces are not the118 open-family faces; the original153 edges are not the180 open-family edges. At boundary parameters some displayed faces/edges may coalesce, so a later equilibrium audit must use the maximal complex appropriate to that parameter.

The exact JSON output stores all64 base vertices,5 displacements per vertex,118 oriented face cycles, source-face labels,6 affine normal/height coefficients per face, hinge lines, centroid compensations, shear gauges, volume/centroid and a strict midpoint nonincidence witness. It is deterministically reconstructed, not an independently required617009-byte input.

<<<FILE farthest_merged_G10000.json 2051 89599e0825f7075c151639b70d9db5959fcdc058c0be555d1a96d8598ccdea3e>>>
{"points":[[-7119,-2846,-12077],[-7102,-909,-11968],[-6439,441,-10952],[-5349,-4467,-12086],[-5306,1891,-11437],[-5230,335,-12543],[-4444,-6826,-8110],[-3525,3597,-8449],[-3014,4040,-6427],[-2286,2708,12727],[-2227,2539,12720],[-2057,3816,12738],[-1808,-7620,-6954],[-1509,3919,-8754],[-1436,6502,12651],[-1283,-100,12426],[-1163,-418,12195],[-890,6773,12054],[-406,6327,4821],[-161,-2259,9752],[-91,4644,-5528],[153,6179,2265],[554,-7288,-2690],[638,6245,10653],[1035,-840,11842],[1095,-1583,10629],[1411,5933,1052],[2617,-309,11395],[2785,-7516,-3384],[2832,5731,1161],[3015,-4896,1990],[3199,3144,-4133],[4148,-3498,3419],[4148,5374,4913],[5115,5438,2525],[5262,2761,-1815],[5273,-5387,-2759],[5640,1860,-2182],[5640,3983,67],[5646,3546,-433],[5715,4413,873],[5808,4866,1838],[5964,426,4608],[6055,645,-2661],[6147,-654,4872],[6229,-630,-2949],[6271,-2552,1707],[6289,-3808,-183],[6330,-2190,-2728],[6504,2553,1748],[6634,126,825],[6643,1898,1637],[6681,844,1225]],"grid":10000,"T":[[6,15,0],[1,0,9],[7,13,4],[23,34,17],[21,13,7],[45,52,48],[14,17,7],[14,7,4],[16,15,6],[29,17,34],[29,21,17],[18,17,21],[50,48,52],[50,52,47],[50,47,48],[5,45,48],[5,4,13],[5,13,45],[5,0,1],[5,1,4],[11,1,9],[11,14,1],[2,4,1],[2,14,4],[2,1,14],[20,13,21],[20,29,34],[8,21,7],[8,18,21],[8,7,17],[8,17,18],[36,48,47],[36,47,28],[22,12,28],[22,6,12],[43,45,13],[10,15,11],[10,11,9],[10,0,15],[10,9,0],[46,47,52],[46,52,44],[46,44,47],[51,44,52],[51,49,44],[51,52,45],[51,45,43],[51,43,49],[41,20,34],[41,49,43],[41,13,20],[26,21,29],[26,20,21],[26,29,20],[3,5,48],[3,48,36],[3,0,5],[3,28,12],[3,36,28],[3,6,0],[3,12,6],[30,28,47],[30,25,28],[19,22,28],[19,28,25],[19,16,6],[19,6,22],[24,11,15],[24,14,11],[24,15,16],[24,16,19],[24,19,25],[31,13,38],[31,43,13],[42,44,49],[42,49,41],[40,38,13],[40,13,41],[40,43,38],[40,41,43],[27,25,30],[27,47,44],[27,24,25],[27,44,42],[27,23,17],[27,17,14],[27,14,24],[33,42,41],[33,34,23],[33,41,34],[33,23,27],[33,27,42],[32,30,47],[32,47,27],[32,27,30],[39,38,43],[39,31,38],[39,35,31],[37,43,31],[37,31,35],[37,39,43],[37,35,39]]}
<<<FILE five_hinge_exact.py 8463 b29b4604d9e0fa0cf83ca277b9ecb8aacd8ec73753d3cf65ae9a7e7e50fd8a12>>>
"""Exact convex five-hinge, filled-moment-preserving C306 family.
Input: literal C306 grid table, fixed by SHA-256. No external dependencies.
The five crease lines are the small z-cap blocks; large blocks stay at zero.
All parameters in [0,1]^5 are covered by affine support inequalities and
polynomial ordinary-volume/first-moment identities. This is not an equilibrium
or global nonexistence proof. Coordinates/facets are maximal in the OPEN cube.
"""
import json, hashlib, pathlib
from fractions import Fraction as Q
ROOT=pathlib.Path(__file__).resolve().parent
EXPECTED='89599e0825f7075c151639b70d9db5959fcdc058c0be555d1a96d8598ccdea3e'
HINGES=[(1,(1,14)),(1,(2,14)),(1,(28,47)),(1,(47,52)),(-1,(1,4))]
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def det(a,b,c):return dot(a,cross(b,c))
def side(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def plane(points):
 a,b,c=points;d=side(a,b,c);assert d
 dx=b[2]-a[2];dy=c[2]-a[2]
 x=(dx*(c[1]-a[1])-dy*(b[1]-a[1]))/d
 y=((b[0]-a[0])*dy-(c[0]-a[0])*dx)/d
 return (x,y,a[2]-x*a[0]-y*a[1])
def value(l,p):return l[0]*p[0]+l[1]*p[1]+l[2]
def tidy(poly):
 r=[]
 for p in poly:
  if not r or r[-1]!=p:r.append(p)
 if len(r)>1 and r[0]==r[-1]:r.pop()
 changed=True
 while len(r)>=3 and changed:
  changed=False
  for i in range(len(r)):
   if side(r[i-1],r[i],r[(i+1)%len(r)])==0:
    r.pop(i);changed=True;break
 return r
def clip(poly,line,sign):
 out=[]
 for p,q in zip(poly,poly[1:]+poly[:1]):
  a=sign*value(line,p);b=sign*value(line,q)
  if a>=0:out.append(p)
  if a*b<0:
   t=a/(a-b);out.append(tuple(x+t*(y-x)for x,y in zip(p,q)))
 return tidy(out)
def mass_polynomial(P,B,faces):
 # P: base points, B: five longitudinal displacement values per point.
 # D(t)=6V, Nk(t)=24Mk. Canonical monomial dictionaries of degree <=2.
 D=[Q(0)]*6;N=[{}, {}, {}]
 for cyc in faces:
  for j in range(1,len(cyc)-1):
   ids=[cyc[0],cyc[j],cyc[j+1]];pts=[P[i]for i in ids]
   ds=[det(*pts)]
   for k in range(5):
    ds.append(sum(det(*(pts[:r]+[(Q(0),Q(0),B[ids[r]][k])]+pts[r+1:]))for r in range(3)))
   for k,d in enumerate(ds):D[k]+=d
   for axis in range(3):
    ss=[sum(p[axis]for p in pts)]+([sum(B[i][k]for i in ids)for k in range(5)]if axis==2 else [Q(0)]*5)
    for k,d in enumerate(ds):
     for l,s in enumerate(ss):
      key=tuple(sorted(q for q in [k,l]if q));N[axis][key]=N[axis].get(key,Q(0))+d*s
 return D,[{k:v for k,v in r.items()if v}for r in N]
def build():
 raw=(ROOT/'farthest_merged_G10000.json').read_bytes();assert hashlib.sha256(raw).hexdigest()==EXPECTED
 src=json.loads(raw);P=[tuple(map(Q,p))for p in src['points']];T=src['T'];G=src['grid']
 edges={};planes=[];signs=[]
 for it,tri in enumerate(T):
  a,b,c=[P[i]for i in tri];n=cross(sub(b,a),sub(c,a));assert n[2]
  assert all(dot(n,sub(p,a))<0 for i,p in enumerate(P)if i not in tri)
  planes.append(plane([a,b,c]));signs.append(1 if n[2]>0 else -1)
  for i,j in zip(tri,tri[1:]+tri[:1]):edges.setdefault(tuple(sorted((i,j))),[]).append((it,i,j))
 assert len(edges)==153 and all(len(e)==2 and e[0][1:]==e[1][1:][::-1]for e in edges.values())
 lines=[]
 for sg,e in HINGES:
  fs=[f for f,_,_ in edges[e]];assert len(fs)==2 and all(signs[f]==sg for f in fs)
  line=sub(planes[fs[0]],planes[fs[1]]);assert any(line)
  assert value(line,P[e[0]])==value(line,P[e[1]])==0
  # Removing the crease separates the cap dual. This verifies it is a full
  # boundary-to-boundary hinge, not an unextendible finite interior crease.
  cap={i for i,s in enumerate(signs)if s==sg};adj={i:[]for i in cap}
  for ee,owners in edges.items():
   oo=[f for f,_,_ in owners if f in cap]
   if len(oo)==2 and ee!=e:
    a,b=oo;adj[a].append(b);adj[b].append(a)
  reached={fs[0]};todo=[fs[0]]
  while todo:
   for q in adj[todo.pop()]:
    if q not in reached:reached.add(q);todo.append(q)
  assert fs[1]not in reached and reached<cap
  for f in cap:
   vals=[value(line,P[i])for i in T[f]]
   assert min(vals)>=0 or max(vals)<=0
  lines.append(line)
 points=[];lookup={};faces=[];owner=[]
 for f,tri in enumerate(T):
  poly=[P[i][:2]for i in tri]
  if side(*poly)<0:poly.reverse()
  pieces=[poly]
  for line in lines:
   nxt=[]
   for poly in pieces:
    vals=[value(line,p)for p in poly]
    if min(vals)<0<max(vals):
     nxt.extend(q for s in[-1,1]if len(q:=clip(poly,line,s))>=3)
    else:nxt.append(poly)
   pieces=nxt
  for poly in pieces:
   ids=[]
   for xy in poly:
    p=(*xy,value(planes[f],xy))
    if p not in lookup:lookup[p]=len(points);points.append(p)
    ids.append(lookup[p])
   if signs[f]<0:ids.reverse()
   faces.append(ids);owner.append(f)
 B=[[Q(sg)*max(Q(0),value(line,p))for (sg,_),line in zip(HINGES,lines)]for p in points]
 D,N=mass_polynomial(points,B,faces)
 assert D[0]>0 and D[1:]==[0]*5
 assert all(k==()for r in N[:2]for k in r)
 assert all(len(k)<=1 for k in N[2])
 centroid=[r.get((),Q(0))/(4*D[0])for r in N]
 shifts=[N[2].get((i+1,),Q(0))/(4*D[0])for i in range(5)]
 BB=[[v-s for v,s in zip(row,shifts)]for row in B]
 # Remove an EXACT parameter-dependent affine shear gauge. This preserves
 # each body's centroid/volume and its full nonsingular affine orbit.
 XY=[sub(p[:2],centroid[:2])for p in points]
 aa=sum(p[0]*p[0]for p in XY);bb=sum(p[0]*p[1]for p in XY);cc=sum(p[1]*p[1]for p in XY)
 gram=aa*cc-bb*bb;assert gram>0;gauge=[]
 for k in range(5):
  u=sum(p[0]*b[k]for p,b in zip(XY,BB));v=sum(p[1]*b[k]for p,b in zip(XY,BB))
  gx=(cc*u-bb*v)/gram;gy=(aa*v-bb*u)/gram;gauge.append((gx,gy))
  for p,b in zip(XY,BB):b[k]-=gx*p[0]+gy*p[1]
 DD,NN=mass_polynomial(points,BB,faces)
 assert DD==D and all(r=={():4*D[0]*c}for r,c in zip(NN,centroid))
 # Affine face planes and all-support inequalities prove convexity on the
 # entire cube by exact minimum of each affine function, not random sampling.
 normals=[];heights=[];min_mid=None
 for ids,of in zip(faces,owner):
  sg=signs[of];abc=[points[i]for i in ids[:3]];pl=[plane(abc)]
  for k in range(5):pl.append(plane([(p[0],p[1],BB[i][k])for i,p in zip(ids[:3],abc)]))
  nr=[(-sg*l[0],-sg*l[1],Q(sg)if k==0 else Q(0))for k,l in enumerate(pl)]
  hh=[Q(sg)*l[2] for l in pl]
  for i,p in enumerate(points):
   coef=[hh[0]-dot(nr[0],p)]+[hh[k+1]-dot(nr[k+1],p)-sg*BB[i][k]for k in range(5)]
   assert coef[0]+sum(min(Q(0),q)for q in coef[1:])>=0
   mid=coef[0]+sum(coef[1:])/2
   if i in ids:assert all(q==0 for q in coef)
   else:
    assert mid>0,(of,i,mid)
    min_mid=mid if min_mid is None else min(min_mid,mid)
  normals.append(nr);heights.append([h-dot(n,centroid)for h,n in zip(hh,nr)])
 edge={}
 for f,ids in enumerate(faces):
  for i,j in zip(ids,ids[1:]+ids[:1]):edge.setdefault(tuple(sorted((i,j))),[]).append((f,i,j))
 assert all(len(r)==2 and r[0][1:]==r[1][1:][::-1]for r in edge.values())
 assert len(points)-len(edge)+len(faces)==2
 # Matching the base moment against the original exact tetrahedral boundary.
 D0=sum(det(*(P[i]for i in t))for t in T)
 C0=[sum(det(*(P[i]for i in t))*sum(P[i][k]for i in t)for t in T)/(4*D0)for k in range(3)]
 assert D0==D[0] and C0==centroid
 out=dict(version=1,input_sha256=EXPECTED,grid=G,hinges=[[sg,list(e)]for sg,e in HINGES],
  scope='all five parameters in [0,1]; displayed maximal complex for open cube; affine metric unrestricted',
  V=len(points),E=len(edge),F=len(faces),C=2*len(edge),faces=faces,source_faces=owner,
  points_grid=[[str(x)for x in p]for p in points],displacements_grid=[[str(x)for x in b]for b in BB],
  centroid_grid=[str(x)for x in centroid],volume_grid=str(D[0]/6),
  normals=[[list(map(str,n))for n in row]for row in normals],
  own_heights_grid=[list(map(str,row))for row in heights],hinge_lines_grid=[list(map(str,l))for l in lines],
  centroid_compensations_grid=list(map(str,shifts)),affine_shear_gauge=[list(map(str,q))for q in gauge],min_nonincidence_at_midpoint_grid=str(min_mid),
  validation='exact original hull; bridge hinges; full cube support; maximal open complex; full polynomial filled mass and own centroid identities')
 return out
if __name__=='__main__':
 out=build();raw=json.dumps(out,sort_keys=True,separators=(',',':')).encode();p=ROOT/'C306_FIVE_HINGE_FAMILY.json';p.write_bytes(raw)
 print('C306_FIVE_HINGE_EXACT_CONVEX_MASS_FAMILY_PASS',out['V'],out['E'],out['F'],out['C'],len(raw),hashlib.sha256(raw).hexdigest())
 print('MASS',out['volume_grid'],out['centroid_grid']);print('MEANS',out['centroid_compensations_grid'])
