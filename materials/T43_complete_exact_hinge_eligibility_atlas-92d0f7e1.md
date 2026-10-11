# material-92d0f7e14db2

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# T43 complete exact plane-eligibility atlas for convex FULL hinges

This is an exact eligibility classification and a reusable finite search reduction, NOT an equilibrium-family exclusion or an own110 construction. The complete standalone source below repeats the literal43 integer T43 rows from fully read [internal-source-reference]. No additional files, packages or numerical hull engine are required. No worker result is being renamed. Canonical own110 remainsC622; targetC<500 is unmet.

## Geometric theorem
Let K be a bounded full-dimensional convex polyhedron and H={n.x=h} an interior-cutting plane. For n.v=0, F_v(x)=x+v max(0,n.x-h) is a determinant-one piecewise affine homeomorphism. A crossed maximal facet m_f.x<=b_f has old vertices strictly on both sides of H. The full image is convex for some sufficiently small nonzero v exactly when the cone T_H={v:n.v=0,m_f.v<=0 for all crossed facets} is nontrivial. This follows by imposing support of all lower and upper facet pieces on every transformed old vertex: crossed facets supply the zero-slack inequalities, all other nontrivial inequalities have positive slack at0. Full finite support inequalities and exact mass law are preserved in [internal-source-reference].

If H contains no old edge, every section-polygon edge is supplied by a crossed facet. Its outward projected normals positively span the section plane, hence T_H={0}. Therefore every nonzero convex full hinge must have a plane through an old edge. This necessity does not imply every edge-plane permits a hinge.

For a generic interior section containing exactly one old edge a--b and no other old vertex, let alpha,beta be the section-polygon interior angles at a,b. A nonzero hinge exists iff alpha+beta<=pi. Strict inequality gives a two-dimensional cone; equality gives one ray. To prove it, remove the outward normal of old edge a--b from the cyclic section-polygon normal fan. The remaining crossed-facet normals fit in a closed semicircle precisely when the gap across the removed normal is at least pi. The gap is the sum of the exterior turns at a and b, namely2pi-alpha-beta. All other gaps of the convex polygon are less than pi. In the feasible case the two endpoint-crossed-facet normals determine the extreme constraints; all the other crossed normals lie between them.

The test is rational, without inverse trigonometry. Set d=b-a, orient n so u=n cross d points into the section from edge a--b, and let ma,mb be the two crossed facet normals incident to a,b. Then ma.d<0<mb.d and eligibility is n.(ma cross mb)<=0. In each old-vertex-sign interval of the rational edge-plane chart n(t)=n0+t n1, the endpoint facets are fixed. The scalar test is affine in t up to a constant positive scaling and orientation. Thus there is at most one additional rational flat-angle cut in that interval. At old-vertex critical planes and chart infinity, use the complete crossed-normal cone directly; the generic two-facet shortcut is not assumed there.

## Exact result and scope
Executed standard-library CPython3.13.5. All123 true old edges were processed. There are5166 vertex-sign chart intervals, of which5028 cut the interior. Splitting at238 additional flat-endpoint thresholds gives5266 interior open cells:1142 eligible and4124 impossible. Among4905 edge-indexed critical interior planes,1219 have nonzero cones. These last counts are edge-indexed occurrences, NOT unique geometric planes: a plane containing several old edges can appear repeatedly. The chart infinity is included. Both orientation signs of a geometric plane have the same tangent-cone eligibility, although finite amplitudes and one-sided maps must still be treated appropriately.

Every open cell stores exact rational interval endpoints, endpoint facet indices, sample normal and all cone boundary rays; each critical plane stores exact normal, all zero vertices and rays. This is a complete geometric-plane eligibility atlas because every nonzero full hinge requires an old edge. It does NOT enumerate all finite velocities or determine equilibria at their true uniform-volume centroids. The 1142 feasible open cells and eligible critical planes remain a substantial finite-amplitude construction problem.

The code exhausts supporting triples to recover the exact simplicial T43 facets and true edges. On open cells it crosschecks the endpoint determinant criterion against the full cone inequalities. This is one implementation with exact redundant checks, not a claimed independent second engine. The input is simplicial; the hull helper asserts no nontriangular maximal facets. All numbers are integers/Fractions; no numerical zero threshold occurs.

