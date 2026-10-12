# material-5ef7761abe1e

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# J131 Recovery capsule part 1 of 3

Object family: J131_PARALLEL_100, J131_PARALLEL_010, J131_PARALLEL_001 and their exact mass-preserving paths; J131 four-chart local rank test. These are three own211 nonwinners, NOT a new own110 record. Parts1 and2 together contain the complete deterministic exact reconstruction. Part3 preserves the numerical producing methods and their finite-failure scope; it is not needed to reconstruct the frozen exact objects. All units below are complete literal UTF-8 files, including their terminal newline. No originating sandbox is required.

The exact parent input is the standalone DETACHED_G6 source from material [internal-source-reference] (J130 source SHA6d97f53e2309152267578dca8c280cb9a7469c93b0756d6d8e9ea8ffdbd41a15), rather than an inferred reconstruction of a worker workspace. The input is repeated here because it is necessary for this complete runnable successor. Qhull only nominates triangular faces: every supporting, incidence, mass and equilibrium sign in the endpoint audit is rational. There is one exact Fraction implementation, not independent dual verification.

Save each named code block as that filename in one directory; also save the named units from part2. Reconstruction and verification commands:

```sh
OPENBLAS_NUM_THREADS=1 python cert131.py
OPENBLAS_NUM_THREADS=1 python atlas131.py
```

Observed environment: CPython3.13.5, NumPy2.3.5, SciPy1.17.0. These versions nominate the same strictly triangular lattice. Exact computations use fractions.Fraction; the numerical routines are imported but no optimizer runs during the two reconstruction commands.

Source identities (bytes/SHA256):
- DETACHED_G6.txt 1034 / a5b7cb7cd10de4a8ba08a997945ee3a932385cf03a5e259946be867954772a50
- engine131.py 5318 / 57c193dfbdc155935de187e4c6b01f0115bd1dba1c65d89b383076abd0c7f63a
- parallel131.py 5151 / c57594109a3b9a91cc4f90f2404bf4b7b59b65893c01e923abedd1310d4e4057

## File: DETACHED_G6.txt
```text
47 1000000
-220660 -170809 739992
-470733 -252568 617724
-344429 -201140 695040
-827617 -345105 -7630
-804956 -306141 -196980
-617752 -310722 484546
-802871 -391980 208231
708441 212327 -26773
629324 353053 -32544
109721 -76616 760640
306556 -32243 700380
212446 -60072 735986
469379 -34257 598089
392685 -40271 652622
646907 -14969 394808
537342 -31849 536185
596588 -24705 468240
750839 45997 64966
-102855 -139962 763378
7557 -112190 768796
719082 11448 235222
687865 -2839 316832
740239 27161 150766
750330 69885 -21314
738230 84890 -114933
592447 240452 -366643
659702 196951 -280592
707333 140337 -199650
700973 -34829 -222306
-736323 -274563 -374807
228858 452552 -370941
60624 561672 -200802
142319 490402 -325534
566004 -68026 -372688
612214 -197888 -188679
464617 500011 -71398
-487325 -442504 -463527
552036 118367 -435356
-19326 554813 -63048
350712 442484 -390884
577522 340656 -272794
199735 530859 -305689
-532859 -303654 -567337
-484871 -149126 -645284
472985 292300 -459118
-416022 64364 111262
-193306 -303834 71494
```

