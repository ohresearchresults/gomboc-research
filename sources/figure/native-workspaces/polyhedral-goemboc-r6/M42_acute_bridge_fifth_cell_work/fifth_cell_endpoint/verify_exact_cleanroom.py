#!/usr/bin/env python3
"""Independent standard-library exact reconstruction of the M42 double-rail fifth-cell endpoint."""
from __future__ import annotations
from fractions import Fraction as Q
from collections import defaultdict
from pathlib import Path
import csv,json,math,sys,time
R=Path(__file__).resolve().parent;CERT=json.load(open(R/'certificate.json'));S=int(CERT['scale'])
def sub(a,b):return (a[0]-b[0],a[1]-b[1],a[2]-b[2])
def add(a,b):return (a[0]+b[0],a[1]+b[1],a[2]+b[2])
def mul(a,t):return (a[0]*t,a[1]*t,a[2]*t)
def dot(a,b):return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def n2(a):return dot(a,a)
def gcdall(xs):
 g=0
 for x in xs:g=math.gcd(g,abs(int(x)))
 return g
def canon(n,h):
 g=gcdall((*n,h));n=tuple(z//g for z in n);h//=g
 if next(z for z in (*n,h) if z)<0:n=tuple(-z for z in n);h=-h
 return (*n,h)
def qs(x):x=Q(x);return f'{x.numerator}/{x.denominator}'
rows={};reported_active=[];reported_inactive=[]
for r in csv.DictReader(open(R/'coordinates_all_exact.csv')):
 i=int(r['source_id']);assert int(r['denominator'])==S;rows[i]=tuple(int(r[k]) for k in ('x_int','y_int','z_int'));(reported_active if int(r['active']) else reported_inactive).append(i)
assert len(rows)==CERT['input_rows']==119
cycles=json.load(open(R/'face_cycles.json'));assert len(cycles)==104
# stored faces exact
planes=[];stored={}
for fi,c in enumerate(cycles):
 assert len(c)>=3 and len(set(c))==len(c);a,b,z=(rows[i] for i in c[:3]);n=cross(sub(b,a),sub(z,a));assert n!=(0,0,0);h=dot(n,a)
 vals={i:dot(n,p)-h for i,p in rows.items()};pos=any(v>0 for v in vals.values());neg=any(v<0 for v in vals.values());assert not(pos and neg),(fi,min(vals.values()),max(vals.values()))
 if pos:n=tuple(-v for v in n);h=-h;vals={i:-v for i,v in vals.items()}
 assert all(v<=0 for v in vals.values());cop={i for i,v in vals.items() if v==0};assert cop==set(c),(fi,c,sorted(cop))
 area=(0,0,0)
 for u,v in zip(c,c[1:]+c[:1]):area=add(area,cross(rows[u],rows[v]))
 assert dot(area,n)>0
 for j in range(len(c)):
  u,v,w=(rows[c[j-1]],rows[c[j]],rows[c[(j+1)%len(c)]])
  assert dot(cross(sub(v,u),sub(w,v)),n)>0,(fi,j)
 g=gcdall((*n,h));n=tuple(v//g for v in n);h//=g;key=canon(n,h);assert key not in stored;stored[key]=fi;planes.append((n,h))
# exhaustive all unique triples
ids=sorted(rows);pts=[rows[i] for i in ids];found={};t0=time.time()
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
   key=canon(n,h);cop={i for i,p in rows.items() if dot(n,p)==h};found.setdefault(key,cop);assert found[key]==cop
assert set(found)==set(stored),(len(found),len(stored),set(found)-set(stored),set(stored)-set(found))
for key,cop in found.items():assert cop==set(cycles[stored[key]])
# topology
EF=defaultdict(list);N=defaultdict(set)
for fi,c in enumerate(cycles):
 for a,b in zip(c,c[1:]+c[:1]):e=tuple(sorted((a,b)));EF[e].append(fi);N[a].add(b);N[b].add(a)
assert len(EF)==163 and all(len(z)==2 for z in EF.values());active=sorted(set().union(*(set(c) for c in cycles)));inactive=sorted(set(rows)-set(active));assert active==reported_active==CERT['active_rows'];assert inactive==reported_inactive==CERT['inactive_rows'];assert len(active)==61 and len(active)-len(EF)+len(cycles)==2
adj=defaultdict(set)
for x,y in EF.values():adj[x].add(y);adj[y].add(x)
seen={0};stack=[0]
while stack:
 a=stack.pop()
 for b in adj[a]:
  if b not in seen:seen.add(b);stack.append(b)
assert len(seen)==len(cycles)
# mass and centroid
D6=0;Mint=[0,0,0]
for c in cycles:
 for j in range(1,len(c)-1):
  a,b,z=(rows[i] for i in (c[0],c[j],c[j+1]));d=det(a,b,z);D6+=d
  for k in range(3):Mint[k]+=d*(a[k]+b[k]+z[k])
assert D6>0;V=Q(D6,6*S**3);C=tuple(Q(Mint[k],4*D6*S) for k in range(3));Mom=tuple(Q(Mint[k],24*S**4) for k in range(3));assert qs(V)==CERT['volume_exact'];assert [qs(z) for z in C]==CERT['centroid_unshifted_exact'];assert [qs(z) for z in Mom]==CERT['first_moments_unshifted_exact'];assert all(Mom[k]==V*C[k] for k in range(3));X={i:tuple(Q(rows[i][k],S)-C[k] for k in range(3)) for i in active}
# exact mechanics
stable=[];FC={}
for fi,c in enumerate(cycles):
 n=tuple(Q(z) for z in planes[fi][0]);h=dot(n,X[c[0]]);assert h>0;foot=mul(n,h/n2(n));ref=tuple(sum((X[i][k] for i in c),Q(0))/len(c) for k in range(3));vals=[]
 for a,b in zip(c,c[1:]+c[:1]):
  v=dot(cross(sub(X[b],X[a]),sub(foot,X[a])),n)
  if dot(cross(sub(X[b],X[a]),sub(ref,X[a])),n)<0:v=-v
  vals.append(v)
 FC[fi]=vals
 if min(vals)>0:stable.append(fi)
assert {frozenset(cycles[i]) for i in stable}=={frozenset(range(17)),frozenset({198,224,258})}
SUP={};unstable=[]
for i in active:
 vals={j:-dot(X[i],sub(X[j],X[i])) for j in sorted(N[i])};assert vals and all(v!=0 for v in vals.values());SUP[i]=vals
 if min(vals.values())>0:unstable.append(i)
assert unstable==[8]
EC={};saddles=[]
for e,inc in sorted(EF.items()):
 i,j=e;d=sub(X[j],X[i]);t=-dot(X[i],d)/n2(d);p=add(X[i],mul(d,t));n1=tuple(Q(z) for z in planes[inc[0]][0]);n2v=tuple(Q(z) for z in planes[inc[1]][0]);aa=n2(n1);bb=dot(n1,n2v);cc=n2(n2v);r1=dot(p,n1);r2=dot(p,n2v);den=aa*cc-bb*bb;assert den>0;b1=(r1*cc-r2*bb)/den;b2=(r2*aa-r1*bb)/den;vals=(t,Q(1)-t,b1,b2);EC[e]=vals
 if min(vals)>0:saddles.append(e)
assert saddles==[(229,247)] and [len(stable),len(unstable),len(saddles)]==CERT['class']==[2,1,1] and len(stable)+len(unstable)-len(saddles)==2
# predecessor feature deletion
for i in CERT['old_fourth_packet_rows_now_inactive']:assert i in inactive
for e in [(135,224),(183,223),(226,227)]:assert e not in EF
assert not any(set(c)=={195,223,224} for c in cycles)
# exact rails, graph connected
bridge=json.load(open(R/'acute_bridge_graph.json'))
for rail in [bridge['short_rail'],bridge['long_rail']]:
 for z in rail['steps']:
  a,b=z['from'],z['to'];assert tuple(sorted((a,b))) in EF;raw=dot(X[a],sub(X[b],X[a]));pd=dot(X[a],X[b]);assert raw>0 and pd>0;assert qs(raw)==z['directed_support_exact'];assert qs(pd)==z['positive_dot_exact']
G={i:set() for i in active};pos=[];non=[]
for a,b in EF:
 z=dot(X[a],X[b]);(pos if z>0 else non).append((a,b,z))
 if z>0:G[a].add(b);G[b].add(a)
seen={active[0]};stack=[active[0]]
while stack:
 a=stack.pop()
 for b in G[a]:
  if b not in seen:seen.add(b);stack.append(b)
assert seen==set(active);assert len(pos)==134 and len(non)==29
# exact cell atlas
complexrec=json.load(open(R/'fifth_cell_complex.json'))
def verify_cell(z):
 a,b=z['true_edge'];u,v=z['apices'];dp=det(X[u],X[a],X[b]);dm=det(X[v],X[a],X[b]);assert dp*dm<0;assert [qs(dp),qs(dm)]==z['apex_determinants_exact'];t=Q(z['segment_parameter_exact']);l0,la,lb=(Q(x) for x in z['equator_barycentric_exact']);assert min(t,1-t,l0,la,lb)>0 and l0+la+lb==1;lhs=add(X[u],mul(sub(X[v],X[u]),t));rhs=add(mul(X[a],la),mul(X[b],lb));assert lhs==rhs
for z in complexrec['all_strict_convex_edge_star_bipyramids']:verify_cell(z)
assert len(complexrec['all_strict_convex_edge_star_bipyramids'])==64 and complexrec['new_row_touching_bipyramids']==58
closure=complexrec['closure_face_ids'];ced=defaultdict(list)
for fi in closure:
 c=cycles[fi];assert len(c)==3 and set(c)&set(range(229,265));assert det(X[c[0]],X[c[1]],X[c[2]])!=0
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
assert seen==set(closure) and len(closure)==95
# ledgers cross-check
for r in csv.DictReader(open(R/'vertices_mechanics.csv')):
 i=int(r['vertex']);assert json.loads(r['supports_exact_json'])=={str(j):qs(v) for j,v in SUP[i].items()}
for r in csv.DictReader(open(R/'edges_four_component_audit.csv')):
 e=(int(r['u']),int(r['v']));assert [r[k] for k in ('t_exact','one_minus_t_exact','beta1_exact','beta2_exact')]==[qs(v) for v in EC[e]]
print('PASS exhaustive exact supporting-triple reconstruction',len(found),'faces in',time.time()-t0,'seconds')
print('PASS connected closed hull f-vector',len(active),len(EF),len(cycles),'Euler',len(active)-len(EF)+len(cycles))
print('PASS exact volume',qs(V));print('PASS exact own centroid',*[qs(z) for z in C]);print('PASS zero translated first moments')
print('PASS exhaustive exact class',len(stable),len(unstable),len(saddles),'stable',[cycles[i] for i in stable],'unstable',unstable,'saddles',saddles)
print('PASS both exact 19-edge monotone rails, connected positive-dot graph',len(pos),len(non))
print('PASS 64 strict convex edge-star bipyramids, 58 touching new rows, 95-face connected closure')
print('PASS predecessor packet deletion and residual single S-H pair')
