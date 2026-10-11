#!/usr/bin/env python3
"""Independent exact verification of the M42 fourth-cell endpoint.

Standard-library only.  This script does not import the generator/builder.  It
reconstructs every supporting plane from every unique input triple, proves the
stored maximal-face lattice is the complete exact hull, checks the connected
closed boundary, exact mass and own centroid, audits every maximal face,
actual vertex and all four components of every true-edge normal cone, and
verifies the fourth shared-interior-edge complex, transferred obstruction,
unique-farthest target, and exact acute-component graph obstruction.
"""
from __future__ import annotations
from fractions import Fraction as Q
from collections import defaultdict
from pathlib import Path
import csv,json,math
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
def qs(x):return f'{x.numerator}/{x.denominator}'

# Exact construction inputs.
rows={};reported_active=[];reported_inactive=[]
with open(R/'coordinates_all_exact.csv') as f:
 for r in csv.DictReader(f):
  i=int(r['source_id']);assert int(r['denominator'])==S
  rows[i]=(int(r['x_int']),int(r['y_int']),int(r['z_int']))
  (reported_active if int(r['active']) else reported_inactive).append(i)
assert len(rows)==CERT['input_rows']==140
cycles=json.load(open(R/'face_cycles.json'));assert len(cycles)==CERT['f_vector'][2]==148

# Exact support, exact coplanar set, winding and face-polygon convexity.
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
 assert dot(area,n)>0,(fi,c)
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
   key=canon(n,h);cop={i for i,p in rows.items() if dot(n,p)==h}
   found.setdefault(key,cop);assert found[key]==cop
assert set(found)==set(stored_keys),(len(found),len(stored_keys),len(set(found)-set(stored_keys)),len(set(stored_keys)-set(found)))
for key,cop in found.items():assert cop==set(cycles[stored_keys[key]])

# Actual true edges, closed connected 2-manifold, active/inactive status.
EF=defaultdict(list)
for fi,c in enumerate(cycles):
 for a,b in zip(c,c[1:]+c[:1]):EF[tuple(sorted((a,b)))].append(fi)
assert len(EF)==CERT['f_vector'][1]==229 and all(len(v)==2 for v in EF.values())
active=sorted(set().union(*(set(c) for c in cycles)));inactive=sorted(set(rows)-set(active))
assert active==CERT['active_rows']==reported_active;assert inactive==CERT['inactive_rows']==reported_inactive
assert len(active)==CERT['f_vector'][0]==83 and len(active)-len(EF)+len(cycles)==2
adj=defaultdict(set)
for fs in EF.values():adj[fs[0]].add(fs[1]);adj[fs[1]].add(fs[0])
seen={0};stack=[0]
while stack:
 a=stack.pop()
 for b in adj[a]:
  if b not in seen:seen.add(b);stack.append(b)
assert len(seen)==len(cycles)

# Exact mass and actual ordinary-volume centroid.
D6=0;Mint=[0,0,0]
for c in cycles:
 for j in range(1,len(c)-1):
  a,b,z=(rows[i] for i in (c[0],c[j],c[j+1]));d=det(a,b,z);D6+=d
  for k in range(3):Mint[k]+=d*(a[k]+b[k]+z[k])
assert D6>0
V=Q(D6,6*S**3);C=tuple(Q(Mint[k],4*D6*S) for k in range(3));Mom=tuple(Q(Mint[k],24*S**4) for k in range(3))
assert qs(V)==CERT['volume_exact'];assert [qs(z) for z in C]==CERT['centroid_unshifted_exact'];assert [qs(z) for z in Mom]==CERT['first_moments_unshifted_exact'];assert all(Mom[k]-V*C[k]==0 for k in range(3))
X={i:tuple(Q(rows[i][k],S)-C[k] for k in range(3)) for i in active}

# Every maximal face: perpendicular foot and all polygon boundary components.
stable=[];face_components={}
for fi,c in enumerate(cycles):
 n=tuple(Q(v) for v in planes[fi][0]);h=dot(n,X[c[0]]);assert h>0
 foot=mul(n,h/n2(n));ref=tuple(sum((X[i][k] for i in c),Q(0))/len(c) for k in range(3));vals=[]
 for a,b in zip(c,c[1:]+c[:1]):
  v=dot(cross(sub(X[b],X[a]),sub(foot,X[a])),n)
  if dot(cross(sub(X[b],X[a]),sub(ref,X[a])),n)<0:v=-v
  vals.append(v)
 face_components[fi]=vals
 if min(vals)>0:stable.append(fi)
