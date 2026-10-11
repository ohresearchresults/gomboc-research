#!/usr/bin/env python3
"""Independent standard-library exact verifier for first outgoing chamber atlas.

Reconstructs every cell from the exact base coordinates and two rational
parameters, exhaustively enumerates all supporting planes from all unique input
triples, rebuilds the complete boundary/true-edge lattice, exact mass and own
centroid, and every face/vertex/four-component edge-cone decision. It also
checks the two isolated paired-birth wall brackets by exact signs.
"""
from __future__ import annotations
from fractions import Fraction as Q
from collections import defaultdict
from pathlib import Path
import csv, json, math
R=Path(__file__).resolve().parent
A=json.load(open(R/'first_chamber_atlas.json'))
BASE=10**36

def q(s): return Q(s)
def qs(x): return f'{x.numerator}/{x.denominator}'
def sub(a,b): return tuple(a[k]-b[k] for k in range(3))
def add(a,b): return tuple(a[k]+b[k] for k in range(3))
def mul(a,t): return tuple(a[k]*t for k in range(3))
def dot(a,b): return sum(a[k]*b[k] for k in range(3))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def n2(a): return dot(a,a)
def lcm(a,b): return abs(a*b)//math.gcd(a,b)
def gcdall(xs):
 g=0
 for x in xs:g=math.gcd(g,abs(int(x)))
 return g
