#!/usr/bin/env python3
"""Outward exact rational interval verification of an open coordinate box."""
from __future__ import annotations
from fractions import Fraction as Q
from collections import defaultdict
from pathlib import Path
import csv,json
R=Path(__file__).resolve().parent;RAD=Q(1,10**12);CERT=json.load(open(R/'certificate.json'));S=int(CERT['scale'])
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
for r in csv.DictReader(open(R/'coordinates_all_exact.csv')):
 i=int(r['source_id']);assert int(r['denominator'])==S;p=tuple(Q(int(r[k]),S) for k in ('x_int','y_int','z_int'));rows[i]=p;(active if int(r['active']) else inactive).append(i)
faces=json.load(open(R/'faces_mechanics.json'));cycles=[z['cycle'] for z in faces]
# Base plane vertices and inactive inputs fixed. Every other active coordinate varies independently.
P={}
for i,p in rows.items():
 variable=i in active and i not in range(17)
 P[i]=tuple(I(z-RAD,z+RAD) if variable else I(z) for z in p)
face_nom=[[Q(z) for z in f['components_exact']] for f in faces]
vert_nom={}
for r in csv.DictReader(open(R/'vertices_mechanics.csv')):vert_nom[int(r['vertex'])]={int(j):Q(z) for j,z in json.loads(r['supports_exact_json']).items()}
edge_nom={}
for r in csv.DictReader(open(R/'edges_four_component_audit.csv')):edge_nom[(int(r['u']),int(r['v']))]=[Q(r[k]) for k in ('t_exact','one_minus_t_exact','beta1_exact','beta2_exact')]
EF=defaultdict(list);N=defaultdict(set)
for fi,c in enumerate(cycles):
 for a,b in zip(c,c[1:]+c[:1]):e=tuple(sorted((a,b)));EF[e].append(fi);N[a].add(b);N[b].add(a)
assert (len(active),len(EF),len(cycles))==(61,163,104) and all(len(z)==2 for z in EF.values())
# Complete incidence.
top=[];ing=[]
for fi,c in enumerate(cycles):
 a,b,z=(P[c[0]],P[c[1]],P[c[2]])
 for i,p in P.items():
  if i in c:continue
  d=det(sub(b,a),sub(z,a),sub(p,a));assert d.hi<0,(fi,i,float(d.lo),float(d.hi));top.append(-d.hi)
  if i in inactive:ing.append(-d.hi)
# Exact interval mass and own centroid.
D6=I(0);M=[I(0),I(0),I(0)]
for c in cycles:
 for j in range(1,len(c)-1):
  a,b,z=P[c[0]],P[c[j]],P[c[j+1]];d=det(a,b,z);D6+=d;ss=add(add(a,b),z)
  for k in range(3):M[k]+=d*ss[k]
assert D6.lo>0;V=D6/6;C=tuple(M[k]/(4*D6) for k in range(3));X={i:tuple(P[i][k]-C[k] for k in range(3)) for i in active}
for k in range(3):
 z=(-V*C[k])+(M[k]/24);assert z.lo<=0<=z.hi
FN=[cross(sub(P[c[1]],P[c[0]]),sub(P[c[2]],P[c[0]])) for c in cycles]
# Full face cones.
fp=[];fn=[]
for fi,c in enumerate(cycles):
 n=FN[fi];h=dot(n,X[c[0]]);foot=mul(n,h/n2(n));vals=[dot(cross(sub(X[b],X[a]),sub(foot,X[a])),n) for a,b in zip(c,c[1:]+c[:1])];nom=face_nom[fi];eq=all(z>0 for z in nom)
 if eq:
  assert all(z.lo>0 for z in vals),(fi,[(float(z.lo),float(z.hi)) for z in vals]);fp.extend(z.lo for z in vals)
 else:
  k=min(range(len(nom)),key=lambda j:nom[j]);assert nom[k]<0 and vals[k].hi<0,(fi,k,float(vals[k].lo),float(vals[k].hi));fn.append(-vals[k].hi)
assert sum(all(z>0 for z in x) for x in face_nom)==2
# Full vertex cones.
SUP={};vp=[];vn=[]
for i in active:
 vals={j:-dot(X[i],sub(X[j],X[i])) for j in sorted(N[i])};SUP[i]=vals;nom=vert_nom[i];eq=all(z>0 for z in nom.values())
 if eq:
  assert all(z.lo>0 for z in vals.values()),(i,[(j,float(z.lo),float(z.hi)) for j,z in vals.items()]);vp.extend(z.lo for z in vals.values())
 else:
  j=min(nom,key=nom.get);assert nom[j]<0 and vals[j].hi<0,(i,j,float(vals[j].lo),float(vals[j].hi));vn.append(-vals[j].hi)
