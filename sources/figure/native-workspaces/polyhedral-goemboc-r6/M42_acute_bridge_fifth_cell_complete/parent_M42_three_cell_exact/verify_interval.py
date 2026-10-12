#!/usr/bin/env python3
"""Exact rational interval box for the M42 three-cell endpoint."""
from __future__ import annotations
from fractions import Fraction as Q
from collections import defaultdict
from pathlib import Path
import csv,json
R=Path(__file__).resolve().parent;RAD=Q(1,10**12)
cert=json.load(open(R/'certificate.json'));S=int(cert['scale'])
class I:
 __slots__=('lo','hi')
 def __init__(self,lo,hi=None):self.lo=Q(lo);self.hi=Q(lo if hi is None else hi);assert self.lo<=self.hi
 def __add__(self,o):o=iv(o);return I(self.lo+o.lo,self.hi+o.hi)
 __radd__=__add__
 def __neg__(self):return I(-self.hi,-self.lo)
 def __sub__(self,o):return self+(-iv(o))
 def __rsub__(self,o):return iv(o)-self
 def __mul__(self,o):
  o=iv(o);z=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi);return I(min(z),max(z))
 __rmul__=__mul__
 def recip(self):
  assert not(self.lo<=0<=self.hi),(self.lo,self.hi)
  return I(min(1/self.lo,1/self.hi),max(1/self.lo,1/self.hi))
 def __truediv__(self,o):return self*iv(o).recip()
 def __rtruediv__(self,o):return iv(o)/self
def iv(x):return x if isinstance(x,I) else I(x)
def add(a,b):return tuple(a[k]+b[k] for k in range(3))
def sub(a,b):return tuple(a[k]-b[k] for k in range(3))
def mul(a,t):return tuple(a[k]*t for k in range(3))
def dot(a,b):return sum((a[k]*b[k] for k in range(3)),I(0))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def n2(a):return dot(a,a)
rows={};active=[];inactive=[]
with open(R/'coordinates_all_exact.csv') as f:
 for r in csv.DictReader(f):
  i=int(r['source_id']);p=tuple(Q(int(r[k]),S) for k in ('x_num','y_num','z_num'));rows[i]=p;(active if int(r['active']) else inactive).append(i)
faces=json.load(open(R/'faces_mechanics.json'));cycles=[f['cycle'] for f in faces]
P={}
for i,p in rows.items():
 variable=(i in active and i not in range(17))
 P[i]=tuple(I(z-RAD,z+RAD) if variable else I(z) for z in p)
face_nom=[[Q(z) for z in f['components_exact']] for f in faces]
vert_nom={}
with open(R/'vertices_mechanics.csv') as f:
 for r in csv.DictReader(f):vert_nom[int(r['vertex'])]={int(j):Q(z) for j,z in json.loads(r['supports_exact_json']).items()}
edge_nom={}
with open(R/'edges_four_component_audit.csv') as f:
 for r in csv.DictReader(f):edge_nom[(int(r['u']),int(r['v']))]=[Q(r[k]) for k in ('t_exact','one_minus_t_exact','beta1_exact','beta2_exact')]
EF=defaultdict(list);N=defaultdict(set)
for fi,c in enumerate(cycles):
 for a,b in zip(c,c[1:]+c[:1]):e=tuple(sorted((a,b)));EF[e].append(fi);N[a].add(b);N[b].add(a)
assert len(EF)==256 and len(cycles)==166 and all(len(v)==2 for v in EF.values())
# 1 incidence
top=[];ing=[]
for fi,c in enumerate(cycles):
 a,b,z=(P[c[0]],P[c[1]],P[c[2]])
 for i,p in P.items():
  if i in c:continue
  d=det(sub(b,a),sub(z,a),sub(p,a));assert d.hi<0,(fi,i,float(d.lo),float(d.hi));top.append(-d.hi)
  if i in inactive:ing.append(-d.hi)
# 2 interval mass/centroid
D6=I(0);M=[I(0),I(0),I(0)]
for c in cycles:
 for j in range(1,len(c)-1):
  a,b,z=P[c[0]],P[c[j]],P[c[j+1]];d=det(a,b,z);D6+=d;s=add(add(a,b),z)
  for k in range(3):M[k]+=d*s[k]
assert D6.lo>0;V=D6/6;C=tuple(M[k]/(4*D6) for k in range(3));X={i:tuple(P[i][k]-C[k] for k in range(3)) for i in active}
for k in range(3):
 z=(-V*C[k])+(M[k]/24);assert z.lo<=0<=z.hi
FN=[cross(sub(P[c[1]],P[c[0]]),sub(P[c[2]],P[c[0]])) for c in cycles]
# 3 faces
fp=[];fn=[]
for fi,c in enumerate(cycles):
 n=FN[fi];h=dot(n,X[c[0]]);foot=mul(n,h/n2(n));vals=[dot(cross(sub(X[b],X[a]),sub(foot,X[a])),n) for a,b in zip(c,c[1:]+c[:1])];nom=face_nom[fi];eq=all(z>0 for z in nom)
 if eq:assert all(z.lo>0 for z in vals),(fi,[(float(z.lo),float(z.hi)) for z in vals]);fp += [z.lo for z in vals]
 else:
  k=min(range(len(nom)),key=lambda j:nom[j]);assert nom[k]<0 and vals[k].hi<0,(fi,k,float(vals[k].lo),float(vals[k].hi));fn.append(-vals[k].hi)
