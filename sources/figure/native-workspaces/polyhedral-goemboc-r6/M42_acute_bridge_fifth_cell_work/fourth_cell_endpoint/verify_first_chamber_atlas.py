#!/usr/bin/env python3
"""Independent standard-library exact verifier for the M42 fourth-cell atlas.

The endpoint itself is exhaustively reconstructed by verify_exact_cleanroom.py.
Here every stored adjacent chamber is independently checked as a strict exact
closed convex boundary: exact support against all 140 inputs, connected
2-manifold incidence, exact mass/own centroid, and every face/vertex/four-
component edge cone.  Exact determinant formulas verify both incidence walls,
and exact mechanics on the appropriate adjacent incidence cells verifies both
width-1e-13 U-H-U brackets.
"""
from __future__ import annotations
from fractions import Fraction as Q
from collections import defaultdict
from pathlib import Path
import csv,json,math
R=Path(__file__).resolve().parent;A=json.load(open(R/'first_chamber_atlas.json'))

def qs(x):return f'{x.numerator}/{x.denominator}'
def sub(a,b):return tuple(a[k]-b[k] for k in range(3))
def add(a,b):return tuple(a[k]+b[k] for k in range(3))
def mul(a,t):return tuple(a[k]*t for k in range(3))
def dot(a,b):return sum(a[k]*b[k] for k in range(3))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def n2(a):return dot(a,a)
base={};S=None
with open(R/'input_rows_common_lattice.csv') as f:
 for r in csv.DictReader(f):
  d=int(r['denominator']);S=d if S is None else S;assert d==S;base[int(r['source_id'])]=tuple(int(r[k]) for k in ('x_int','y_int','z_int'))

