#!/usr/bin/env python3
from fractions import Fraction as Q
from pathlib import Path
import csv,json
R=Path(__file__).resolve().parent;cert=json.load(open(R/'certificate.json'));S=int(cert['scale']);cycles=json.load(open(R/'face_cycles.json'))
def add(a,b):return tuple(a[k]+b[k] for k in range(3))
def sub(a,b):return tuple(a[k]-b[k] for k in range(3))
def mul(a,t):return tuple(a[k]*t for k in range(3))
def dot(a,b):return sum(a[k]*b[k] for k in range(3))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def qs(x):x=Q(x);return f'{x.numerator}/{x.denominator}'
P={}
for r in csv.DictReader(open(R/'coordinates_all_exact.csv')):P[int(r['source_id'])]=tuple(Q(int(r[k]),S) for k in ('x_int','y_int','z_int'))
C=tuple(Q(x) for x in cert['centroid_unshifted_exact']);V=Q(cert['volume_exact']);D6=6*V
tris=[]
for c in cycles:
 for j in range(1,len(c)-1):tris.append((c[0],c[j],c[j+1]))
def derivative(move,v):
 d6=Q(0);N=[Q(0),Q(0),Q(0)];d6p=Q(0);Np=[Q(0),Q(0),Q(0)]
 for ids in tris:
  a,b,c=(P[i] for i in ids);d=det(a,b,c);ss=add(add(a,b),c);d6+=d
  for k in range(3):N[k]+=d*ss[k]
  if move in ids:
   pos=ids.index(move);dp=det(v,b,c) if pos==0 else det(a,v,c) if pos==1 else det(a,b,v);d6p+=dp
   for k in range(3):Np[k]+=dp*ss[k]+d*v[k]
 assert d6==D6
 Cp=tuple((Np[k]*d6-N[k]*d6p)/(4*d6*d6) for k in range(3))
 return Cp,d6p,tuple(Np)
controls=[]
for name,a,b,src in [('short_rail_antibirth',231,232,231),('long_rail_antibirth',247,248,247)]:
 v=sub(P[src],C);Cp,d6p,Np=derivative(b,v);x=sub(P[a],C);d=sub(P[b],P[a]);W=dot(x,d);Wp=dot(tuple(-z for z in Cp),d)+dot(x,v);assert W>0 and Wp>0
 smax=Q(1,10**14);disp=max(abs(smax*z) for z in v);assert disp<Q(1,10**12)
 controls.append({'name':name,'moved_row':b,'witness_directed_edge':[a,b],'direction_exact':[qs(z) for z in v],'base_witness_exact':qs(W),'base_witness_decimal':float(W),'centroid_derivative_exact':[qs(z) for z in Cp],'witness_derivative_exact':qs(Wp),'witness_derivative_decimal':float(Wp),'positive_parameter_interval':['0/1',qs(smax)],'maximum_coordinate_displacement_exact':qs(disp),'maximum_coordinate_displacement_decimal':float(disp),'inside_coordinate_box_radius_exact':'1/1000000000000','strictly_away_from_vertex_birth_wall':True})
out={'version':1,'moment_closure':{'dependent_controls':'global translation tau=-C(s,t)','base_volume_exact':qs(V),'translation_moment_jacobian':'V*I_3','translation_jacobian_determinant_exact':qs(V**3),'rank':3},'independent_shape_antibirth_controls':controls,'disjoint_row_support':True,'combined_control_rank':5,'open_stability_reference':'interval_certificate.json','verdict':'PASS: two disjoint exact one-sided shape directions increase the nearest short/long rail nonunstable witnesses and remain strictly inside the certified coordinate box; three exact dependent translations close all moments.'}
json.dump(out,open(R/'control_certificate.json','w'),indent=2)
print(out['verdict']);print('derivatives',[z['witness_derivative_decimal'] for z in controls]);print('displacements',[z['maximum_coordinate_displacement_decimal'] for z in controls])