assert sum(all(z>0 for z in vert_nom[i].values()) for i in active)==1
# All four-component edge cones.
hp=[];hn=[]
for e,inc in sorted(EF.items()):
 i,j=e;d=sub(X[j],X[i]);t=-dot(X[i],d)/n2(d);p=add(X[i],mul(d,t));n1=FN[inc[0]];n2v=FN[inc[1]];aa=n2(n1);bb=dot(n1,n2v);cc=n2(n2v);r1=dot(p,n1);r2=dot(p,n2v);den=aa*cc-bb*bb;assert den.lo>0,(e,float(den.lo),float(den.hi));b1=(r1*cc-r2*bb)/den;b2=(r2*aa-r1*bb)/den;vals=[t,1-t,b1,b2];nom=edge_nom[e];eq=all(z>0 for z in nom)
 if eq:
  assert all(z.lo>0 for z in vals),(e,[(float(z.lo),float(z.hi)) for z in vals]);hp.extend(z.lo for z in vals)
 else:
  k=min(range(4),key=lambda j:nom[j]);assert nom[k]<0 and vals[k].hi<0,(e,k,float(vals[k].lo),float(vals[k].hi));hn.append(-vals[k].hi)
assert sum(all(z>0 for z in edge_nom[e]) for e in EF)==1
# Predecessor packet remains deleted.
for i in CERT['old_fourth_packet_rows_now_inactive']:assert i in inactive
for e in [(135,224),(183,223),(226,227)]:assert e not in EF
assert not any(set(c)=={195,223,224} for c in cycles)
# Both rail directions and enough positive-dot edges to retain graph connectivity.
graph=json.load(open(R/'acute_bridge_graph.json'));railraw=[];raildot=[]
for rail in [graph['short_rail'],graph['long_rail']]:
 for z in rail['steps']:
  a,b=z['from'],z['to'];rr=dot(X[a],sub(X[b],X[a]));pd=dot(X[a],X[b]);assert rr.lo>0 and pd.lo>0,(a,b,float(rr.lo),float(pd.lo));railraw.append(rr.lo);raildot.append(pd.lo)
# Verify every nominal positive-dot edge stays positive; this keeps the stored connected spanning graph.
positive=[]
for z in graph['positive_dot_true_edges']:
 a,b=z['edge'];d=dot(X[a],X[b]);assert d.lo>0,(a,b,float(d.lo),float(d.hi));positive.append(d.lo)
# All strict cell atlas members and closure tetrahedra.
complexrec=json.load(open(R/'fifth_cell_complex.json'));cell=[];bary=[]
for z in complexrec['all_strict_convex_edge_star_bipyramids']:
 a,b=z['true_edge'];u,v=z['apices'];dp=det(X[u],X[a],X[b]);dm=det(X[v],X[a],X[b]);assert (dp.lo>0 and dm.hi<0) or (dp.hi<0 and dm.lo>0),(z['true_edge'],float(dp.lo),float(dp.hi),float(dm.lo),float(dm.hi));cell.extend([min(abs(dp.lo),abs(dp.hi)),min(abs(dm.lo),abs(dm.hi))]);t=dp/(dp-dm);p=add(X[u],mul(sub(X[v],X[u]),t));aa=n2(X[a]);bb=dot(X[a],X[b]);cc=n2(X[b]);ra=dot(p,X[a]);rb=dot(p,X[b]);den=aa*cc-bb*bb;assert den.lo>0;la=(ra*cc-rb*bb)/den;lb=(rb*aa-ra*bb)/den;l0=1-la-lb
 for zz in (t,1-t,l0,la,lb):assert zz.lo>0,(z['true_edge'],float(zz.lo),float(zz.hi));bary.append(zz.lo)
closure=[]
for fi in complexrec['closure_face_ids']:
 c=cycles[fi];z=det(X[c[0]],X[c[1]],X[c[2]]);assert z.lo>0 or z.hi<0,(fi,float(z.lo),float(z.hi));closure.append(min(abs(z.lo),abs(z.hi)))
out={'version':1,'radius_exact':str(RAD),'radius_decimal':float(RAD),'variable_rows':[i for i in active if i not in range(17)],'variable_coordinates':3*len([i for i in active if i not in range(17)]),'fixed_base_rows':list(range(17)),'fixed_inactive_rows':inactive,'preserved_f_vector':[61,163,104],'preserved_class':[2,1,1],'volume_box':[str(V.lo),str(V.hi),float(V.lo),float(V.hi)],'centroid_box':[[str(z.lo),str(z.hi),float(z.lo),float(z.hi)] for z in C],'strict_lower_bounds':{'facet_determinant':float(min(top)),'inactive_facet_determinant':float(min(ing)),'stable_face_component':float(min(fp)),'nonstable_witness':float(min(fn)),'unstable_vertex_support':float(min(vp)),'nonunstable_witness':float(min(vn)),'saddle_edge_component':float(min(hp)),'nonsaddle_witness':float(min(hn)),'rail_directed_support':float(min(railraw)),'positive_dot_spanning_graph':float(min(positive)),'cell_tetra_determinant':float(min(cell)),'cell_barycentric':float(min(bary)),'closure_fan_determinant':float(min(closure))},'verdict':'PASS: the exact +/-1e-12 coordinate box preserves the complete (61,163,104) hull, strict own-centroid (2,1,1), both 19-edge monotone rails, connected positive-dot graph, all 64 strict convex edge-star bipyramids, and predecessor feature deletion.'}
json.dump(out,open(R/'interval_certificate.json','w'),indent=2)
print(out['verdict']);print('variable coordinates',out['variable_coordinates']);print('bounds',out['strict_lower_bounds'])
