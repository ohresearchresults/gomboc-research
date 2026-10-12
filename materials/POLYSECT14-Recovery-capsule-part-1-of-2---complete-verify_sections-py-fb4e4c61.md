# material-fb4e4c61fa42

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""Exact recovery for variable-radius polynomial circular sections.
CPython 3.13.5 standard library only. No external inputs or numerical tests.
Run: python -B -S verify_sections.py
Every claim is about a smooth solid, NOT an accepted target polyhedron.
"""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import json,hashlib

def trim(p):
 p=list(map(Q,p))
 while len(p)>1 and p[-1]==0:p.pop()
 return p

def add(p,q):return trim([(p[i] if i<len(p) else 0)+(q[i] if i<len(q) else 0) for i in range(max(len(p),len(q)))])
def scale(c,p):return trim([c*x for x in p])
def sub(p,q):return add(p,scale(-1,q))
def mul(p,q):
 r=[Q(0)]*(len(p)+len(q)-1)
 for i,x in enumerate(p):
  for j,y in enumerate(q):r[i+j]+=x*y
 return trim(r)
def power(p,n):
 r=[Q(1)]
 for _ in range(n):r=mul(r,p)
 return r
def der(p):return trim([i*p[i] for i in range(1,len(p))] or [0])
def shift(p):return [Q(0)]+p
def ev(p,x):
 r=Q(0)
 for a in reversed(p):r=r*x+a
 return r
def moment(p):return sum((c/Q(2*i+1) for i,c in enumerate(p)),Q(0))
def bernstein(p):
 n=len(p)-1
 return [sum((p[k]*Q(comb(i,k),comb(n,k)) for k in range(i+1)),Q(0)) for i in range(n+1)]
def split(b):
 rows=[b]
 while len(rows[-1])>1:rows.append([(a+c)/2 for a,c in zip(rows[-1],rows[-1][1:])])
 return [r[0] for r in rows],[r[-1] for r in reversed(rows)]
def positive(p):
 leaves=[]
 def visit(b,lo,hi,depth):
  if min(b)>0:
   leaves.append(dict(interval=[lo,hi],coefficients=b,lower_bound=min(b)));return
  assert depth<50 and b[0]>0 and b[-1]>0,('not certified',lo,hi,depth)
  l,r=split(b);m=(lo+hi)/2;visit(l,lo,m,depth+1);visit(r,m,hi,depth+1)
 visit(bernstein(p),Q(0),Q(1),0)
 return leaves

def coefficients(a,p1,q,B):
 H=mul([1,-1],power(B,2))
 P=[a,a*p1,Q(0)]
 # Exact volume-weighted first moment; the free quadratic coefficient.
 P[2]=-moment(mul(H,P))/moment(shift(shift(H)))
 return P,scale(a,q),H

def certify(name,a,p1,q,B,lam):
 P,Qp,H=coefficients(a,p1,q,B)
 assert a==P[0] and 0<a<1 and B[0]==1 and lam>0
 assert moment(mul(H,P))==0
 D=add(power(P,2),shift(power(Qp,2)));R=mul(H,D)
 J=add(add([0,lam*lam],H),D)
 Hp=der(H);Hpp=der(Hp)
 A=sub(add(mul(H,Hp),scale(2,shift(mul(H,Hpp)))),shift(power(Hp,2)))
 N=add(scale(2,der(P)),scale(4,shift(der(der(P)))))
 L=add(scale(6,der(Qp)),scale(4,shift(der(der(Qp)))))
 K=sub(power(A,2),mul(power(H,3),add(power(N,2),shift(power(L,2)))))
 Rp=der(R);W=sub(power(Rp,2),mul(R,power(der(J),2)))
 polynomials=dict(B=B,D=D,minus_Rprime=scale(-1,Rp),W=W,minus_A=scale(-1,A),curvature_gap=K)
 certificates={k:positive(p) for k,p in polynomials.items()}
 # At tips a smooth nonradial axis normal; at the equator the two criticals.
 assert ev(D,Q(1))>0 and ev(H,Q(1))==0 and ev(Hp,Q(1))<0
 volume_over_pi=2*lam*moment(H)
 assert volume_over_pi>0
 radial_at_equator=[1+a,1-a]
 jp=ev(der(J),Q(0));rp=ev(Rp,Q(0))
 fplus=jp+rp/a;fminus=jp-rp/a
 assert fplus<0<fminus
 result=dict(object=name,kind='smooth_uniform_convex_solid_NOT_polyhedron',parameters=dict(a=a,p1=p1,qshape=q,B=B,lam=lam),P=P,Q=Qp,H=H,D=D,R=R,J=J,A=A,polynomials=polynomials,certificates=certificates,volume_over_pi=volume_over_pi,centroid=[0,0,0],critical_U=[0,1+a,0],critical_S=[0,a-1,0],radial_ratio=(1-a)/(1+a),equator_y_derivatives=[fplus,fminus],weak_additional=0)
 return result

def plain(x):
 if isinstance(x,Q):return str(x)
 if isinstance(x,dict):return {k:plain(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [plain(v) for v in x]
 return x

def save(r):
 name=r['object']+'.json';b=json.dumps(plain(r),sort_keys=True,separators=(',',':')).encode()
 Path(name).write_bytes(b);print(name,len(b),hashlib.sha256(b).hexdigest())
 print('POLYNOMIAL_CIRCULAR_SECTIONS_EXACT_PASS',r['object'],'ratio',r['radial_ratio'],'leaves',{k:len(v) for k,v in r['certificates'].items()})

def boundary(r,t,e):
 assert sum(z*z for z in e)==1 and -1<=t<=1
 x=2*t/(1+t*t);y=x*x;rho=(1-t*t)/(1+t*t)*ev(r['parameters']['B'],y)
 return (r['parameters']['lam']*x,ev(r['P'],y)+rho*e[0],x*ev(r['Q'],y)+rho*e[1])

def tangent(r,point):
 lam=r['parameters']['lam'];x=point[0]/lam;y=x*x
 dy=point[1]-ev(r['P'],y);dz=point[2]-x*ev(r['Q'],y)
 assert dy*dy+dz*dz==ev(r['H'],y)
 px=2*x*ev(der(r['P']),y);qx=ev(r['Q'],y)+2*y*ev(der(r['Q']),y)
 n=(-(dy*px+dz*qx+x*ev(der(r['H']),y))/lam,dy,dz)
 return n,sum(a*b for a,b in zip(n,point))

if __name__=='__main__':
 # Arithmetic-simple constant-radius multiplier, with a rational axial scale.
 r=certify('POLYSECT14_AXIAL_V1',Q(1,14),Q(-279,40),[Q(77,20),Q(-37,5),Q(10,7)],[Q(1)],Q(497,500))
 save(r)
 # Genuinely variable radius multiplier; all nominal values are rational.
 r=certify('POLYSECT14_VARIABLE_V1',Q(1,14),Q(-151,22),[Q(724,189),Q(-536,75),Q(185,159)],[Q(1),Q(1,170)],Q(125,126))
 save(r)
 for t in [Q(-1),Q(-3,4),Q(0),Q(2,5),Q(1)]:
  for e in [(Q(1),Q(0)),(Q(3,5),Q(4,5))]:tangent(r,boundary(r,t,e))
 print('VARIABLE_RADIUS_SECTIONS_SELF_CONTAINED_RECOVERY_PASS')