## File: engine131.py
```python
#!/usr/bin/env python3
"""Exact triangular convex hull, filled mass and equilibrium audit for J131.
Qhull nominates faces only. Every supporting/incidence/equilibrium sign is exact.
This is a single Fraction implementation, not an independent pair of engines.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
import numpy as np
from scipy.spatial import ConvexHull
R=Path(__file__).resolve().parent
O=F(0)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(s,a):return tuple(s*x for x in a)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),O)
def cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def serial(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {str(k):serial(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [serial(v) for v in x]
 if isinstance(x,np.integer):return int(x)
 if isinstance(x,np.ndarray):return serial(x.tolist())
 return x

def write(name,x):
 b=(json.dumps(serial(x),indent=2)+'\n').encode();(R/name).write_bytes(b)
 return dict(name=name,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())

def load():
 b=(R/'DETACHED_G6.txt').read_bytes()
 assert len(b)==1034 and hashlib.sha256(b).hexdigest()=='a5b7cb7cd10de4a8ba08a997945ee3a932385cf03a5e259946be867954772a50'
 w=list(map(int,b.split()));N,D=w[:2]
 return [tuple(F(t,D)for t in w[2+3*i:5+3*i])for i in range(N)]

def hull(X):
 h=ConvexHull(np.array([[float(a) for a in p] for p in X]));fs=[]
 for tt in h.simplices:
  t=list(map(int,tt));a,b,c=[X[i] for i in t];n=cross(sub(b,a),sub(c,a));sg=[dot(n,sub(p,a))for p in X]
  if max(sg)>0:
   assert min(sg)>=0,'Nominated facet not exactly supporting';t[1],t[2]=t[2],t[1]
  j=t.index(min(t));fs.append(tuple(t[j:]+t[:j]))
 fs=sorted(fs);assert len(fs)==len(set(fs));hs=[];es={}
 for fi,t in enumerate(fs):
  a,b,c=[X[i] for i in t];n=cross(sub(b,a),sub(c,a));hh=dot(n,a);sg=[dot(n,p)-hh for p in X]
  assert max(sg)==0 and sum(z==0 for z in sg)==3,'Nontriangular or nonstrict hull'
  hs.append((n,hh))
  for j in range(3):es.setdefault(tuple(sorted((t[j],t[(j+1)%3]))),[]).append(fi)
 assert all(len(x)==2 for x in es.values());es=dict(sorted(es.items()));vs=sorted({i for t in fs for i in t})
 assert len(vs)-len(es)+len(fs)==2
 seen={0};todo=[0]
 while todo:
  k=todo.pop()
  for j in range(3):
   for f in es[tuple(sorted((fs[k][j],fs[k][(j+1)%3])))]:
    if f not in seen:seen.add(f);todo.append(f)
 assert len(seen)==len(fs)
 return fs,hs,es,vs

def mass(X,fs):
 V=O;M=(O,O,O)
 for a,b,c in fs:
  d=det(X[a],X[b],X[c]);V+=d/6;M=add(M,mul(d/24,add(add(X[a],X[b]),X[c])))
 assert V>0
 return V,M,mul(1/V,M)

def persistence(X,edges):
 rad=[dot(p,p)for p in X];par=list(range(len(X)));peak=rad[:];links=[];out=[]
 def root(i):
  while par[i]!=i:par[i]=par[par[i]];i=par[i]
  return i
 for a,b in edges:
  d=sub(X[b],X[a]);t=max(O,min(F(1),-dot(X[a],d)/dot(d,d)))
  level=dot(add(X[a],mul(t,d)),add(X[a],mul(t,d)));links.append((level,a,b))
 for level,i,j in sorted(links,reverse=True):
  a,b=root(i),root(j)
  if a==b:continue
  if peak[a]<peak[b]:a,b=b,a
  q=1-level/peak[b];assert q>=0
  if q>0:out.append(dict(root=b,edge=(i,j),birth=peak[b],death=level,depth=q))
  par[b]=a
 return sorted(out,key=lambda x:x['depth'],reverse=True)

def audit(X):
 fs,hs,es,vs=hull(X);V,M,g=mass(X,fs);Y=[sub(x,g)for x in X]
 S=[];U=[];H=[];weak=[[],[],[]];zero=[0,0,0]
 for fi,(t,(n,h))in enumerate(zip(fs,hs)):
  assert h-dot(n,g)>0
  sig=[dot(n,cross(Y[t[j]],Y[t[(j+1)%3]]))for j in range(3)];zero[0]+=sum(s==0 for s in sig)
  if min(sig)>0:S.append(fi)
  elif min(sig)>=0:weak[0].append(fi)
 nb=[[]for _ in X]
 for a,b in es:nb[a].append(b);nb[b].append(a)
 for i in vs:
  sig=[dot(Y[i],sub(Y[j],Y[i]))for j in nb[i]];zero[1]+=sum(s==0 for s in sig)
  if max(sig)<0:U.append(i)
  elif max(sig)<=0:weak[1].append(i)
 for (a,b),(i,j)in es.items():
  d=sub(Y[b],Y[a]);dd=dot(d,d);aa=-dot(Y[a],d);bb=dd-aa;p=add(Y[a],mul(aa/dd,d))
  n1,n2=hs[i][0],hs[j][0];g11,g12,g22=dot(n1,n1),dot(n1,n2),dot(n2,n2);D=g11*g22-g12*g12;assert D>0
  c1=dot(p,n1)*g22-dot(p,n2)*g12;c2=dot(p,n2)*g11-dot(p,n1)*g12
  assert mul(D,p)==add(mul(c1,n1),mul(c2,n2));sig=[aa,bb,c1,c2];zero[2]+=sum(s==0 for s in sig)
  if min(sig)>0:H.append((a,b))
  elif min(sig)>=0:weak[2].append((a,b))
 assert len(S)+len(U)-len(H)==2
 P=persistence(Y,es);Q=persistence([mul(1/(h-dot(n,g)),n)for n,h in hs],es.values())
 assert len(P)==len(U)-1 and len(Q)==len(S)-1
 return dict(V=len(vs),E=len(es),F=len(fs),strict=[len(S),len(U),len(H)],weak=list(map(len,weak)),primitive_zero=zero,S=[fs[i]for i in S],S_indices=S,U=U,H=H,P=P,Q=Q,volume=V,moment=M,centroid=g),fs

def rref(A):
 a=[list(r)for r in A];m=len(a);n=len(a[0]);row=0;piv=[]
 for j in range(n):
  k=next((k for k in range(row,m)if a[k][j]),None)
  if k is None:continue
  a[k],a[row]=a[row],a[k];z=a[row][j];a[row]=[v/z for v in a[row]]
  for k in range(m):
   if k==row:continue
   z=a[k][j]
   if z:a[k]=[v-z*u for v,u in zip(a[k],a[row])]
  piv.append(j);row+=1
  if row==m:break
 return a,piv

def lift_free(rr,piv,free,values):
 out=[O]*len(rr[0])
 for j,v in zip(free,values):out[j]=v
 for row,j in enumerate(piv):out[j]=-sum((rr[row][k]*out[k]for k in free),O)
 return out
```