assert stable==[z['face'] for z in CERT['stable_faces']]
assert {frozenset(cycles[i]) for i in stable}=={frozenset(range(17)),frozenset({195,224,223})}

# Every actual vertex: all adjacent-edge support components.
N=defaultdict(set)
for a,b in EF:N[a].add(b);N[b].add(a)
SUP={};unstable=[]
for i in active:
 vals={j:-dot(X[i],sub(X[j],X[i])) for j in sorted(N[i])};assert vals and all(v!=0 for v in vals.values());SUP[i]=vals
 if min(vals.values())>0:unstable.append(i)
assert unstable==[8,227]==[z['vertex'] for z in CERT['unstable_vertices']]

# Every true edge: t,1-t and both incident-normal coefficients.
edge_components={};saddles=[]
for e,inc in sorted(EF.items()):
 i,j=e;d=sub(X[j],X[i]);t=-dot(X[i],d)/n2(d);p=add(X[i],mul(d,t));n1=tuple(Q(v) for v in planes[inc[0]][0]);n2v=tuple(Q(v) for v in planes[inc[1]][0]);aa=n2(n1);bb=dot(n1,n2v);cc=n2(n2v);r1=dot(p,n1);r2=dot(p,n2v);den=aa*cc-bb*bb;assert den>0;b1=(r1*cc-r2*bb)/den;b2=(r2*aa-r1*bb)/den;vals=(t,Q(1)-t,b1,b2);edge_components[e]=vals
 if min(vals)>0:saddles.append(e)
assert saddles==[(135,224),(183,223)]==[tuple(z['edge']) for z in CERT['saddle_edges']]
assert [len(stable),len(unstable),len(saddles)]==CERT['class']==[2,2,2]
assert len(stable)+len(unstable)-len(saddles)==2

# Joint parent-packet absorption and named feature deletion.
for i in CERT['absorbed_parent_rows']:assert i in inactive
assert (153,154) not in EF and (130,222) not in EF and (176,182) not in EF
assert not any(set(c)=={201,220,221} for c in cycles)
for name in CERT['old_channel_absences']:
 a,b=(int(x) for x in name.split('_'));assert tuple(sorted((a,b))) not in EF

# Exact external-positive transferred obstruction.
assert (226,227) in EF
for i,j in ((226,227),(227,226)):
 assert all(v>0 for k,v in SUP[i].items() if k!=j)
A=SUP[226][227];B=SUP[227][226];rhs=n2(sub(X[227],X[226]));assert A+B==rhs and rhs>0
obs=CERT['obstruction'];assert obs['edge']==[226,227];assert qs(A)==obs['mutual_A_exact'];assert qs(B)==obs['mutual_B_exact'];assert qs(rhs)==obs['sum_squared_edge_exact'];assert all(v>0 for v in SUP[8].values())

# Protected vertex 8 is exact unique farthest.
rad={i:n2(X[i]) for i in active};order=sorted(active,key=lambda i:rad[i],reverse=True);assert order==CERT['radial_order']['order'];assert order[0]==8
min_gap=min(rad[8]-rad[i] for i in active if i!=8);assert min_gap>0 and qs(min_gap)==CERT['radial_order']['minimum_squared_gap_exact']

