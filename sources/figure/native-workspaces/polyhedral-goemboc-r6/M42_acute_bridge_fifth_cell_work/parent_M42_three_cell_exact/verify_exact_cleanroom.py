#!/usr/bin/env python3
"""Independent exact verification of the M42 three-cell endpoint.

Standard-library only. Does not import the builder/generator. Enumerates every
supporting plane from all unique input triples, proves the stored maximal-face
lattice is the complete exact hull, recomputes mass/centroid, audits every
face, actual vertex and all four edge-cone components, proves the transferred
edge obstruction, unique-farthest target, and the three nonsimplicial cells.
"""
from __future__ import annotations
from fractions import Fraction as Q
from collections import defaultdict
from pathlib import Path
import csv,json,itertools,math
R=Path(__file__).resolve().parent
CERT=json.load(open(R/'certificate.json'));S=int(CERT['scale'])
def sub(a,b):return tuple(a[k]-b[k] for k in range(3))
def add(a,b):return tuple(a[k]+b[k] for k in range(3))
def mul(a,t):return tuple(a[k]*t for k in range(3))
def dot(a,b):return sum(a[k]*b[k] for k in range(3))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def n2(a):return dot(a,a)
def gcdall(xs):
 g=0
 for x in xs:g=math.gcd(g,abs(int(x)))
 return g
