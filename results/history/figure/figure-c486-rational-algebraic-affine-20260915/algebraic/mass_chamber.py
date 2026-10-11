"""Exact filled-mass equations and scalar quartic for a one-point hull.
Usage: python -B -S mass_chamber.py C592_PROOF NEW_OUTPUT_JSON
"""
import hashlib,json,sys
from pathlib import Path
from fractions import Fraction as Q
from math import gcd,lcm
import augment_exact as ag
assert __debug__
sys.set_int_max_str_digits(0)
B=ag.B;SHA=ag.SHA
Z=(Q(0),)*3

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(t,a):return tuple(t*x for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def matvec(A,x):return tuple(dot(row,x) for row in A)
def det(A):return dot(A[0],cross(A[1],A[2]))
def encode(x):
 if isinstance(x,Q):return str(x)
 if isinstance(x,(tuple,list)):return [encode(y) for y in x]
 if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
 return x

def primitive(p):
 den=lcm(*(x.denominator for x in p));a=[int(x*den) for x in p];g=gcd(*a)
 return [x//g for x in a] if g else a

def run(root,output):
 ab=(root/'A.json').read_bytes();pb=(root/'PARENT_A.json').read_bytes()
 assert SHA(ab)==ag.CHILD
 assert SHA(pb)=='2426da394eda9520bd30b2b8b3e1f00d043697353bb6bc73658f5983653c11ec'
 A=json.loads(ab);parent=json.loads(pb)
 P=[tuple(map(Q,row)) for row in A['raw_vertices']]
 normals=[tuple(Q(x,h) for x in n) for n,h in zip(A['normals'],A['offsets'])]
 c0=tuple(map(Q,parent['raw_centroid']));a=tuple(Q(x,ag.D) for x in ag.TRIAL)
 V=Q(0);M=Z;k=Z;k0=Q(0);BB=[[Q(0)]*3 for _ in range(3)];b0=Z;visible=[]
 fullk=Z;fullB=[[Q(0)]*3 for _ in range(3)]
 for fi,(cy,q) in enumerate(zip(A['faces'],normals)):
  ff=Q(0);bf=Z
  for j in range(1,len(cy)-1):
   u,v,w=[P[i] for i in (cy[0],cy[j],cy[j+1])]
   h=dot(u,cross(v,w))/6;assert h>0
   ff+=h;bf=add(bf,mul(h,add(add(u,v),w)))
  V+=ff;M=add(M,mul(Q(1,4),bf));fullk=add(fullk,mul(ff,q))
  for i in range(3):
   for j in range(3):fullB[i][j]+=bf[i]*q[j]/4
  gap=dot(q,a)-1;assert gap!=0
  if gap<0:continue
  visible.append(fi);k=add(k,mul(ff,q));k0-=ff;b0=sub(b0,mul(Q(1,4),bf))
  for i in range(3):
   for j in range(3):BB[i][j]+=bf[i]*q[j]/4
 assert V==Q(A['ordinary_volume']) and M==tuple(map(Q,A['raw_first_moments']))
 assert fullk==Z and fullB==[[V/4 if i==j else 0 for j in range(3)] for i in range(3)]
 d=sub(add(M,b0),mul(V+k0,c0))
 L=[[BB[i][j]+(k0/4 if i==j else 0)-c0[i]*k[j] for j in range(3)] for i in range(3)]
 tr=sum(L[i][i] for i in range(3));c2=sum(L[i][i]*L[j][j]-L[i][j]*L[j][i] for i in range(3) for j in range(i+1,3));c3=det(L)
 Ld=matvec(L,d);L2d=matvec(L,Ld);kd=dot(k,d);kLd=dot(k,Ld);kL2d=dot(k,L2d)
 delta=[c3,c2,tr,Q(1)]
 N=[[L2d[i]-tr*Ld[i]+c2*d[i],tr*d[i]-Ld[i],d[i]] for i in range(3)]
 polynomial=[kL2d-tr*kLd+c2*kd,4*c3+tr*kd-kLd,4*c2+kd,4*tr,Q(4)]
 t0=dot(k,a)/4
 value=add(add(d,matvec(L,a)),mul(t0,a))
 VV=V+k0+4*t0
 MM=add(add(M,b0),add(matvec(BB,a),mul(k0/4+t0,a)))
 assert value==sub(MM,mul(VV,c0))
 data=encode(dict(identity='C592_OPPOSITE_VISIBILITY_MASS_QUARTIC',C592_A_sha256=SHA(ab),C602_A_sha256=SHA(pb),new_point_grid=ag.D,new_point_proposal=list(ag.TRIAL),visible_facets=visible,target_centroid=c0,body_volume=V,body_first_moments=M,chamber_k=k,chamber_k0=k0,chamber_B=BB,chamber_b0=b0,closure_d=d,closure_L=L,determinant_coefficients_low_to_high=delta,adjugate_times_d_coefficients_low_to_high=N,quartic_coefficients_low_to_high=polynomial,quartic_integer_coefficients_low_to_high=primitive(polynomial),trial_t=t0,trial_volume=VV,trial_first_moments=MM,trial_centroid=mul(1/VV,MM),trial_closure_residual=value,trial_mass_exactly_closed=value==Z))
 output.write_bytes(B(data));print('EXACT_SINGLE_POINT_MASS_QUARTIC_BUILT',len(B(data)),SHA(B(data)),flush=True)
 print('visible',len(visible),'t_trial',float(t0),'poly',[float(x) for x in polynomial],flush=True)
 print('target_delta',[float(x) for x in sub(mul(1/VV,MM),c0)],flush=True)
if __name__=='__main__':run(Path(sys.argv[1]),Path(sys.argv[2]))