# Four linked nonsimplicial triangular-bipyramidal cells.
rec=json.load(open(R/'fourth_cell_complex.json'));M0=tuple(Q(z) for z in rec['M0_exact']);N0=tuple(Q(z) for z in rec['N0_exact']);points={'M0':M0,'N0':N0}
for cell in rec['cells']:
 _,u,v=cell['equator'];ap=points[cell['positive_apex']] if isinstance(cell['positive_apex'],str) else X[cell['positive_apex']];am=points[cell['negative_apex']] if isinstance(cell['negative_apex'],str) else X[cell['negative_apex']]
 dp=det(ap,X[u],X[v]);dm=det(am,X[u],X[v]);assert dp*dm<0
 assert qs(dp)==cell['positive_tetra_determinant_exact'];assert qs(dm)==cell['negative_tetra_determinant_exact']
 t=Q(cell['segment_parameter_exact']);l0,lu,lv=(Q(z) for z in cell['equator_barycentric_exact']);assert min(t,1-t,l0,lu,lv)>0 and l0+lu+lv==1
 lhs=add(ap,mul(sub(am,ap),t));rr=add(mul(X[u],lu),mul(X[v],lv));assert lhs==rr==tuple(Q(z) for z in cell['intersection_exact'])
closure=rec['closure_face_ids'];assert len(closure)==rec['closure_faces']
ced=defaultdict(list)
for fi in closure:
 c=cycles[fi];assert len(c)==3 and set(c)&set(rec['new_rows']);assert det(X[c[0]],X[c[1]],X[c[2]])!=0
 for a,b in zip(c,c[1:]+c[:1]):ced[tuple(sorted((a,b)))].append(fi)
cadj=defaultdict(set)
for fs in ced.values():
 for a in fs:
  for b in fs:
   if a!=b:cadj[a].add(b)
seen={closure[0]};stack=[closure[0]]
while stack:
 a=stack.pop()
 for b in cadj[a]:
  if b not in seen:seen.add(b);stack.append(b)
assert len(seen)==len(closure)
for e in rec['new_true_edges']:assert tuple(e) in EF

# Strong exact acute-component obstruction, recomputed from current graph.
G={i:set() for i in active};positive=[];nonpositive=[]
for a,b in EF:
 z=dot(X[a],X[b]);(positive if z>0 else nonpositive).append((a,b,z))
 if z>0:G[a].add(b);G[b].add(a)
un=set(active);components=[]
while un:
 s=min(un);cc={s};q=[s]
 while q:
  u=q.pop()
  for v in G[u]:
   if v not in cc:cc.add(v);q.append(v)
 un-=cc;components.append(sorted(cc))
components.sort(key=lambda c:(-len(c),c));ci={v:k for k,c in enumerate(components) for v in c}
graph=json.load(open(R/'graph_radial_obstruction.json'));assert components==graph['acute_components'];assert len(components)==2;assert ci[226]==ci[227] and ci[8]!=ci[226]
for a in components[ci[226]]:
 for b in components[ci[8]]:assert dot(X[a],X[b])<0
assert len(positive)==graph['positive_dot_true_edges'];assert len(nonpositive)==graph['nonpositive_dot_true_edges']

# Exact stored mechanics ledger cross-checks.
with open(R/'vertices_mechanics.csv') as f:vr=list(csv.DictReader(f))
assert len(vr)==len(active)
for r in vr:
 i=int(r['vertex']);assert json.loads(r['supports_exact_json'])=={str(j):qs(v) for j,v in SUP[i].items()}
with open(R/'edges_four_component_audit.csv') as f:er=list(csv.DictReader(f))
assert len(er)==len(EF)
for r in er:
 e=(int(r['u']),int(r['v']));assert [r[k] for k in ('t_exact','one_minus_t_exact','beta1_exact','beta2_exact')]==[qs(v) for v in edge_components[e]]

print('PASS exhaustive exact supporting-triple V->H reconstruction:',len(found),'maximal faces')
print('PASS exact connected closed hull and f-vector',len(active),len(EF),len(cycles),'complexity',CERT['complexity'])
print('PASS exact volume',qs(V))
print('PASS exact own centroid',*[qs(z) for z in C])
print('PASS exact three centred first moments 0,0,0')
print('PASS exhaustive class',len(stable),len(unstable),len(saddles),'stable cycles',[cycles[i] for i in stable],'unstable',unstable,'saddles',saddles)
print('PASS joint old-packet absorption and all named feature/channel deletions')
print('PASS four linked nondegenerate nonsimplicial centroid-fan cells and connected closure')
print('PASS edge (226,227) external-positive obstruction; independent target 8; U>=2')
print('PASS target 8 unique exact farthest')
print('PASS exact positive-dot graph has two components and every cross-component pair is obtuse')
