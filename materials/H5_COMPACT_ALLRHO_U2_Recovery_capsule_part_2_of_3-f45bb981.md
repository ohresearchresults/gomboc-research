# material-f45bb981ef51

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# H5_COMPACT_ALLRHO_11PARAMETER_U2_V1 — Recovery capsule part 2/3

All three ordered parts are required. Part 1 contains the common manifest, pins, commands and allroot_stress.py. This part contains taylor_tube.py in full. Part 3 contains tube_cover.py. Save the fence as taylor_tube.py, UTF-8/LF with final newline: 6643 bytes, SHA256 69d4c0318b54a89827cf922b338fbf9c8490f5065f75423e05e6900b5afb8902. Here the local argument named rho is the compact coordinate ell=rho_physical/(1+rho_physical), not the original physical ratio. The mapping is explicit; no earlier exact object is aliased.

```python
#!/usr/bin/env python3
"""H5 compactified ALL-rho actual-refill Taylor boxes; exact acceptance."""
from allroot_stress import *
import argparse
N=11
RAW_ACTUAL=actual
def actual(theta=THETA,rho=F(3,5),s=F(0),t=F(0)):
 # Here rho is compact coordinate lambda; the seed locator in allroot_stress
 # retains its own original physical-rho globals. No shape is silently aliased.
 assert 0<rho<1
 h=1-rho
 X,C,Q,V,g=RAW_ACTUAL(theta,rho/h,s*h,t*h)
 d=(h,h,F(1))
 return (tuple(tuple(v[i]*d[i] for i in range(3)) for v in X),
         tuple(tuple(C[i][j]*d[i]*d[j] for j in range(3)) for i in range(3)),
         tuple(tuple(v[i]/d[i] for i in range(3)) for v in Q),
         V*h*h,tuple(g[i]*d[i] for i in range(3)))
RADII=tuple(map(F,('1/100','1/100','1/100','1/200','1/100','1/100','1/400','1/400')))
class TM:
 __slots__=('c','a','r')
 def __init__(self,c,a=None,r=F(0)):
  self.c=F(c);self.a=tuple(map(F,a)) if a is not None else (F(0),)*N;self.r=F(r)
  assert self.r>=0 and len(self.a)==N
 @staticmethod
 def var(c,d,k):
  a=[F(0)]*N;a[k]=F(d);return TM(c,a)
 def __add__(self,y):
  if not isinstance(y,TM):y=TM(y)
  return TM(self.c+y.c,tuple(a+b for a,b in zip(self.a,y.a)),self.r+y.r)
 __radd__=__add__
 def __neg__(self):return TM(-self.c,tuple(-a for a in self.a),self.r)
 def __sub__(self,y):
  if self is y:return TM(0)
  return self+-y if isinstance(y,TM) else self+(-F(y))
 def __rsub__(self,y):return -self+y
 def dev(self):return sum(abs(a) for a in self.a)+self.r
 def __mul__(self,y):
  if not isinstance(y,TM):
   y=F(y);return TM(self.c*y,tuple(a*y for a in self.a),self.r*abs(y))
  r=abs(self.c)*y.r+abs(y.c)*self.r+self.dev()*y.dev()
  return TM(self.c*y.c,tuple(self.c*b+y.c*a for a,b in zip(self.a,y.a)),r)
 __rmul__=__mul__
 def recip(self):
  d=self.dev();c=abs(self.c);assert d<c
  return TM(1/self.c,tuple(-a/self.c**2 for a in self.a),self.r/c**2+d*d/(c*c*(c-d)))
 def __truediv__(self,y):return self*y.recip() if isinstance(y,TM) else self*(1/F(y))

def compile_box(lo,hi,mult=F(1)):
 assert 0<=lo<=hi<=1 and 0<mult<=1
 b,c,p,q,a,d,u,v=[TM.var(x,mult*h,k) for k,(x,h) in enumerate(zip(THETA,RADII))]
 rho=TM.var((lo+hi)/2,(hi-lo)/2,8);s=TM.var(0,mult/200,9);t=TM.var(0,mult/200,10)
 h=1-rho
 Y=((h*b,0,0),(h*c,0,0),(h*(1-p),h*p,0),(h*q,h*(1-q),0),(0,h*d,0),(0,h*a,0),(h*u,h*v,0),(0,0,1),(rho,0,1),(0,rho,1))
 Z=[]
 for y in Y:
  y=tuple(z if isinstance(z,TM) else TM(z) for z in y)
  h=(1+s*y[0]+t*y[1]).recip();Z.append(tuple(z*h for z in y))
 o=Z[7];V=TM(0);J=[TM(0) for _ in range(3)]
 # Exactly the nine genuine nonzero tetrahedra. Other boundary fans lie
 # identically in a plane containing the fixed apex, also after projectivity.
 for fi in (0,3,4,5):
  f=FACETS[fi]
  for k in range(1,len(f)-1):
   z=[o,Z[f[0]],Z[f[k]],Z[f[k+1]]]
   w=det([sub(v,o) for v in z[1:]])/6
   V=V+w
   h=tuple(sum(v[j] for v in z) for j in range(3))
   J=[x+w*y/4 for x,y in zip(J,h)]
 ij=tuple((i,j) for a,b in EDGES for i,j in ((a,b),(b,a)))
 rr=[]
 for i,j in ij:
  a=tuple(V*z-h for z,h in zip(Z[i],J));d=sub(Z[j],Z[i])
  # Numerators of physical sym[(Zi-g)(Zj-Zi)^T], doubled offdiagonals.
  rr.append((a[0]*d[0],a[1]*d[1],a[2]*d[2],a[0]*d[1]+a[1]*d[0],a[0]*d[2]+a[2]*d[0],a[1]*d[2]+a[2]*d[1]))
 # Independent point identity at the box centre; no approximation in checker.
 X,C,Q,vv,g=actual(rho=(lo+hi)/2)
 assert V.c==vv
 assert tuple(x.c for x in J)==scale(g,vv)
 for e,r in zip(ij,rr):assert tuple(z.c for z in r)==scale(row(X,*e),vv)
 return ij,rr,V

def weighted(rr,ids,terms):
 poly=[[F(0)]*6 for _ in range(N+1)];err=[F(0)]*6
 for i,j,w in terms:
  w=F(w);assert w>0
  for k,x in enumerate(rr[ids[(i,j)]]):
   poly[0][k]-=w*x.c
   for n,a in enumerate(x.a):poly[n+1][k]-=w*a
   err[k]+=w*x.r
 return tuple(matrix(p) for p in poly),matrix(err)

def congruence(H,A):
 return tuple(tuple(sum(H[i][k]*A[k][l]*H[j][l] for k in range(3) for l in range(3)) for j in range(3)) for i in range(3))

def accept(rr,ids,terms,H):
 H=tuple(tuple(F(x) for x in row) for row in H);assert det(H)!=0
 A,E=weighted(rr,ids,terms);Q=[congruence(H,a) for a in A]
 E=congruence(tuple(tuple(abs(x) for x in row) for row in H),E)
 margins=[]
 for i in range(3):
  j,k=[z for z in range(3) if z!=i]
  for s,t in product((-1,1),repeat=2):
   z=Q[0][i][i]-s*Q[0][i][j]-t*Q[0][i][k]
   z-=sum(abs(q[i][i]-s*q[i][j]-t*q[i][k]) for q in Q[1:])
   z-=E[i][i]+E[i][j]+E[i][k]
   if z<=0:return False
   margins.append(z)
 return min(margins)

def numerical(rr):
 import numpy as np
 pp=np.zeros((len(rr),N+1,3,3));er=np.zeros((len(rr),3,3))
 for e,r in enumerate(rr):
  for n in range(N+1):pp[e,n]=np.array(matrix(tuple(x.c if n==0 else x.a[n-1] for x in r)),float)
  er[e]=np.array(matrix(tuple(x.r for x in r)),float)
 return pp,er

def template(A):
 import numpy as np
 try:return np.linalg.inv(np.linalg.cholesky(A))
 except np.linalg.LinAlgError:return None

def margin_float(P,E,H):
 import numpy as np
 Q=np.einsum('ik,nkl,jl->nij',H,P,H);R=abs(H)@E@abs(H).T
 value=1e100
 for i in range(3):
  j,k=[z for z in range(3) if z!=i]
  for s,t in product((-1,1),repeat=2):
   z=Q[:,i,i]-s*Q[:,i,j]-t*Q[:,i,k]
   value=min(value,z[0]-sum(abs(z[1:]))-sum(R[i]))
 return value

def proof_H(H):
 return [[str(F(float(x)).limit_denominator(10**6)) for x in row] for row in H]

def probe(lo,hi,mult=F(1),source='recovered/primal_search.json'):
 import numpy as np
 start=time.time();ij,rr,V=compile_box(lo,hi,mult);ids={e:k for k,e in enumerate(ij)};pp,er=numerical(rr)
 trees=np.array([sum(1<<ids[e] for e in t) for r,t in rooted_trees(10,EDGES)],np.uint64)
 db=json.loads(Path(source).read_text())['certificates'];covered=np.zeros(len(trees),bool);good=[];margins=[]
 for no,terms in enumerate(db):
  ks=[ids[(i,j)] for i,j,w in terms];w=np.array([float(F(w)) for i,j,w in terms]);P=-np.einsum('e,enij->nij',w,pp[ks]);E=np.einsum('e,eij->ij',w,er[ks]);H=template(P[0])
  if H is None:continue
  m=margin_float(P,E,H);margins.append(m)
  if m<=1e-8:continue
  HH=proof_H(H)
  assert accept(rr,ids,terms,HH)
  mask=sum(1<<k for k in ks);covered|=(trees&np.uint64(mask))==mask;good.append({'terms':terms,'H':HH})
 out={'lo':str(lo),'hi':str(hi),'mult':str(mult),'volume_bound':str(V.c-V.dev()),'covered':int(sum(covered)),'certificates':good}
 Path('probe.json').write_text(jdump(out))
 print('PROBE',lo,hi,mult,'covered',sum(covered),'good',len(good),'VMIN',float(V.c-V.dev()),'margins',np.percentile(margins,[0,10,50,90,100]),'seconds',time.time()-start,flush=True)
 return out

if __name__=='__main__':
 if sys.argv[1]=='probe':probe(F(sys.argv[2]),F(sys.argv[3]),F(sys.argv[4]) if len(sys.argv)>4 else F(1))
 else:raise ValueError('probe LO HI [MULT]')
```
