#!/usr/bin/env python3
"""Exact cross-file reconstruction of the fourth -> acute-bridge fifth transition."""
from fractions import Fraction as F
from pathlib import Path
from collections import defaultdict,deque
import csv,json,hashlib
R=Path(__file__).resolve().parent; A=R/'fourth_cell_endpoint'; B=R/'fifth_cell_endpoint'
def read_input(p):
 out={};D=None
 for z in csv.DictReader(open(p)):
  d=int(z['denominator']);D=d if D is None else D;assert d==D
  out[int(z['source_id'])]=tuple(int(z[k]) for k in ('x_int','y_int','z_int'))
 return out,D
def dot(a,b):return sum(a[k]*b[k] for k in range(3))
def sub(a,b):return tuple(a[k]-b[k] for k in range(3))
def q3(irow,D,C):return tuple(F(irow[k],D)-C[k] for k in range(3))
def edges(p):
 return {tuple(sorted((int(z['u']),int(z['v'])))) for z in csv.DictReader(open(p))}
def components(V,E,X):
 adj={i:set() for i in V};pos=[]
 for a,b in E:
  if dot(X[a],X[b])>0:adj[a].add(b);adj[b].add(a);pos.append((a,b))
 seen=set();cc=[]
 for s in V:
  if s in seen:continue
  z={s};seen.add(s);dq=[s]
  while dq:
   u=dq.pop()
   for v in adj[u]:
    if v not in seen:seen.add(v);z.add(v);dq.append(v)
  cc.append(sorted(z))
 return sorted(cc,key=lambda z:(-len(z),z)),pos
RA,DA=read_input(A/'input_rows_common_lattice.csv');RB,DB=read_input(B/'input_rows_common_lattice.csv');assert DA==DB
ca=json.load(open(A/'certificate.json'));cb=json.load(open(B/'certificate.json'))
Aactive=set(ca['active_rows']); Binherited=set(RB)&set(RA);new=set(RB)-set(RA)
assert len(RA)==140 and len(RB)==119 and len(Aactive)==83
assert Binherited==Aactive and new==set(range(229,265))
assert all(RA[i]==RB[i] for i in Binherited)
assert set(RA)-set(RB)==set(RA)-Aactive
EA=edges(A/'true_edges.csv');EB=edges(B/'true_edges.csv')
CA=tuple(F(z) for z in ca['centroid_unshifted_exact']);CB=tuple(F(z) for z in cb['centroid_unshifted_exact'])
XA={i:q3(RA[i],DA,CA) for i in Aactive};XB={i:q3(RB[i],DB,CB) for i in cb['active_rows']}
cca,posa=components(sorted(Aactive),EA,XA);ccb,posb=components(cb['active_rows'],EB,XB)
assert list(map(len,cca))==[45,38] and len(ccb)==1 and len(ccb[0])==61
G=json.load(open(B/'acute_bridge_graph.json'))
for key in ('short_rail','long_rail'):
 path=G[key]['path'];assert len(path)==20 and path[0]==228 and path[-1]==8
 for a,b in zip(path,path[1:]):
  assert tuple(sorted((a,b))) in EB
  assert dot(XB[a],XB[b])>0 and dot(XB[a],sub(XB[b],XB[a]))>0
old={135,183,195,223,225,226,227};assert old<=set(cb['inactive_rows'])
assert (226,227) not in EB and (135,224) not in EB and (183,223) not in EB
assert ca['class']==[2,2,2] and cb['class']==[2,1,1]
assert len(posa)==186 and len(posb)==134
out={'version':1,'common_denominator':DA,'fourth_input_rows':len(RA),'fourth_active_rows':len(Aactive),'fifth_input_rows':len(RB),'inherited_rows':len(Binherited),'new_rows':sorted(new),'inherited_coordinates_identical':True,'fourth_f_vector':ca['f_vector'],'fifth_f_vector':cb['f_vector'],'class_transition':[ca['class'],cb['class']],'fourth_positive_dot_components':[len(z) for z in cca],'fifth_positive_dot_components':[len(z) for z in ccb],'fourth_positive_dot_true_edges':len(posa),'fifth_positive_dot_true_edges':len(posb),'old_packet_rows_inactive':sorted(old),'deleted_edges':[[226,227],[135,224],[183,223]],'rails':{k:{'path':G[k]['path'],'minimum_directed_support_exact':G[k]['minimum_directed_support_exact']} for k in ('short_rail','long_rail')},'verdict':'PASS: the fifth generator is exactly the 83 active fourth rows plus 36 new rows; both exact 19-edge rails merge the previous 45+38 acute components, remove the fourth U-H packet, and change (2,2,2) to (2,1,1).'}
json.dump(out,open(R/'fourth_to_fifth_lineage_certificate.json','w'),indent=2)
print(out['verdict'])