def controlled(a,b):
 L=math.lcm(a.denominator,b.denominator);rows={i:tuple(z*L for z in p) for i,p in base.items()};scale=S*L
 rows[223]=tuple(z*a.numerator//a.denominator for z in rows[223]);rows[227]=tuple(z*b.numerator//b.denominator for z in rows[227])
 assert all(Q(rows[i][k],scale)==Q(base[i][k],S)*(a if i==223 else b if i==227 else 1) for i in rows for k in range(3))
 return rows,scale

def reconstruct(a,b,cycles):
 rows,L=controlled(a,b);planes=[]
 for fi,c in enumerate(cycles):
  x,y,z=(rows[i] for i in c[:3]);n=cross(sub(y,x),sub(z,x));assert n!=(0,0,0);h=dot(n,x);vals={i:dot(n,p)-h for i,p in rows.items()};pos=any(v>0 for v in vals.values());neg=any(v<0 for v in vals.values());assert not(pos and neg),(fi,min(vals.values()),max(vals.values()))
  if pos:n=tuple(-v for v in n);h=-h;vals={i:-v for i,v in vals.items()}
  assert all(v<=0 for v in vals.values());assert {i for i,v in vals.items() if v==0}==set(c)
  area=(0,0,0)
  for u,v in zip(c,c[1:]+c[:1]):area=add(area,cross(rows[u],rows[v]))
  assert dot(area,n)>0
  planes.append((n,h))
 EF=defaultdict(list)
 for fi,c in enumerate(cycles):
  for u,v in zip(c,c[1:]+c[:1]):EF[tuple(sorted((u,v)))].append(fi)
 assert all(len(fs)==2 for fs in EF.values())
 active=sorted(set().union(*(set(c) for c in cycles)));inactive=sorted(set(rows)-set(active));assert len(active)-len(EF)+len(cycles)==2
 # connected face adjacency
 adj=defaultdict(set)
 for x,y in EF.values():adj[x].add(y);adj[y].add(x)
 seen={0};q=[0]
 while q:
  u=q.pop()
  for v in adj[u]:
   if v not in seen:seen.add(v);q.append(v)
 assert len(seen)==len(cycles)
 D6=0;M=[0,0,0]
 for c in cycles:
  for j in range(1,len(c)-1):
   x,y,z=(rows[i] for i in (c[0],c[j],c[j+1]));d=det(x,y,z);D6+=d
   for k in range(3):M[k]+=d*(x[k]+y[k]+z[k])
 assert D6>0;V=Q(D6,6*L**3);C=tuple(Q(M[k],4*D6*L) for k in range(3));Mom=tuple(Q(M[k],24*L**4) for k in range(3));assert all(Mom[k]==V*C[k] for k in range(3))
 X={i:tuple(Q(rows[i][k],L)-C[k] for k in range(3)) for i in active}
 stable=[];face_raw={}
 for fi,c in enumerate(cycles):
  n=tuple(Q(v) for v in planes[fi][0]);h=dot(n,X[c[0]]);foot=mul(n,h/n2(n));ref=tuple(sum((X[i][k] for i in c),Q(0))/len(c) for k in range(3));vals=[]
  for u,v in zip(c,c[1:]+c[:1]):
   z=dot(cross(sub(X[v],X[u]),sub(foot,X[u])),n)
   if dot(cross(sub(X[v],X[u]),sub(ref,X[u])),n)<0:z=-z
   vals.append(z)
  face_raw[fi]=vals
  if min(vals)>0:stable.append(fi)
 N=defaultdict(set)
 for u,v in EF:N[u].add(v);N[v].add(u)
 SUP={};unst=[]
 for i in active:
  vals={j:-dot(X[i],sub(X[j],X[i])) for j in sorted(N[i])};SUP[i]=vals
  if min(vals.values())>0:unst.append(i)
 eraw={};sadd=[]
 for e,inc in sorted(EF.items()):
  i,j=e;d=sub(X[j],X[i]);t=-dot(X[i],d)/n2(d);p=add(X[i],mul(d,t));n1=tuple(Q(v) for v in planes[inc[0]][0]);n2v=tuple(Q(v) for v in planes[inc[1]][0]);aa=n2(n1);bb=dot(n1,n2v);cc=n2(n2v);r1=dot(p,n1);r2=dot(p,n2v);den=aa*cc-bb*bb;assert den>0;b1=(r1*cc-r2*bb)/den;b2=(r2*aa-r1*bb)/den;vals=(t,Q(1)-t,b1,b2);eraw[e]=vals
  if min(vals)>0:sadd.append(e)
 return {'rows':rows,'L':L,'cycles':cycles,'EF':EF,'active':active,'inactive':inactive,'V':V,'C':C,'X':X,'stable':stable,'face_raw':face_raw,'SUP':SUP,'unst':unst,'eraw':eraw,'sadd':sadd}

cellmap={c['cell_id']:c for c in A['cells']};recs={}
for cell in A['cells']:
 R0=reconstruct(Q(cell['a_exact']),Q(cell['b_exact']),cell['face_cycles']);recs[cell['cell_id']]=R0
 assert [len(R0['active']),len(R0['EF']),len(R0['cycles'])]==cell['f_vector'];assert R0['active']==cell['active_rows'];assert R0['inactive']==cell['inactive_rows'];assert qs(R0['V'])==cell['volume_exact'];assert [qs(z) for z in R0['C']]==cell['centroid_unshifted_exact']
 assert [len(R0['stable']),len(R0['unst']),len(R0['sadd'])]==cell['class'];assert [R0['cycles'][i] for i in R0['stable']]==[z['cycle'] for z in cell['stable_faces']];assert R0['unst']==[z['vertex'] for z in cell['unstable_vertices']];assert R0['sadd']==[tuple(z['edge']) for z in cell['saddle_edges']]
 assert any(set(R0['cycles'][i])==set(range(17)) for i in R0['stable']) and 8 in R0['unst'];assert (226,227) in R0['EF']
 for i,j in ((226,227),(227,226)):assert all(v>0 for k,v in R0['SUP'][i].items() if k!=j)
 assert R0['SUP'][226][227]+R0['SUP'][227][226]==n2(sub(R0['X'][227],R0['X'][226]))>0
 print('PASS exact atlas cell',cell['cell_id'],'f-vector',cell['f_vector'],'class',cell['class'])

def orient(rows,a,b,c,d):return det(sub(rows[b],rows[a]),sub(rows[c],rows[a]),sub(rows[d],rows[a]))
def linear_root(moving,circuit):
 rows,L=controlled(Q(1),Q(1));r0=dict(rows);r0[moving]=(0,0,0);f0=orient(r0,*circuit);f1=orient(rows,*circuit);return -Q(f0,f1-f0)
for w in A['exact_incidence_walls']:
 moving=223 if 223 in w['circuit'] else 227;assert qs(linear_root(moving,w['circuit']))==w['root_exact']
 if moving==223:L0,H0=recs['A0B3'],recs['A1B3']
 else:L0,H0=recs['A1B1'],recs['A1B2']
 removed=sorted([list(e) for e in L0['EF'] if e not in H0['EF']]);added=sorted([list(e) for e in H0['EF'] if e not in L0['EF']]);assert removed==w['removed_edges'] and added==w['added_edges']
 print('PASS exact incidence wall',w['description'],w['root_exact'])

# The birth bracket lies in pre-incidence topology A1B0; the death bracket lies
# in post-incidence topology A1B2.  Reuse only their exact cycle sets, not their
# mechanical data, and recompute mass/cones at both bracket endpoints.
for w in A['isolated_mechanical_walls']:
 lo=Q(w['lo_exact']);hi=Q(w['hi_exact']);assert hi-lo==Q(1,10**13);template=cellmap['A1B0']['face_cycles'] if 'birth' in w['description'] else cellmap['A1B2']['face_cycles'];L0=reconstruct(Q(1),lo,template);H0=reconstruct(Q(1),hi,template)
 aL,bL=L0['SUP'][226][227],L0['SUP'][227][226];aH,bH=H0['SUP'][226][227],H0['SUP'][227][226]
 assert qs(aL)==w['sigma_226_to_227_lo_exact'];assert qs(aH)==w['sigma_226_to_227_hi_exact'];assert qs(bL)==w['sigma_227_to_226_lo_exact'];assert qs(bH)==w['sigma_227_to_226_hi_exact']
 if 'birth' in w['description']:assert bL<0<bH
 else:assert aL>0>aH
 print('PASS isolated exact mechanical wall',w['description'],w['lo_exact'],w['hi_exact'])
print('PASS all eight exact first outgoing chambers, both incidence flips and both width-1e-13 U-H-U wall brackets; no chamber is (1,1,0)')