## Recovery and verification
Save the code block as T43_exact_hinge_plane_atlas.py including final newline:6268bytes SHA256 cf395fd43ce877eca4dd74e9b09bc0f28ac0feffe56a4075c86be94030281ba2. Run `python -B -S T43_exact_hinge_plane_atlas.py`. Expected terminal marker EXACT_HINGE_PLANE_ATLAS_PASS and counts above. Reproduced T43_HINGE_ELIGIBILITY_ATLAS.json:1991140bytes SHA256 1625d61c49eeb6e58bbf06a9d438e1d405d2b62b9c489a8e7bb86e3416ba882a. These byte counts/hashes were checked from the actual executable unit and a completed reconstruction. Earlier compacted references to6583bytes or output1990438bytes do not identify this unit and must not replace its exact bytes.

```python
"""New finite-hinge atlas implementation; literal T43 input from immutable recovery."""
from fractions import Fraction as F
from itertools import combinations
from collections import defaultdict
import math,json
P0=[[-1131,-380,23],[-1127,-283,-218],[-1086,-225,-391],[-1013,-181,-547],[-945,-683,646],[-931,-156,-666],[-871,-801,885],[-869,-137,-738],[-780,-129,-818],[-668,-131,-892],[-635,202,-115],[-589,230,-7],[-559,224,54],[-528,217,107],[-496,331,-186],[-445,199,212],[-382,425,-214],[-366,407,-88],[-316,410,9],[-307,448,-285],[-230,462,-332],[-215,439,46],[-128,476,-366],[-30,481,-367],[-2,-201,-1240],[126,415,143],[140,485,-321],[295,502,-44],[325,457,97],[385,-951,2433],[389,393,124],[432,342,135],[462,305,132],[491,268,127],[517,230,121],[553,-80,-600],[564,161,93],[602,94,61],[633,24,23],[657,-49,-23],[674,-125,-78],[675,-281,-220],[681,-203,-143]]
P=[tuple(x) for x in P0]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(a,t):return tuple(t*x for x in a)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def primitive(a):
 g=math.gcd(*a);return tuple(x//g for x in a)
def hull(X):
 faces=[]; edges=defaultdict(list)
 for ids in combinations(range(len(X)),3):
  a,b,c=[X[i] for i in ids];m=cross(sub(b,a),sub(c,a))
  if not any(m):continue
  h=dot(m,a);s=[dot(m,p)-h for p in X]
  if min(s)<0<max(s) or min(s)==max(s):continue
  if max(s)>0:m=mul(m,-1);ids=(ids[0],ids[2],ids[1])
  assert s.count(0)==3
  m=primitive(m);h=dot(m,a);fi=len(faces);faces.append((ids,m,h))
  for e in combinations(ids,2):edges[tuple(sorted(e))].append(fi)
 assert all(len(x)==2 for x in edges.values()); assert len(X)-len(edges)+len(faces)==2
 return faces,dict(edges)
faces,edges=hull(P)

"""Exact open-chart eligibility atlas of convex FULL T43 hinges.
Dependencies: the complete immutable-source hinge_atlas.py. No floating arithmetic.
This does not solve finite-amplitude equilibrium cancellation.
"""
from fractions import Fraction as F
from pathlib import Path
import json,math,hashlib

def integer_normal(n0,n1,t):
 return primitive(add(mul(n0,t.denominator),mul(n1,t.numerator)))
def interior(n,a):
 zz=[dot(n,sub(p,P[a])) for p in P]
 return min(zz)<0<max(zz),zz

def crossed(zz):
 return [f for f,(ids,m,h) in enumerate(faces) if min(zz[i] for i in ids)<0<max(zz[i] for i in ids)]
def tangent_rays(n,fs):
 ns=[faces[f][1] for f in fs];rays=set()
 for m in ns:
  r=cross(n,m)
  if not any(r):continue
  r=primitive(r)
  for v in (r,mul(r,-1)):
   if all(dot(mm,v)<=0 for mm in ns):rays.add(v)
 return sorted(rays)

def sample(lo,hi):
 if lo is None:return hi-1 if hi is not None else F(0)
 if hi is None:return lo+1
 return (lo+hi)/2

def local_test(n,e,zz):
 a,b=e;d=sub(P[b],P[a]);u=cross(n,d)
 em=[faces[f][1] for f in edges[e]]
 su=[dot(m,u) for m in em]
 assert su[0]*su[1]>0
 if su[0]>0:n=mul(n,-1);u=mul(u,-1)
 fs=crossed(zz)
 aa=[f for f in fs if a in faces[f][0]];bb=[f for f in fs if b in faces[f][0]]
 assert len(aa)==len(bb)==1
 ma,mb=faces[aa[0]][1],faces[bb[0]][1]
 assert dot(ma,d)<0<dot(mb,d)
 turn=dot(n,cross(ma,mb))
 rays=tangent_rays(n,fs)
 assert bool(rays)==(turn<=0), (e,n,turn,rays)
 return turn,aa[0],bb[0],rays,n

def serialize(o):
 if isinstance(o,F):return str(o)
 if isinstance(o,dict):return {str(k):serialize(v) for k,v in o.items()}
 if isinstance(o,(tuple,list)):return [serialize(v) for v in o]
 return o

def run():
 out=[];counts={'old_edges':len(edges),'vertex_sign_intervals':0,'interior_intervals':0,'eligible_open_cells':0,'ineligible_open_cells':0,'flat_endpoint_cuts':0,'critical_interior_planes':0,'critical_eligible_planes':0}
 for e in sorted(edges):
  a,b=e;d=sub(P[b],P[a]);axis=min(range(3),key=lambda k:abs(d[k]));base=tuple(int(k==axis) for k in range(3));n0=primitive(cross(d,base));n1=primitive(cross(d,n0));assert any(n0) and any(n1)
  aa=[dot(n0,sub(p,P[a])) for p in P];bb=[dot(n1,sub(p,P[a])) for p in P]
  crit=sorted(set(F(-q,r) for q,r in zip(aa,bb) if r))
  cuts=[None]+crit+[None];rows=[];boundary=[]
  for lo,hi in zip(cuts,cuts[1:]):
   counts['vertex_sign_intervals']+=1;t=sample(lo,hi);n=integer_normal(n0,n1,t);ok,zz=interior(n,a)
   if not ok:continue
   counts['interior_intervals']+=1
   turn,fa,fb,rays,nor=local_test(n,e,zz)
   crossm=cross(faces[fa][1],faces[fb][1]);A=dot(n0,crossm);B=dot(n1,crossm)
   kink=F(-A,B) if B else None
   split=kink is not None and (lo is None or lo<kink) and (hi is None or kink<hi)
   subcuts=[lo,kink,hi] if split else [lo,hi]
   for ll,hh in zip(subcuts,subcuts[1:]):
    tt=sample(ll,hh);nn=integer_normal(n0,n1,tt);ok,z=interior(nn,a);assert ok
    turn,fa2,fb2,rr,nor=local_test(nn,e,z);assert (fa,fb)==(fa2,fb2)
    eligible=turn<=0;counts['eligible_open_cells' if eligible else 'ineligible_open_cells']+=1
    rows.append(dict(lo=ll,hi=hh,eligible=eligible,endpoint_facets=[fa,fb],sample=tt,normal=nor,rays=rr,turn=turn))
   if split:
    nn=integer_normal(n0,n1,kink);ok,z=interior(nn,a);turn,fa2,fb2,rr,nor=local_test(nn,e,z);assert turn==0 and len(rr)==1
    counts['flat_endpoint_cuts']+=1;boundary.append(dict(t=kink,kind='flat_endpoint',normal=nor,rays=rr))
  for tt in crit+[None]:
   nn=n1 if tt is None else integer_normal(n0,n1,tt);ok,z=interior(nn,a)
   if not ok:continue
   rr=tangent_rays(nn,crossed(z));counts['critical_interior_planes']+=1
   if rr:counts['critical_eligible_planes']+=1
   boundary.append(dict(t=tt,kind='projective_infinity' if tt is None else 'old_vertex',normal=nn,rays=rr,zero_vertices=[i for i,s in enumerate(z) if s==0]))
  out.append(dict(edge=e,n0=n0,n1=n1,cells=rows,boundaries=boundary))
 return dict(counts=counts,edges=out,scope='Complete exact projective plane eligibility atlas per labelled old edge; boundary planes may appear under more than one edge. No finite-amplitude own-equilibrium exclusion.')

if __name__=='__main__':
 out=run();raw=(json.dumps(serialize(out),sort_keys=True,separators=(',',':'))+'\n').encode();path=Path(__file__).with_name('T43_HINGE_ELIGIBILITY_ATLAS.json');path.write_bytes(raw)
 print('EXACT_HINGE_PLANE_ATLAS_PASS',out['counts'],len(raw),hashlib.sha256(raw).hexdigest(),flush=True)
```