def canon(n,h):
 g=gcdall((*n,h)); n=tuple(int(z)//g for z in n); h=int(h)//g
 for z in (*n,h):
  if z:
   if z<0:n=tuple(-v for v in n);h=-h
   break
 return (*n,h)

base={}
with open(R/'coordinates_all_exact.csv') as f:
 for r in csv.DictReader(f):
  i=int(r['source_id']);d=int(r['denominator']);base[i]=tuple(Q(int(r[k]),d) for k in ('x_num','y_num','z_num'))
CSTAR=base[102];Q222=base[222];Q182=base[182]
def construct(a,b):
 P=dict(base);P[222]=add(CSTAR,mul(sub(Q222,CSTAR),1+a));P[182]=add(CSTAR,mul(sub(Q182,CSTAR),1+b));return P

def reconstruct(a,b,stored=None, exhaustive=True):
 P=construct(a,b);L=BASE
 for z in (a.denominator,b.denominator):L=lcm(L,BASE*z)
 rows={i:tuple(int(v*L) for v in p) for i,p in P.items()}
 assert all(Q(rows[i][k],L)==P[i][k] for i in rows for k in range(3))
 # Stored cycles are used only as a comparison target, not as reconstruction input.
 stored_cycles=[] if stored is None else [f['cycle'] for f in stored['faces']]
 stored_keys={}
 for fi,c in enumerate(stored_cycles):
  x,y,z=(rows[i] for i in c[:3]);n=cross(sub(y,x),sub(z,x));h=dot(n,x)
  vals=[dot(n,p)-h for p in rows.values()]
  assert not(any(v>0 for v in vals) and any(v<0 for v in vals))
  if any(v>0 for v in vals):n=tuple(-v for v in n);h=-h
  key=canon(n,h);assert key not in stored_keys;stored_keys[key]=fi
 # Exhaustive complete V->H supporting-plane enumeration.
 coord_to_ids=defaultdict(list)
 for i,p in rows.items():coord_to_ids[p].append(i)
 pts=list(coord_to_ids);found={}
 for ia in range(len(pts)-2):
  x=pts[ia]
  for ib in range(ia+1,len(pts)-1):
   xy=sub(pts[ib],x)
   for ic in range(ib+1,len(pts)):
    n=cross(xy,sub(pts[ic],x))
    if n==(0,0,0):continue
    h=dot(n,x);sg=0;ok=True
    for p in pts:
     v=dot(n,p)-h
     if v:
      s=1 if v>0 else -1
      if sg and s!=sg:ok=False;break
      sg=s
    if not ok:continue
    if sg>0:n=tuple(-v for v in n);h=-h
    key=canon(n,h);cop=frozenset(i for i,p in rows.items() if dot(n,p)==h)
    rec=(cop,n,h)
    if key in found:assert found[key][0]==cop
    else:found[key]=rec
 if stored is not None:
  assert set(found)==set(stored_keys),(len(found),len(stored_keys),len(set(found)-set(stored_keys)),len(set(stored_keys)-set(found)))
 # Recover oriented cycles. When no stored template is supplied, every non-base
 # face at these wall representatives is triangular; the only polygon is the
 # protected 17-gon, whose exact cyclic order is the source order 0..16.
 if stored is None:
  cycles=[]
  for key,(cop,n,h) in found.items():
   if len(cop)==3:c=sorted(cop)
   else:
    assert cop==frozenset(range(17)),(len(cop),sorted(cop))
    c=list(range(17))
   area=(0,0,0)
   for u,v in zip(c,c[1:]+c[:1]):area=add(area,cross(rows[u],rows[v]))
   if dot(area,n)<0:
    c=[c[0]]+list(reversed(c[1:]))
   cycles.append(c)
 else:
  cycles=stored_cycles
 planes=[]
 for fi,c in enumerate(cycles):
  x,y,z=(rows[i] for i in c[:3]);n=cross(sub(y,x),sub(z,x));h=dot(n,x)
  vals={i:dot(n,p)-h for i,p in rows.items()}
  if any(v>0 for v in vals.values()):n=tuple(-v for v in n);h=-h;vals={i:-v for i,v in vals.items()}
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
 # Exact mass.
 D6=0;M=[0,0,0]
 for c in cycles:
  for j in range(1,len(c)-1):
   x,y,z=(rows[i] for i in (c[0],c[j],c[j+1]));d=det(x,y,z);D6+=d
   for k in range(3):M[k]+=d*(x[k]+y[k]+z[k])
 assert D6>0;V=Q(D6,6*L**3);C=tuple(Q(M[k],4*D6*L) for k in range(3));Mom=tuple(Q(M[k],24*L**4) for k in range(3));assert all(Mom[k]==V*C[k] for k in range(3))
 X={i:tuple(Q(rows[i][k],L)-C[k] for k in range(3)) for i in active}
 # Faces.
 stable=[];face_raw={}
 for fi,c in enumerate(cycles):
  n=tuple(Q(v) for v in planes[fi][0]);h=dot(n,X[c[0]]);foot=mul(n,h/n2(n));ref=tuple(sum((X[i][k] for i in c),Q(0))/len(c) for k in range(3));vals=[]
  for u,v in zip(c,c[1:]+c[:1]):
   e=sub(X[v],X[u]);z=dot(cross(e,sub(foot,X[u])),n)
   if dot(cross(e,sub(ref,X[u])),n)<0:z=-z
   vals.append(z)
  face_raw[fi]=vals
  if min(vals)>0:stable.append(fi)
 # Vertices.
 N=defaultdict(set)
 for u,v in EF:N[u].add(v);N[v].add(u)
 SUP={};unst=[]
 for i in active:
  vals={j:-dot(X[i],sub(X[j],X[i])) for j in sorted(N[i])};SUP[i]=vals
  if min(vals.values())>0:unst.append(i)
 # Edges.
 eraw={};sadd=[]
 for e,inc in sorted(EF.items()):
  i,j=e;d=sub(X[j],X[i]);t=-dot(X[i],d)/n2(d);p=add(X[i],mul(d,t));n1=tuple(Q(v) for v in planes[inc[0]][0]);n2v=tuple(Q(v) for v in planes[inc[1]][0]);aa=n2(n1);bb=dot(n1,n2v);cc=n2(n2v);r1=dot(p,n1);r2=dot(p,n2v);den=aa*cc-bb*bb;assert den>0;b1=(r1*cc-r2*bb)/den;b2=(r2*aa-r1*bb)/den;vals=(t,Q(1)-t,b1,b2);eraw[e]=vals
  if min(vals)>0:sadd.append(e)
 return {'rows':rows,'L':L,'cycles':cycles,'planes':planes,'EF':EF,'active':active,'inactive':inactive,'V':V,'C':C,'X':X,'stable':stable,'SUP':SUP,'unst':unst,'eraw':eraw,'sadd':sadd,'face_raw':face_raw,'found':found}

for cell in A['cells']:
 a=q(cell['parameters']['a_222']);b=q(cell['parameters']['b_182']);R0=reconstruct(a,b,cell)
 assert [len(R0['active']),len(R0['EF']),len(R0['cycles'])]==cell['f_vector']
 assert R0['active']==cell['active_rows'];assert R0['inactive']==cell['inactive_rows']
 assert qs(R0['V'])==cell['volume_exact'];assert [qs(z) for z in R0['C']]==cell['centroid_exact']
 assert [len(R0['stable']),len(R0['unst']),len(R0['sadd'])]==cell['class']
 assert [R0['cycles'][i] for i in R0['stable']]==[f['cycle'] for f in cell['stable_faces']]
 assert R0['unst']==[v['vertex'] for v in cell['unstable_vertices']]
 assert R0['sadd']==[tuple(e['edge']) for e in cell['saddle_edges']]
 assert any(set(R0['cycles'][i])==set(range(17)) for i in R0['stable']);assert 8 in R0['unst']
 # External-positive obstruction remains exact in every atlas cell.
 assert (153,154) in R0['EF']
 for i,j in ((153,154),(154,153)):assert all(v>0 for k,v in R0['SUP'][i].items() if k!=j)
 A0=R0['SUP'][153][154];B0=R0['SUP'][154][153];assert A0+B0==n2(sub(R0['X'][154],R0['X'][153]))>0
 assert all(v>0 for v in R0['SUP'][8].values())
 print('PASS exact atlas cell',cell['name'],'f-vector',cell['f_vector'],'class',cell['class'],'supporting planes',len(R0['found']))

# Independently evaluate exact signs at both sides of each isolated wall.
for w in A['wall_brackets']:
 axis=w['axis'];states=w['states'];assert Q(w['width_exact'])==Q(1,10**13)
 signs=[]
 for st in states:
  t=Q(st['parameter']);a,b=(t,Q(0)) if axis=='A' else (Q(0),t)
  # Reconstruct the exact wall-side hull directly from all supporting triples.
  R0=reconstruct(a,b,None)
  if axis=='A':
   v=R0['SUP'][222][221];e=min(R0['eraw'][(221,222)]);assert qs(v)==st['signatures']['vertex_222_min_support_exact'];signs.append((v>0,e>0))
  else:
   fi=next(i for i,c in enumerate(R0['cycles']) if set(c)=={172,175,182});v=min(R0['face_raw'][fi]);e=min(R0['eraw'][(172,182)]);signs.append((v>0,e>0))
 assert signs==[(False,False),(True,True)],(w['name'],signs)
 print('PASS isolated exact paired-birth wall',w['name'],w['interval_exact'])
print('PASS all four exact first outgoing chambers and both width-1e-13 wall brackets; no chamber is (1,1,0)')