## File: parallel131.py
```python
#!/usr/bin/env python3
"""J131 correlated parallel-vertex mass charts, exact and numerical nomination.
For fixed v and oriented triangles, p_i -> p_i+t_i*v has affine hull gaps,
affine V, and M=M0+L*t+v*(t.T B t). On A*t=0 fixing V and transverse
M, translate by -v*(ell*t+t.T B t)/V0. This is an EXACT polynomial
parametrization with the original V,M,g. Translation DOES NOT preserve
reference equilibrium guards; the actual centred guards below are cubic.
"""
import engine131 as e
from fractions import Fraction as F
import numpy as np
from scipy.linalg import null_space
O=F(0)

def exact_coefficients(X,fs,v):
 N=len(X);Vr=[O]*N;L=[[O]*N for _ in range(3)];B=[[O]*N for _ in range(N)]
 for a,b,c in fs:
  d=e.det(X[a],X[b],X[c]);ids=[a,b,c]
  bb=[e.det(v,X[b],X[c]),e.det(X[a],v,X[c]),e.det(X[a],X[b],v)]
  p=e.add(e.add(X[a],X[b]),X[c])
  for k,z in zip(ids,bb):
   Vr[k]+=z/6
   for j in range(3):L[j][k]+=p[j]*z/24
   for h in ids:B[k][h]+=z/48;B[h][k]+=z/48
  for k in ids:
   for j in range(3):L[j][k]+=d*v[j]/24
 kk=next(k for k in range(3)if v[k]);other=[j for j in range(3)if j!=kk]
 A=[Vr]+[[L[j][k]-v[j]*L[kk][k]/v[kk]for k in range(N)]for j in other]
 ell=[z/v[kk]for z in L[kk]]
 return A,ell,B,Vr,L

def retract(X,fs,v,t):
 A,ell,B,vr,L=exact_coefficients(X,fs,v)
 assert all(e.dot(a,t)==0 for a in A)
 V,M,g=e.mass(X,fs);q=e.dot(ell,t)+sum((t[i]*e.dot(B[i],t)for i in range(len(t))),O)
 shift=q/V;tt=[a-shift for a in t];Y=[e.add(p,e.mul(z,v))for p,z in zip(X,tt)]
 assert e.mass(Y,fs)==(V,M,g)
 return Y,shift,tt

class Chart:
 def __init__(self,X,fs,v,g=None):
  self.X=np.array(X,float);self.fs=np.array(fs,int);self.v=np.array(v,float);self.N=len(X)
  if g is None:
   raw=[tuple(F(str(a))for a in p)for p in X];vv,mm,gg=e.mass(raw,fs);self.V=float(vv);self.g=np.array(gg,float)
  else:self.V,self.g=g[0],np.array(g[1],float)
  self.P=self.X-self.g
  N=self.N;v=self.v;Vr=np.zeros(N);L=np.zeros((3,N));B=np.zeros((N,N))
  for a,b,c in fs:
   xx=self.X[[a,b,c]];d=np.dot(xx[0],np.cross(xx[1],xx[2]));ids=[a,b,c]
   bb=[np.dot(v,np.cross(xx[1],xx[2])),np.dot(xx[0],np.cross(v,xx[2])),np.dot(xx[0],np.cross(xx[1],v))]
   for k,z in zip(ids,bb):
    Vr[k]+=z/6;L[:,k]+=xx.sum(0)*z/24
    for h in ids:B[k,h]+=z/48;B[h,k]+=z/48
   for k in ids:L[:,k]+=d*v/24
  kk=np.argmax(abs(v));other=[j for j in range(3)if j!=kk]
  self.A=np.array([Vr]+[L[j]-v[j]*L[kk]/v[kk]for j in other]);self.ell=L[kk]/v[kk];self.B=B
  # Fix one gauge: the mean uncorrected height is zero. Uniform height is a
  # pure translation removed by the exact retraction; this loses no shape.
  AA=np.vstack([self.A,np.ones(N)]);AA/=np.linalg.norm(AA,axis=1)[:,None]
  self.T=null_space(AA);self.d=self.T.shape[1]
  fs=self.fs;a,b,c=fs.T
  self.n0=np.cross(self.P[b]-self.P[a],self.P[c]-self.P[a]);self.dn=np.zeros((len(fs),3,N))
  cB=np.cross(v,self.P[c]-self.P[a]);cC=np.cross(self.P[b]-self.P[a],v)
  for f in range(len(fs)):
   self.dn[f,:,b[f]]=cB[f];self.dn[f,:,c[f]]=cC[f];self.dn[f,:,a[f]]=-cB[f]-cC[f]
  self.HT=[];self.h0=[];self.hspec=[]
  for f,(a,b,c)in enumerate(fs):
   n=self.n0[f];nv=np.dot(n,v)
   for j in range(N):
    if j in(a,b,c):continue
    row=np.dot(self.P[j]-self.P[a],self.dn[f]);row[j]+=nv;row[a]-=nv
    self.HT.append(row);self.h0.append(np.dot(n,self.P[j]-self.P[a]));self.hspec.append((f,j))
  self.HT=np.array(self.HT);self.h0=np.array(self.h0)
  self.hscale=abs(self.h0)
  self.hjac=-self.HT@self.T/self.hscale[:,None]
  es={}
  for f,t in enumerate(fs):
   for k in range(3):es.setdefault(tuple(sorted((t[k],t[(k+1)%3]))),[]).append(f)
  self.es=es;self.nb=[[]for _ in X]
  for a,b in es:self.nb[a].append(b);self.nb[b].append(a)
  self.last=None

 def state(self,z):
  t=self.T@z;q=self.ell@t+t@self.B@t;delta=q/self.V;deltagrad=(self.ell+2*self.B@t)/self.V
  Y=self.P+(t-delta)[:,None]*self.v
  n=self.n0+np.einsum('fak,k->fa',self.dn,t)
  return t,Y,n,deltagrad

 def allguards(self,z):
  t,Y,n,dg=self.state(z);N=self.N;v=self.v;fs=self.fs
  U=np.zeros((N,N));dU=np.zeros((N,N,N,self.d)) if False else np.zeros((N,N,self.d))
  for i in range(N):
   for j in self.nb[i]:
    diff=Y[j]-Y[i];val=np.dot(Y[i],diff);grad=-dg*np.dot(v,diff);grad[i]+=np.dot(v,diff)-np.dot(Y[i],v);grad[j]+=np.dot(Y[i],v)
    U[i,j]=val;dU[i,j]=grad@self.T
  S=np.zeros((len(fs),3));dS=np.zeros((len(fs),3,self.d))
  for f,face in enumerate(fs):
   for k in range(3):
    a,b=face[k],face[(k+1)%3];cr=np.cross(Y[a],Y[b]);u=np.dot(n[f],np.cross(v,Y[b]));w=np.dot(n[f],np.cross(Y[a],v))
    grad=cr@self.dn[f]-(u+w)*dg;grad[a]+=u;grad[b]+=w
    S[f,k]=np.dot(n[f],cr);dS[f,k]=grad@self.T
  return U,dU,S,dS

 def hullguard(self,z):return -(self.h0+self.HT@(self.T@z))/self.hscale
 def bar(self,z,birth,edge):
  t,Y,n,dg=self.state(z);a=self.fs[:,0];h=np.einsum('fa,fa->f',n,Y[a]);nv=n@self.v
  dh=np.einsum('fa,fak->fk',Y[a],self.dn)-nv[:,None]*dg
  dh[np.arange(len(a)),a]+=nv
  Q=n/h[:,None];dQ=(self.dn/h[:,None,None]-n[:,:,None]*dh[:,None,:]/h[:,None,None]**2)@self.T
  i,j=edge;d=Q[j]-Q[i];tt=np.clip(-np.dot(Q[i],d)/np.dot(d,d),0,1);r=Q[i]+tt*d
  rd=np.dot(r,r);rb=np.dot(Q[birth],Q[birth]);dr=2*r@((1-tt)*dQ[i]+tt*dQ[j]);db=2*Q[birth]@dQ[birth]
  return 1-rd/rb,-dr/rb+rd*db/rb**2
```

IMPORTANT EXACT-TEXT CORRECTION TO THE BLOCK ABOVE: in parallel131.py the allguards allocation line must be the following literal line, replacing the single line containing `if False`. This exact replacement restores the stated 5151-byte source/SHA rather than defining a new source variant. No other substitution is needed.
```python
  U=np.zeros((N,N));dU=np.zeros((N,N,self.d))
```
