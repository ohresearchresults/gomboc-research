"""Independent exact hull/physics audit: 3-D supporting lines, shifted tetrahedra,
explicit perpendicular projections, and cross-product normal-cone coefficients.
Python standard library only. Input JSON has I (integer triples) and D>0.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import gcd
from pathlib import Path
import sys,json,hashlib
sys.set_int_max_str_digits(0)
def plus(a,b):return tuple(x+y for x,y in zip(a,b))
def minus(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(a,s):return tuple(x*s for x in a)
def inner(a,b):return sum(x*y for x,y in zip(a,b))
def outer(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def determinant(a,b,c):return inner(a,outer(b,c))
ZERO=(0,0,0)
def audit(I,D):
 I=[tuple(map(int,p)) for p in I];assert D>0 and len(set(I))==len(I)
 # Enumerate every potential supporting plane; do not use a numerical hull.
 planes={}
 for a,b,c in combinations(I,3):
  n=outer(minus(b,a),minus(c,a))
  if n==ZERO:continue
  h=inner(n,a);v=[inner(n,p)-h for p in I]
  if min(v)>=0:n=mul(n,-1);h=-h;v=[-x for x in v]
  if max(v)>0:continue
  assert min(v)<0
  g=gcd(*n,h);key=tuple(x//g for x in n)+(h//g,)
  planes[key]=[k for k,x in enumerate(v) if x==0]
 keys=sorted(planes);faces=[]
 # A polygon edge is an extremal supported line inside its supporting plane.
 for key in keys:
  n=key[:3];ids=planes[key];succ={}
  for a,b in combinations(ids,2):
   e=minus(I[b],I[a]);l=inner(e,e)
   vals={k:inner(n,outer(e,minus(I[k],I[a]))) for k in ids}
   zeros=[k for k in ids if vals[k]==0]
   pro=[inner(e,minus(I[k],I[a])) for k in zeros]
   if min(pro)<0 or max(pro)>l:continue
   if min(vals.values())>=0:succ[a]=b
   elif max(vals.values())<=0:succ[b]=a
  assert len(succ)>=3 and set(succ)==set(succ.values())
  a=min(succ);cy=[a];b=succ[a]
  while b!=a:
   assert b not in cy;cy.append(b);b=succ[b]
  assert len(cy)==len(succ);faces.append(cy)
 edgefaces={};tri=[]
 for fi,cy in enumerate(faces):
  for a,b in zip(cy,cy[1:]+cy[:1]):edgefaces.setdefault(tuple(sorted((a,b))),[]).append((fi,a,b))
  # Last-vertex fan, not the first-vertex fan used by the other auditor.
  tri += [(cy[-1],cy[k],cy[k+1]) for k in range(len(cy)-2)]
 active=sorted({a for cy in faces for a in cy});adj={a:set() for a in active}
 for (a,b),r in edgefaces.items():
  assert len(r)==2 and r[0][1:]==r[1][1:][::-1];adj[a].add(b);adj[b].add(a)
 assert len(active)-len(edgefaces)+len(faces)==2
 seen=set();queue=[active[0]]
 while queue:
  a=queue.pop()
  if a not in seen:seen.add(a);queue.extend(adj[a]-seen)
 assert seen==set(active)
 # Mean-of-input reference, strictly inside this full-dimensional convex hull.
 cnt=len(I);B=tuple(sum(p[k] for p in I) for k in range(3));J=[minus(mul(p,cnt),B) for p in I]
 W=0;M=ZERO
 for a,b,c in tri:
  d=determinant(J[a],J[b],J[c]);assert d>0;W+=d;M=plus(M,mul(plus(plus(J[a],J[b]),J[c]),d))
 volume=Q(W,6*(cnt*D)**3)
 centroid=tuple(Q(B[k],cnt*D)+Q(M[k],4*W*cnt*D) for k in range(3))
 first=tuple(volume*c for c in centroid)
 X=[tuple(Q(x,D) for x in p) for p in I];Z=[minus(p,centroid) for p in X]
 vc=Q(0);mc=ZERO
 for a,b,c in tri:
  d=determinant(Z[a],Z[b],Z[c]);assert d>0;vc+=d/6;mc=plus(mc,mul(plus(plus(Z[a],Z[b]),Z[c]),d/24))
 assert vc==volume and mc==ZERO
 S=[];Sw=[];U=[];Uw=[];H=[];Hw=[];primitives=0
 for fi,cy in enumerate(faces):
  n=keys[fi][:3];h=Q(keys[fi][3],D)
  foot=plus(centroid,mul(n,(h-inner(n,centroid))/inner(n,n)))
  v=[inner(n,outer(minus(X[b],X[a]),minus(foot,X[a]))) for a,b in zip(cy,cy[1:]+cy[:1])]
  if min(v)>0:S.append(fi)
  elif min(v)>=0:Sw.append(fi)
 for a in active:
  # Incident-edge generators of the tangent cone suffice; no all-point test here.
  vals=[inner(Z[a],minus(X[b],X[a])) for b in adj[a]]
  if max(vals)<0:U.append(a)
  elif max(vals)<=0:Uw.append(a)
 for (a,b),rr in sorted(edgefaces.items()):
  e=minus(X[b],X[a]);l=inner(e,e);t=-inner(Z[a],e)/l
  p=plus(Z[a],mul(e,t));n=keys[rr[0][0]][:3];nn=keys[rr[1][0]][:3];c=outer(n,nn);cc=inner(c,c);assert cc>0
  alpha=inner(outer(p,nn),c)/cc;beta=inner(outer(n,p),c)/cc
  assert p==plus(mul(n,alpha),mul(nn,beta))
  vals=(t,1-t,alpha,beta)
  if min(vals)>0:H.append([a,b])
  elif min(vals)>=0:Hw.append([a,b])
  pa=inner(Z[a],e);pb=-inner(Z[b],e)
  edge_sides=[]
  for fi,i,k in rr:
   normal=keys[fi][:3];edge_sides.append(inner(normal,outer(Z[i],minus(X[k],X[i]))))
  primitives+=sum(v==0 for v in (pa,pb,*edge_sides))
 return dict(input_vertex_count=len(I),V=len(active),E=len(edgefaces),F=len(faces),active_input_indices=active,maximal_faces=faces,true_edges=[list(e) for e in sorted(edgefaces)],primitive_support_planes=[list(k) for k in keys],counts=[len(S),len(U),len(H)],weak=[len(Sw),len(Uw),len(Hw)],stable_faces=[faces[i] for i in S],unstable_vertices=U,saddle_edges=H,weak_faces=Sw,weak_vertices=Uw,weak_edges=Hw,true_edge_primitive_zeros=primitives,volume=str(volume),raw_first_moments=list(map(str,first)),raw_centroid=list(map(str,centroid)),centred_first_moments=list(map(str,mc)),integration_triangles=tri)
if __name__=='__main__':
 p=json.loads(Path(sys.argv[1]).read_text());r=audit(p['I'],p['D']);raw=json.dumps(r,sort_keys=True,separators=(',',':')).encode();out=sys.argv[2] if len(sys.argv)>2 else 'audit_B.json';Path(out).write_bytes(raw)
 print(out,len(raw),hashlib.sha256(raw).hexdigest());print('EXACT_B',r['V'],r['E'],r['F'],r['counts'],r['weak'],r['true_edge_primitive_zeros'])
 if len(sys.argv)>3:
  a=json.loads(Path(sys.argv[3]).read_text())
  for k in r:
   if k!='integration_triangles':assert a[k]==r[k],(k,a[k],r[k])
  print('ALL_COMMON_FIELDS_EQUAL')