def canon(n,h):
 g=gcdall((*n,h));n=tuple(int(z)//g for z in n);h=int(h)//g
 if next(z for z in (*n,h) if z)<0:n=tuple(-z for z in n);h=-h
 return (*n,h)
def qstr(x):return f'{x.numerator}/{x.denominator}'
# Inputs
rows={};reported_active=[];reported_inactive=[]
with open(R/'coordinates_all_exact.csv') as f:
 for r in csv.DictReader(f):
  i=int(r['source_id']);assert int(r['denominator'])==S
  rows[i]=(int(r['x_num']),int(r['y_num']),int(r['z_num']))
  (reported_active if int(r['active']) else reported_inactive).append(i)
assert len(rows)==CERT['input_rows']==134
cycles=json.load(open(R/'face_cycles.json'));assert len(cycles)==166
# Stored face planes: exact support, exact coplanar set, orientation and polygon convexity.
planes=[];stored_keys={}
for fi,c in enumerate(cycles):
 assert len(c)>=3 and len(set(c))==len(c)
 a,b,z=(rows[i] for i in c[:3]);n=cross(sub(b,a),sub(z,a));assert n!=(0,0,0);h=dot(n,a)
 vals={i:dot(n,p)-h for i,p in rows.items()};pos=any(v>0 for v in vals.values());neg=any(v<0 for v in vals.values());assert not(pos and neg),(fi,min(vals.values()),max(vals.values()))
 if pos:n=tuple(-v for v in n);h=-h;vals={i:-v for i,v in vals.items()}
 assert all(v<=0 for v in vals.values())
 cop={i for i,v in vals.items() if v==0};assert cop==set(c),(fi,c,sorted(cop))
 area=(0,0,0)
 for u,v in zip(c,c[1:]+c[:1]):area=add(area,cross(rows[u],rows[v]))
 assert dot(area,n)>0
 # strict convex cyclic order in face plane
 for j in range(len(c)):
  u,v,w=(rows[c[j-1]],rows[c[j]],rows[c[(j+1)%len(c)]])
  assert dot(cross(sub(v,u),sub(w,v)),n)>0,(fi,j)
 g=gcdall((*n,h));n=tuple(v//g for v in n);h//=g
 key=canon(n,h);assert key not in stored_keys;stored_keys[key]=fi;planes.append((n,h))
# Exhaustive V->H reconstruction from every unique input triple.
coord_to_ids=defaultdict(list)
for i,p in rows.items():coord_to_ids[p].append(i)
pts=list(coord_to_ids);found={}
for ia in range(len(pts)-2):
 a=pts[ia]
 for ib in range(ia+1,len(pts)-1):
  ab=sub(pts[ib],a)
  for ic in range(ib+1,len(pts)):
   n=cross(ab,sub(pts[ic],a))
   if n==(0,0,0):continue
   h=dot(n,a);sg=0;ok=True
   for p in pts:
    v=dot(n,p)-h
    if v:
     s=1 if v>0 else -1
     if sg and s!=sg:ok=False;break
     sg=s
   if not ok:continue
   if sg>0:n=tuple(-v for v in n);h=-h
   key=canon(n,h)
   cop={i for i,p in rows.items() if dot(n,p)==h}
   found.setdefault(key,cop);assert found[key]==cop
assert set(found)==set(stored_keys),(len(found),len(stored_keys),len(set(found)-set(stored_keys)),len(set(stored_keys)-set(found)))
for key,cop in found.items():assert cop==set(cycles[stored_keys[key]])
# Actual boundary/edges/manifold.
EF=defaultdict(list)
for fi,c in enumerate(cycles):
 for a,b in zip(c,c[1:]+c[:1]):EF[tuple(sorted((a,b)))].append(fi)
assert len(EF)==256 and all(len(v)==2 for v in EF.values())
active=sorted(set().union(*(set(c) for c in cycles)));inactive=sorted(set(rows)-set(active))
assert active==CERT['active_rows']==reported_active;assert inactive==CERT['inactive_rows']==reported_inactive
assert len(active)==92 and len(active)-len(EF)+len(cycles)==2
# Connected face adjacency.
adj=defaultdict(set)
for fs in EF.values():adj[fs[0]].add(fs[1]);adj[fs[1]].add(fs[0])
seen={0};stack=[0]
while stack:
 a=stack.pop()
 for b in adj[a]:
  if b not in seen:seen.add(b);stack.append(b)
assert len(seen)==len(cycles)
# Exact mass and own centroid.
D6=0;M=[0,0,0]
for c in cycles:
 for j in range(1,len(c)-1):
  a,b,z=(rows[i] for i in (c[0],c[j],c[j+1]));d=det(a,b,z);D6+=d
  for k in range(3):M[k]+=d*(a[k]+b[k]+z[k])
assert D6>0
V=Q(D6,6*S**3);C=tuple(Q(M[k],4*D6*S) for k in range(3));Mom=tuple(Q(M[k],24*S**4) for k in range(3))
assert qstr(V)==CERT['volume_exact'];assert [qstr(z) for z in C]==CERT['centroid_unshifted_exact'];assert [qstr(z) for z in Mom]==CERT['first_moments_unshifted_exact'];assert all(Mom[k]-V*C[k]==0 for k in range(3))
X={i:tuple(Q(rows[i][k],S)-C[k] for k in range(3)) for i in active}
# Full face audit.
stable=[];face_components={}
for fi,c in enumerate(cycles):
 n=tuple(Q(v) for v in planes[fi][0]);h=dot(n,X[c[0]]);foot=mul(n,h/n2(n));ref=tuple(sum((X[i][k] for i in c),Q(0))/len(c) for k in range(3));vals=[]
 for a,b in zip(c,c[1:]+c[:1]):
  v=dot(cross(sub(X[b],X[a]),sub(foot,X[a])),n)
  if dot(cross(sub(X[b],X[a]),sub(ref,X[a])),n)<0:v=-v
  vals.append(v)
 face_components[fi]=vals
 if min(vals)>0:stable.append(fi)
assert stable==[x['face'] for x in CERT['stable_faces']]
assert {frozenset(cycles[i]) for i in stable}=={frozenset(range(17)),frozenset({201,220,221})}
# Full vertex audit.
N=defaultdict(set)
for a,b in EF:N[a].add(b);N[b].add(a)
SUP={};unstable=[]
for i in active:
 vals={j:-dot(X[i],sub(X[j],X[i])) for j in sorted(N[i])};SUP[i]=vals
 if min(vals.values())>0:unstable.append(i)
assert unstable==[8,153]==[x['vertex'] for x in CERT['unstable_vertices']]
# Full four-component edge audit.
edge_components={};saddles=[]
for e,inc in sorted(EF.items()):
 i,j=e;d=sub(X[j],X[i]);t=-dot(X[i],d)/n2(d);p=add(X[i],mul(d,t));n1=tuple(Q(v) for v in planes[inc[0]][0]);n2v=tuple(Q(v) for v in planes[inc[1]][0]);aa=n2(n1);bb=dot(n1,n2v);cc=n2(n2v);r1=dot(p,n1);r2=dot(p,n2v);den=aa*cc-bb*bb;assert den>0;b1=(r1*cc-r2*bb)/den;b2=(r2*aa-r1*bb)/den;vals=(t,Q(1)-t,b1,b2);edge_components[e]=vals
 if min(vals)>0:saddles.append(e)
assert saddles==[(130,222),(176,182)]==[tuple(x['edge']) for x in CERT['saddle_edges']]
assert [len(stable),len(unstable),len(saddles)]==CERT['class']==[2,2,2];assert len(stable)+len(unstable)-len(saddles)==2
# Old core and superlevel packet absorption / old channels.
for i in CERT['absorbed_rows']+CERT['old_absorbed_rows_from_predecessor']:assert i in inactive
for e in CERT['absent_old_edges']:assert tuple(sorted(e)) not in EF
# Exact external-positive obstruction on (153,154).
assert (153,154) in EF
for i,j in ((153,154),(154,153)):
 assert all(v>0 for k,v in SUP[i].items() if k!=j)
A=SUP[153][154];B=SUP[154][153];rhs=n2(sub(X[154],X[153]));assert A+B==rhs and rhs>0
obs=CERT['obstruction'];assert obs['edge']==[153,154];assert qstr(A)==obs['mutual_A'];assert qstr(B)==obs['mutual_B'];assert qstr(rhs)==obs['sum_squared_edge'];assert all(v>0 for v in SUP[8].values())
# Exact unique-farthest target.
rad={i:n2(X[i]) for i in active};order=sorted(active,key=lambda i:rad[i],reverse=True);assert order[0]==8 and all(rad[8]>rad[i] for i in active if i!=8)
assert CERT['radial_order']['target_unique_farthest']
# Three triangular-bipyramidal cells sharing interior edge O-M.
rec=json.load(open(R/'three_cell_complex.json'));Mpt=tuple(Q(z) for z in rec['M_exact']);O=(Q(0),Q(0),Q(0));central=next(fi for fi,c in enumerate(cycles) if set(c)=={220,221,222});assert set(cycles[central])=={220,221,222}
for cell in rec['cells']:
 _,u,v=cell['equator'];p=cell['boundary_apex'];e=tuple(sorted((u,v)));assert central in EF[e];other=EF[e][0] if EF[e][1]==central else EF[e][1];assert set(cycles[other])=={u,v,p}
 dc=det(Mpt,X[u],X[v]);da=det(X[p],X[u],X[v]);assert dc*da<0;assert qstr(dc)==cell['central_tetra_determinant'];assert qstr(da)==cell['adjacent_tetra_determinant']
 t=Q(cell['segment_intersection']['t_M_to_p']);al=Q(cell['segment_intersection']['alpha_u']);be=Q(cell['segment_intersection']['beta_v']);ow=Q(cell['segment_intersection']['origin_weight']);assert 0<t<1 and al>0 and be>0 and ow>0 and al+be+ow==1
 lhs=add(Mpt,mul(sub(X[p],Mpt),t));rhspt=add(mul(X[u],al),mul(X[v],be));assert lhs==rhspt
closure=rec['closure_face_ids'];assert len(closure)==rec['closure_incident_faces']
ced=defaultdict(list)
for fi in closure:
 c=cycles[fi];assert len(c)==3 and set(c)&{220,221,222};assert det(X[c[0]],X[c[1]],X[c[2]])!=0
 for a,b in zip(c,c[1:]+c[:1]):ced[tuple(sorted((a,b)))].append(fi)
cadj=defaultdict(set)
for fs in ced.values():
 for a in fs:
  for b in fs:
   if a!=b:cadj[a].add(b)
seen={closure[0]};stack=list(seen)
while stack:
 a=stack.pop()
 for b in cadj[a]:
  if b not in seen:seen.add(b);stack.append(b)
assert len(seen)==len(closure)
# Stored mechanics ledgers are byte-independent cross-checks.
with open(R/'vertices_mechanics.csv') as f:vr=list(csv.DictReader(f))
assert len(vr)==len(active)
for r in vr:
 i=int(r['vertex']);assert json.loads(r['supports_exact_json'])=={str(j):qstr(v) for j,v in SUP[i].items()}
with open(R/'edges_four_component_audit.csv') as f:er=list(csv.DictReader(f))
assert len(er)==len(EF)
for r in er:
 e=(int(r['u']),int(r['v']));assert [r[k] for k in ('t_exact','one_minus_t_exact','beta1_exact','beta2_exact')]==[qstr(v) for v in edge_components[e]]
print('PASS exhaustive exact supporting-triple V->H reconstruction:',len(found),'maximal faces')
print('PASS exact closed connected boundary and f-vector',len(active),len(EF),len(cycles),'complexity',CERT['complexity'])
print('PASS exact volume',qstr(V))
print('PASS exact centroid',*[qstr(z) for z in C])
print('PASS three exact centered first moments 0,0,0')
print('PASS exhaustive class',len(stable),len(unstable),len(saddles),'stable cycles',[cycles[i] for i in stable],'unstable',unstable,'saddles',saddles)
print('PASS complete old-core/superlevel packet absorption and all named old-channel deletions')
print('PASS external-positive true-edge obstruction (153,154); independent target 8; U>=2')
print('PASS protected vertex 8 is the unique exact global farthest vertex')
print('PASS three nondegenerate triangular-bipyramidal cells sharing interior radial edge O-M and connected closure fan')
