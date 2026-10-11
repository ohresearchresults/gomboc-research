# material-9638801cdac7

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

# Exact V-description audit source

This is ONE complete executed audit implementation, not two independent verifiers. It was calibrated on the literal C330_ROOTFREE_G5 point set and then used for three rational rounded radial nonwinners and a simple rational reference110 center of C330. This material supplies source only; the companion literal geometry material supplies every exact input. No accepted own110 record is changed by these tests.

Environment actually used: Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0. All acceptance predicates below are Python integer/Fraction arithmetic. SciPy nominates hull facets only. The code groups exactly coplanar supports, verifies all input containments, exact planar cycles, closed oppositely oriented two-face edge incidences, one-cycle vertex links and Euler topology, and integrates an exactly positive boundary tetrahedralization. It then checks every maximal-face side, incident vertex escape and four mixed edge-cone primitives at either the exact own filled-volume centroid or an explicitly supplied rational reference point. The separately recomputed centered first moment is a check within this implementation, not an independent second mass algorithm.

Save the following block verbatim with its final newline as EXACT_V_AUDIT.py: 6684 bytes, SHA-256 6f731c9dcfc18cefff7d60ad59d5abd28bd6d2a585257861e8e9ba2a9ec1b420.

```python
"""Exact integer-coordinate hull/own-volume equilibrium audit.
Input: {grid: positive integer, points: [[int,int,int],...]}; optional reference_center
is three rational strings in physical units. Scipy supplies facet nominations ONLY.
Each nominated maximal face, all supporting incidences, closed edge and vertex links,
Euler count and positive oriented volume are verified with exact integer arithmetic.
This is one executed audit method, NOT two independent audits.
"""
import argparse, json, math
from fractions import Fraction as F
from functools import reduce
from collections import defaultdict
from itertools import combinations
import numpy as np
from scipy.spatial import ConvexHull

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def scale(a,s):return tuple(s*x for x in a)
def cycle(points,ids,n):
 # Integer planar hull, after dropping one nonzero-normal coordinate.
 axis=max(range(3),key=lambda j:abs(n[j]));axes=[j for j in range(3) if j!=axis]
 xy={i:(points[i][axes[0]],points[i][axes[1]]) for i in ids}
 def ccw(a,b,c):
  u,v,w=xy[a],xy[b],xy[c]
  return (v[0]-u[0])*(w[1]-u[1])-(v[1]-u[1])*(w[0]-u[0])
 order=sorted(ids,key=xy.get);lo=[];hi=[]
 for i in order:
  while len(lo)>1 and ccw(lo[-2],lo[-1],i)<=0:lo.pop()
  lo.append(i)
 for i in reversed(order):
  while len(hi)>1 and ccw(hi[-2],hi[-1],i)<=0:hi.pop()
  hi.append(i)
 seq=lo[:-1]+hi[:-1];assert len(seq)>=3
 if dot(cross(sub(points[seq[1]],points[seq[0]]),sub(points[seq[2]],points[seq[0]])),n)<0:seq.reverse()
 # Canonical cyclic starting point, preserving outward orientation.
 k=min(range(len(seq)),key=lambda j:points[seq[j]])
 return seq[k:]+seq[:k]

def audit(obj):
 G=int(obj['grid']);assert G>0
 points=[tuple(int(x) for x in p) for p in obj['points']];assert len(set(points))==len(points)
 nom=ConvexHull(np.array(points,dtype=float)/G)
 planes={}
 for tri in nom.simplices:
  i,j,k=map(int,tri);n=cross(sub(points[j],points[i]),sub(points[k],points[i]));d=dot(n,points[i]);g=reduce(math.gcd,(abs(x) for x in n));assert g
  n=tuple(x//g for x in n);d//=g
  val=[dot(n,p)-d for p in points]
  if max(val)>0:
   assert min(val)>=0,('non-supporting nomination',tri.tolist())
   n=scale(n,-1);d=-d;val=[-v for v in val]
  assert max(val)==0 and min(val)<0
  planes[(n,d)]=[i for i,x in enumerate(val) if x==0]
 keys=sorted(planes);faces=[cycle(points,planes[k],k[0]) for k in keys]
 used=set(i for f in faces for i in f);edges=defaultdict(list)
 for fi,f in enumerate(faces):
  for a,b in zip(f,f[1:]+f[:1]):edges[tuple(sorted((a,b)))].append((fi,a,b))
 assert all(len(v)==2 and v[0][1:]==v[1][1:][::-1] for v in edges.values()),'surface not closed and oriented'
 V,E,H=len(used),len(edges),len(faces);assert V-E+H==2
 # At every extreme vertex its face-link is one cycle, excluding pinched surfaces.
 for v in used:
  adj=defaultdict(set)
  for (a,b),rows in edges.items():
   if v not in (a,b):continue
   x,y=rows[0][0],rows[1][0];adj[x].add(y);adj[y].add(x)
  assert all(len(s)==2 for s in adj.values())
  seen=set();todo=[next(iter(adj))]
  while todo:
   j=todo.pop()
   if j in seen:continue
   seen.add(j);todo.extend(adj[j]-seen)
  assert len(seen)==len(adj)
 # Use the mean of extreme vertices as a strictly interior rational anchor;
 # translated integer points avoid an assumption that raw origin is interior.
 K=len(used);anchor=tuple(sum(points[i][j] for i in used) for j in range(3))
 shifted=[sub(scale(p,K),anchor) for p in points]
 triangles=[(f[0],f[j],f[j+1]) for f in faces for j in range(1,len(f)-1)]
 D=0;M=[0,0,0]
 for i,j,k in triangles:
  a,b,c=shifted[i],shifted[j],shifted[k];d=det(a,b,c);assert d>0
  D+=d
  for t in range(3):M[t]+=d*(a[t]+b[t]+c[t])
 # Raw integer-unit centroid C/W, then reduced jointly for cheap exact predicates.
 W=4*D*K;C=tuple(M[t]+4*D*anchor[t] for t in range(3));g=reduce(math.gcd,[W]+[abs(x) for x in C]);W//=g;C=tuple(x//g for x in C)
 own_center=[F(x,W*G) for x in C]
 if 'reference_center' in obj:
  rs=[F(x)*G for x in obj['reference_center']];W=math.lcm(*(x.denominator for x in rs));C=tuple(int(x*W) for x in rs)
 p=[sub(scale(x,W),C) for x in points]
 assert all(dot(n,p[f[0]])>0 for (n,d),f in zip(keys,faces)), 'center is not strictly interior'
 stable=[];weakS=[];zeroS=0
 for fi,((n,d),f) in enumerate(zip(keys,faces)):
  vals=[-dot(n,cross(sub(p[b],p[a]),p[a])) for a,b in zip(f,f[1:]+f[:1])]
  zeroS+=sum(v==0 for v in vals)
  if min(vals)>0:stable.append(fi)
  elif min(vals)>=0:weakS.append(fi)
 nbr=defaultdict(set)
 for a,b in edges:nbr[a].add(b);nbr[b].add(a)
 unstable=[];weakU=[];zeroU=0
 for i in sorted(used):
  vals=[dot(p[i],sub(p[j],p[i])) for j in nbr[i]];zeroU+=sum(x==0 for x in vals)
  if max(vals)<0:unstable.append(i)
  elif max(vals)<=0:weakU.append(i)
 saddle=[];weakH=[];zeroH=0
 for (a,b),rows in sorted(edges.items()):
  e=sub(p[b],p[a]);dd=dot(e,e);tt=-dot(p[a],e)
  q=sub(scale(p[a],dd),scale(e,-tt))
  n1,n2=[keys[x[0]][0] for x in rows];g11=dot(n1,n1);g22=dot(n2,n2);g12=dot(n1,n2);gd=g11*g22-g12*g12;assert gd>0
  q1,q2=dot(q,n1),dot(q,n2);aa=q1*g22-q2*g12;bb=q2*g11-q1*g12
  vals=[tt,dd-tt,aa,bb];zeroH+=sum(x==0 for x in vals)
  if min(vals)>0:saddle.append([a,b])
  elif min(vals)>=0:weakH.append([a,b])
 # Separate centered tetra sum in the common homogeneous coordinates.
 centD=0;centM=[0,0,0]
 for i,j,k in triangles:
  dd=det(p[i],p[j],p[k]);assert dd>0;centD+=dd
  for t in range(3):centM[t]+=dd*(p[i][t]+p[j][t]+p[k][t])
 if 'reference_center' not in obj:assert centM==[0,0,0]
 centeredden=W*G;cg=reduce(math.gcd,[centeredden]+[abs(x) for i in used for x in p[i]]);centeredden//=cg
 out=dict(V=V,E=E,F=H,C=2*E,strict=[len(stable),len(unstable),len(saddle)],weak=[len(weakS),len(weakU),len(weakH)],primitive_zeros=[zeroS,zeroU,zeroH],stable_faces=stable,unstable_input_vertices=unstable,saddle_input_edges=saddle,own_centroid=[str(x) for x in own_center],reference_center=obj.get('reference_center'),volume=str(F(D,6*K**3*G**3)),positive_centered_tetrahedra=len(triangles),common_centered_denominator_bits=centeredden.bit_length(),used_input_vertices=sorted(used),faces=faces)
 if out['weak']==[0,0,0]:assert len(stable)+len(unstable)-len(saddle)==2
 return out
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('input');a.add_argument('output');args=a.parse_args();obj=json.load(open(args.input));res=audit(obj);json.dump(res,open(args.output,'w'),sort_keys=True,indent=2);print('EXACT_V_AUDIT_OK',json.dumps({k:v for k,v in res.items() if k not in ['faces','used_input_vertices']}),flush=True)
```

Usage: `python EXACT_V_AUDIT.py INPUT.json AUDIT.json`. Terminal marker is `EXACT_V_AUDIT_OK`. The output includes the complete actual face cycles and used input vertices, exact own centroid and volume, full strict/weak counts, primitive-zero counts, and centered arithmetic size. Input-index labels are not canonical RAW lexicographic labels of the older H-description auditors.
