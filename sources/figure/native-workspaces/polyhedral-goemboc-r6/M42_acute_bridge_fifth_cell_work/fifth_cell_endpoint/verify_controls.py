#!/usr/bin/env python3
"""Independent exact check of the two one-sided shape controls and 3 moment translations."""
from fractions import Fraction as F
from pathlib import Path
import csv,json
R=Path(__file__).resolve().parent
cert=json.load(open(R/'certificate.json')); ctl=json.load(open(R/'control_certificate.json')); S=int(cert['scale'])
def add(a,b):return tuple(a[k]+b[k] for k in range(3))
def sub(a,b):return tuple(a[k]-b[k] for k in range(3))
def mul(a,t):return tuple(a[k]*t for k in range(3))
def dot(a,b):return sum(a[k]*b[k] for k in range(3))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def q(s):return F(s)
def qs(x):return f'{x.numerator}/{x.denominator}'
P={}
for r in csv.DictReader(open(R/'coordinates_all_exact.csv')):
 P[int(r['source_id'])]=tuple(F(int(r[k]),S) for k in ('x_int','y_int','z_int'))
C=tuple(q(z) for z in cert['centroid_unshifted_exact']); V=q(cert['volume_exact'])
cycles=json.load(open(R/'face_cycles.json')); tris=[]
for c in cycles:
 for j in range(1,len(c)-1):tris.append((c[0],c[j],c[j+1]))
D6=6*V; N=[F(0),F(0),F(0)]
for I in tris:
 a,b,c=(P[i] for i in I);d=det(a,b,c);s=add(add(a,b),c)
 for k in range(3):N[k]+=d*s[k]
assert tuple(N[k]/(4*D6) for k in range(3))==C
assert q(ctl['moment_closure']['translation_jacobian_determinant_exact'])==V**3 and ctl['moment_closure']['rank']==3
seen=set()
for z in ctl['independent_shape_antibirth_controls']:
 move=int(z['moved_row']);a,b=map(int,z['witness_directed_edge']);v=tuple(q(x) for x in z['direction_exact'])
 assert move==b and move not in seen;seen.add(move)
 d6p=F(0);Np=[F(0),F(0),F(0)]
 for I in tris:
  aa,bb,cc=(P[i] for i in I);d=det(aa,bb,cc);s=add(add(aa,bb),cc)
  if move in I:
   pos=I.index(move);dp=det(v,bb,cc) if pos==0 else det(aa,v,cc) if pos==1 else det(aa,bb,v);d6p+=dp
   for k in range(3):Np[k]+=dp*s[k]+d*v[k]
 Cp=tuple((Np[k]*D6-N[k]*d6p)/(4*D6*D6) for k in range(3))
 assert [qs(x) for x in Cp]==z['centroid_derivative_exact']
 x=sub(P[a],C); d=sub(P[b],P[a]); W=dot(x,d); Wp=dot(tuple(-u for u in Cp),d)+dot(x,v)
 assert W==q(z['base_witness_exact']) and Wp==q(z['witness_derivative_exact']) and W>0 and Wp>0
 smax=q(z['positive_parameter_interval'][1]);disp=max(abs(smax*u) for u in v)
 assert disp==q(z['maximum_coordinate_displacement_exact']) and disp<F(1,10**12)
assert len(seen)==2 and ctl['disjoint_row_support'] and ctl['combined_control_rank']==5
print('PASS independent exact control check: rank 5, disjoint rows',sorted(seen))