assert sum(all(z>0 for z in nom) for nom in face_nom)==2
# 4 vertices
SUP={};vp=[];vn=[]
for i in active:
 vals={j:-dot(X[i],sub(X[j],X[i])) for j in sorted(N[i])};SUP[i]=vals;nom=vert_nom[i];eq=all(z>0 for z in nom.values())
 if eq:assert all(z.lo>0 for z in vals.values()),(i,[(j,float(z.lo),float(z.hi)) for j,z in vals.items()]);vp += [z.lo for z in vals.values()]
 else:
  j=min(nom,key=nom.get);assert nom[j]<0 and vals[j].hi<0,(i,j,float(vals[j].lo),float(vals[j].hi));vn.append(-vals[j].hi)
assert sum(all(z>0 for z in vert_nom[i].values()) for i in active)==2
# 5 edges
hp=[];hn=[]
for e,inc in sorted(EF.items()):
 i,j=e;d=sub(X[j],X[i]);t=-dot(X[i],d)/n2(d);p=add(X[i],mul(d,t));n1=FN[inc[0]];n2v=FN[inc[1]];aa=n2(n1);bb=dot(n1,n2v);cc=n2(n2v);r1=dot(p,n1);r2=dot(p,n2v);den=aa*cc-bb*bb;assert den.lo>0,(e,float(den.lo),float(den.hi));b1=(r1*cc-r2*bb)/den;b2=(r2*aa-r1*bb)/den;vals=[t,1-t,b1,b2];nom=edge_nom[e];eq=all(z>0 for z in nom)
 if eq:assert all(z.lo>0 for z in vals),(e,[(float(z.lo),float(z.hi)) for z in vals]);hp += [z.lo for z in vals]
 else:
  k=min(range(4),key=lambda j:nom[j]);assert nom[k]<0 and vals[k].hi<0,(e,k,float(vals[k].lo),float(vals[k].hi));hn.append(-vals[k].hi)
assert sum(all(z>0 for z in edge_nom[e]) for e in EF)==2
# 6 combinatorics
for i in cert['absorbed_rows']+cert['old_absorbed_rows_from_predecessor']:assert i in inactive
for e in cert['absent_old_edges']:assert tuple(sorted(e)) not in EF
# 7 obstruction
obs=[]
for i,j in ((153,154),(154,153)):
 for k,s in SUP[i].items():
  if k==j:continue
  assert s.lo>0,(i,k,float(s.lo),float(s.hi));obs.append(s.lo)
A=SUP[153][154];B=SUP[154][153];rhs=n2(sub(X[154],X[153]));rr=A+B-rhs;assert rr.lo<=0<=rr.hi
for s in SUP[8].values():assert s.lo>0;obs.append(s.lo)
# 8 unique farthest target
r8=n2(X[8]);radgap=[]
for i in active:
 if i==8:continue
 z=r8-n2(X[i]);assert z.lo>0,(i,float(z.lo),float(z.hi));radgap.append(z.lo)
# 9 three cell determinant and closure
Mpt=mul(add(add(X[220],X[221]),X[222]),Q(1,3));O=(I(0),I(0),I(0));rec=json.load(open(R/'three_cell_complex.json'));cell=[]
for z in rec['cells']:
 _,u,v=z['equator'];p=z['boundary_apex'];dc=det(Mpt,X[u],X[v]);da=det(X[p],X[u],X[v]);assert (dc.lo>0 and da.hi<0) or (dc.hi<0 and da.lo>0),(u,v,float(dc.lo),float(dc.hi),float(da.lo),float(da.hi));cell.extend([min(abs(dc.lo),abs(dc.hi)),min(abs(da.lo),abs(da.hi))])
closure=[]
for fi in rec['closure_face_ids']:
 c=cycles[fi];z=det(X[c[0]],X[c[1]],X[c[2]]);assert z.lo>0 or z.hi<0,(fi,float(z.lo),float(z.hi));closure.append(min(abs(z.lo),abs(z.hi)))
out={'version':1,'radius_exact':str(RAD),'radius_decimal':float(RAD),'variable_rows':[i for i in active if i not in range(17)],'variable_coordinates':3*len([i for i in active if i not in range(17)]),'fixed_base_rows':list(range(17)),'fixed_inactive_rows':inactive,'preserved_f_vector':[len(active),len(EF),len(cycles)],'preserved_class':[2,2,2],'volume_box':[str(V.lo),str(V.hi),float(V.lo),float(V.hi)],'centroid_box':[[str(z.lo),str(z.hi),float(z.lo),float(z.hi)] for z in C],'strict_lower_bounds':{'facet_determinant':float(min(top)),'inactive_facet_determinant':float(min(ing)),'stable_face_component':float(min(fp)),'nonstable_witness':float(min(fn)),'unstable_vertex_support':float(min(vp)),'nonunstable_witness':float(min(vn)),'saddle_edge_component':float(min(hp)),'nonsaddle_witness':float(min(hn)),'obstruction_and_target_support':float(min(obs)),'target_unique_farthest_squared_gap':float(min(radgap)),'three_cell_tetra_determinant':float(min(cell)),'closure_fan_determinant':float(min(closure))},'preserved_obstruction_edge':[153,154],'verdict':'PASS: exact +/-1e-12 coordinate box preserves the complete (92,256,166) hull, strict own-centroid (2,2,2), old-core and superlevel absorption, unique-farthest target 8, three shared-edge nonsimplicial cells, and the external-positive (153,154) obstruction.'}
json.dump(out,open(R/'interval_certificate.json','w'),indent=2)
print(out['verdict']);print('variable coordinates',out['variable_coordinates']);print('volume',out['volume_box'][2:]);print('centroid',[(z[2],z[3]) for z in out['centroid_box']]);print('lower bounds',out['strict_lower_bounds'])
