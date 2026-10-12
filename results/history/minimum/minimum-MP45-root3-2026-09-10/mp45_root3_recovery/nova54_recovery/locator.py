"""MP9 numerical proposals only; acceptance is exact integer positivity.
The log-det routines reproduce the authenticated journal V2 engine.
CPython 3.13.5 / NumPy 2.3.5 / SciPy 1.17.0; one BLAS thread.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import sys,warnings,itertools,functools
from fractions import Fraction as F
from math import gcd,lcm
import numpy as np
import scipy
from scipy.linalg import solve
assert __debug__ and sys.version_info[:3]==(3,13,5)
assert np.__version__=='2.3.5' and scipy.__version__=='1.17.0'
warnings.filterwarnings('ignore')
FS=[]
def fan(a,s):
 out=[]
 for f in FS:
  if a in f:continue
  j=s%len(f);f=f[j:]+f[:j]
  out.extend((a,f[0],f[k],f[k+1]) for k in range(1,len(f)-1))
 return out

def sym(a,b):return (np.outer(a,b)+np.outer(b,a))/2

def locate(parent,fans,eps=1e-7,maxouter=12):
 n=len(parent);A=len(fans);E=np.eye(n);I=np.eye(n)
 nodes=[i for i in range(n)if parent[i]!=i]
 S=[sym(E[i],E[i]-E[parent[i]])for i in nodes];m=len(S)
 K=[sym(E[i],E[j])for i in range(n)for j in range(i,n)];d=len(K);k=sum(map(len,fans))
 nl=A*n;ls=np.arange(nl,nl+k*m);ns=nl+k*m;N=ns+(A-1)*d+1;mu=N-1
 x=np.zeros(N);x[ls]=1/(k*m);x[mu]=-1;B=np.zeros(N);B[ls]=1
 mats=[];bi=[];tidx=0
 for a,ts in enumerate(fans):
  for t in ts:
   w=E[list(t)].sum(0);ix=list(range(a*n,(a+1)*n))+list(range(nl+tidx*m,nl+(tidx+1)*m))
   L=[sym(e,w)for e in E]+S;tidx+=1
   if a<A-1:ix+=list(range(ns+a*d,ns+(a+1)*d));L+=K
   else:
    for j in range(A-1):ix+=list(range(ns+j*d,ns+(j+1)*d));L+=[-Q for Q in K]
   bi.append(np.array(ix+[mu]));mats.append(np.array(L+[-I]))
 def calc(x,tau,hess=True):
  if min(x[ls])<=0:return None
  f=-x[-1]-tau*np.log(x[ls]).sum()
  if hess:
   g=np.zeros(N);g[-1]=-1;g[ls]=-tau/x[ls]
   H=np.zeros((N,N));H[ls,ls]=tau/x[ls]**2
  for ix,L in zip(bi,mats):
   Q=np.einsum('a,aij->ij',x[ix],L)
   try:R=np.linalg.cholesky(Q)
   except np.linalg.LinAlgError:return None
   f-=2*tau*np.log(np.diag(R)).sum()
   if hess:
    W=np.linalg.solve(Q,I);WL=np.einsum('ij,ajk->aik',W,L)
    g[ix]-=tau*np.trace(WL,axis1=1,axis2=2)
    H[np.ix_(ix,ix)]+=tau*np.einsum('aij,bji->ab',WL,WL)
  return (f,g,H)if hess else f
 for it in range(maxouter):
  tau=.05*.18**it
  for j in range(70):
   out=calc(x,tau)
   if out is None:return None
   f,g,H=out;Z=np.zeros((N+1,N+1));Z[:N,:N]=H;Z[N,:N]=B;Z[:N,N]=B
   rhs=np.r_[-g,1-B@x]
   try:p=solve(Z,rhs,assume_a='sym',check_finite=False)[:N]
   except Exception:p=np.linalg.lstsq(Z,rhs,rcond=1e-14)[0][:N]
   decr=-g@p
   if decr<min(1e-7,tau*.001):break
   al=1.;nn=p[ls]<0
   if nn.any():al=min(al,.99*np.min(-x[ls][nn]/p[ls][nn]))
   for _ in range(60):
    xx=x+al*p;ff=calc(xx,tau,False)
    if ff is not None and ff<=f+.05*al*(g@p):break
    al*=.5
   else:return x
   x=xx
  if x[-1]>eps or tau*(k*n+k*m)<eps:break
 return x

def merged_problem(p,fs,extra_rel=None):
 n=9; E=np.eye(n); I=E.copy(); A=len(fs)
 nodes=[i for i in range(n)if p[i]!=i]
 S=[sym(E[i],E[i]-E[p[i]])for i in nodes]
 K=[sym(E[i],E[j])for i in range(n)for j in range(i,n)]
 ts=sorted(set(tuple(sorted(t))for f in fs for t in f));tt={t:i for i,t in enumerate(ts)}
 ft=np.zeros((A,len(ts)))
 for a,f in enumerate(fs):
  for t in f:ft[a,tt[tuple(sorted(t))]]=1
 # rowspace of centroid equations to reduce free variables
 from scipy.linalg import qr
 _,rr,pp=qr(ft.T,pivoting=True,mode='economic');rk=np.linalg.matrix_rank(rr)
 ft=ft[pp[:rk]]; A=len(ft)
 if extra_rel is None:rel=ft[:-1]-ft[-1]
 else:rel=extra_rel
 # reduce mass constraints
 if len(rel):
  _,rr,pp=qr(rel.T,pivoting=True,mode='economic');rk=np.linalg.matrix_rank(rr)
  rel=rel[pp[:rk]]
 k=len(ts);d=45; nl=A*n;ls=np.arange(nl,nl+k*8);ns=nl+k*8;N=ns+len(rel)*d+1;mu=N-1
 x=np.zeros(N);x[ls]=1/(k*8);x[-1]=-1;B=np.zeros(N);B[ls]=1
 mats=[];bi=[]
 for t,tet in enumerate(ts):
  w=E[list(tet)].sum(0);ix=[];L=[]
  for a in range(A):
   if ft[a,t]:ix+=list(range(a*n,(a+1)*n));L+=[ft[a,t]*sym(e,w)for e in E]
  ix+=list(range(nl+t*8,nl+(t+1)*8));L+=S
  for s,r in enumerate(rel):
   if r[t]:ix+=list(range(ns+s*d,ns+(s+1)*d));L += [r[t]*q for q in K]
  bi.append(np.array(ix+[mu]));mats.append(np.array(L+[-I]))
 return x,B,ls,bi,mats,(ts,ft,rel)

def shared_locate(prob,eps=1e-8,maxouter=14):
 x,B,ls,bi,mats,_=prob;x=x.copy();N=len(x);n=9;I=np.eye(n);k=len(mats)
 def calc(x,tau,hess=True):
  if min(x[ls])<=0:return None
  f=-x[-1]-tau*np.log(x[ls]).sum()
  if hess:
   g=np.zeros(N);g[-1]=-1;g[ls]=-tau/x[ls]
   H=np.zeros((N,N));H[ls,ls]=tau/x[ls]**2
  for ix,L in zip(bi,mats):
   Q=np.einsum('a,aij->ij',x[ix],L)
   try:R=np.linalg.cholesky(Q)
   except np.linalg.LinAlgError:return None
   f-=2*tau*np.log(np.diag(R)).sum()
   if hess:
    W=np.linalg.solve(Q,I);WL=np.einsum('ij,ajk->aik',W,L)
    g[ix]-=tau*np.trace(WL,axis1=1,axis2=2)
    H[np.ix_(ix,ix)]+=tau*np.einsum('aij,bji->ab',WL,WL)
  return (f,g,H)if hess else f
 for it in range(maxouter):
  tau=.05*.18**it
  for j in range(70):
   out=calc(x,tau)
   if out is None:return None
   f,g,H=out;Z=np.zeros((N+1,N+1));Z[:N,:N]=H;Z[N,:N]=B;Z[:N,N]=B
   rhs=np.r_[-g,1-B@x]
   try:p=solve(Z,rhs,assume_a='sym',check_finite=False)[:N]
   except Exception:p=np.linalg.lstsq(Z,rhs,rcond=1e-14)[0][:N]
   decr=-g@p
   if decr<min(1e-7,tau*.001):break
   al=1.;nn=p[ls]<0
   if nn.any():al=min(al,.99*np.min(-x[ls][nn]/p[ls][nn]))
   for _ in range(60):
    xx=x+al*p;ff=calc(xx,tau,False)
    if ff is not None and ff<=f+.05*al*(g@p):break
    al*=.5
   else:return x
   x=xx
  if x[-1]>eps or tau*(k*n+len(ls))<eps:break
 return x

def addcov(prob):
 x,B,ls,bi,ms,info=prob;ts,ft,rel=info
 cv=ft[:-1]-ft[-1];N=len(x);ncv=len(cv);nz=np.zeros(ncv)
 X=np.r_[x[:-1],nz,x[-1]];BB=np.r_[B[:-1],nz,B[-1]]
 BBi=[];MM=[]
 for u,t in enumerate(ts):
  w=np.array([int(i in t)for i in range(9)]);J=np.outer(w,w)+np.diag(w)
  ix=list(bi[u][:-1])+list(range(N-1,N-1+ncv))+[N-1+ncv]
  L=np.concatenate([ms[u][:-1],np.array([c[u]*J for c in cv]),ms[u][-1:]])
  BBi.append(np.array(ix));MM.append(L)
 return X,BB,ls,BBi,MM,info

def kernel(rows,n):
 a=[list(map(F,r))for r in rows];pivs=[];r=0
 for j in range(n):
  k=next((k for k in range(r,len(a))if a[k][j]),None)
  if k is None:continue
  a[r],a[k]=a[k],a[r];z=a[r][j];a[r]=[v/z for v in a[r]]
  for i in range(len(a)):
   if i!=r and a[i][j]:
    z=a[i][j];a[i]=[u-z*v for u,v in zip(a[i],a[r])]
  pivs.append(j);r+=1
  if r==len(a):break
 out=[]
 for j in range(n):
  if j in pivs:continue
  v=[F(0)]*n;v[j]=F(1)
  for i,k in enumerate(pivs):v[k]=-a[i][j]
  den=lcm(*(x.denominator for x in v));w=[int(x*den)for x in v];gg=gcd(*w);w=[x//gg for x in w]
  if next(x for x in w if x)!=abs(next(x for x in w if x)):w=[-x for x in w]
  assert all(sum(x*y for x,y in zip(row,w))==0 for row in rows)
  out.append(w)
 return out

@functools.lru_cache(None)
def data(faces,spec):
 fs=[[(a,)+f for f in faces if a not in f]for a in spec]
 ts=sorted({tuple(sorted(t))for f in fs for t in f});tr=list(itertools.combinations(range(9),3));ti={t:i for i,t in enumerate(tr)};sig={}
 for f in fs:
  for t in f:
   s=(-1)**sum(t[i]>t[j]for i in range(4)for j in range(i+1,4));key=tuple(sorted(t));assert key not in sig or sig[key]==s;sig[key]=s
 R=[[0]*len(ts)for _ in tr]
 for j,t in enumerate(ts):
  for k in range(4):R[ti[t[:k]+t[k+1:]]][j]=sig[t]*(-1)**k
 rel=kernel(R,len(ts))
 return fs,ts,rel

def cycle_problem(p,faces):
 n=9;E=np.eye(n);I=E.copy();nodes=[i for i in range(n)if p[i]!=i];root=next(i for i in range(n)if p[i]==i)
 fs,ts,re=data(tuple(map(tuple,faces)),tuple(range(9)));rel=np.array(re,dtype=int)
 ft=np.vstack([[int(t in {tuple(sorted(u))for u in fs[root]})for t in ts],rel]);A=len(ft)
 S=[sym(E[i],E[i]-E[p[i]])for i in nodes];K=[sym(E[i],E[j])for i in range(n)for j in range(i,n)]
 k=len(ts);d=45;nl=A*n;ls=np.arange(nl,nl+k*8);ns=nl+k*8;nc=len(rel);N=ns+nc*d+nc+1;mu=N-1
 x=np.zeros(N);x[ls]=1/(k*8);x[-1]=-1;B=np.zeros(N);B[ls]=1;mats=[];bi=[]
 for t,tet in enumerate(ts):
  w=E[list(tet)].sum(0);ix=[];L=[]
  for a in range(A):
   if ft[a,t]:ix+=list(range(a*n,(a+1)*n));L+=[ft[a,t]*sym(e,w)for e in E]
  ix+=list(range(nl+t*8,nl+(t+1)*8));L+=S
  for s,r in enumerate(rel):
   if r[t]:ix+=list(range(ns+s*d,ns+(s+1)*d));L += [r[t]*q for q in K]
  J=np.outer(w,w)+np.diag(w)
  for s,r in enumerate(rel):
   if r[t]:ix.append(ns+nc*d+s);L.append(r[t]*J)
  bi.append(np.array(ix+[mu]));mats.append(np.array(L+[-I]))
 return x,B,ls,bi,mats,(ts,ft,rel)

def integer_matrices(rec,ff):
    p=rec['parent'];r=rec['root'];z=rec['z'];A=len(ff)
    shared=rec['kind']!='ordinary';cycle=rec['kind']=='cycle';volume=rec['kind']in('volume','cycle')
    if shared:
        ts=sorted({tuple(sorted(t))for f in ff for t in f})
        ft=[[int(t in{tuple(sorted(u))for u in f})for t in ts]for f in ff]
        inst=[(None,t)for t in ts]
        if cycle:
            assert rec['fans']==[[a,0]for a in range(9)]
            ft=[ft[r]]+rec['relations'];A=len(ft)
    else:inst=[(a,t)for a,f in enumerate(ff)for t in f]
    rel=rec.get('relations');nr=len(rel)if volume else A-1;ns=9*A+8*len(inst)
    assert len(z)==ns+45*nr+(A-1 if shared else 0) and min(z[9*A:ns])>=0
    Ks=[];at=ns
    for _ in range(nr):
        K=[[0]*9 for _ in range(9)]
        for i in range(9):
            for j in range(i,9):K[i][j]=K[j][i]=z[at]*(2 if i==j else 1);at+=1
        Ks.append(K)
    for u,(a,t)in enumerate(inst):
        w=[int(i in t)for i in range(9)]
        if shared:
            g=[sum(ft[b][u]*z[9*b+i]for b in range(A))for i in range(9)]
            hs=[row[u]for row in rel]if volume else[ft[b][u]-ft[-1][u]for b in range(A-1)]
            cc=sum(z[at+b]*rel[b][u]for b in range(nr))if cycle else sum(z[at+b]*(ft[b][u]-ft[-1][u])for b in range(A-1))
        else:g=z[9*a:9*a+9];hs=[int(a==b)-int(a==A-1)for b in range(A-1)];cc=0
        Q=[[g[i]*w[j]+g[j]*w[i]+sum(h*K[i][j]for h,K in zip(hs,Ks))+2*cc*(w[i]*w[j]+int(i==j)*w[i])for j in range(9)]for i in range(9)]
        for i,lm in zip([i for i in range(9)if i!=r],z[9*A+8*u:9*A+8*(u+1)]):
            Q[i][i]+=2*lm;Q[i][p[i]]-=lm;Q[p[i]][i]-=lm
        yield Q

def quick_pd(Q):
    a=[r[:]for r in Q];prev=1
    for i in range(9):a[i][i]-=1
    for k in range(9):
        d=a[k][k];assert d>0
        for i in range(k+1,9):
            for j in range(k+1,9):
                u=d*a[i][j]-a[i][k]*a[k][j];assert u%prev==0;a[i][j]=u//prev
        prev=d

def make_record(g,r,p,kind,spec,power,expected_sel,generic=False):
    global FS
    FS=g['facets']if g is not None else []
    if generic:fs=[[(0,)+t for t in itertools.combinations(range(1,9),3)]]
    else:fs=[fan(a,0)for a in spec]
    sel=spec;rel=None
    if kind=='cycle':
        assert spec==list(range(9));pr=cycle_problem(p,FS);rel=pr[-1][2];x=shared_locate(pr,eps=1e-8,maxouter=14)
    elif kind=='ordinary':x=locate(p,fs,eps=1e-7,maxouter=11)
    else:
        if kind=='volume':
            fs,ts,re=data(tuple(map(tuple,FS)),tuple(spec));pr=merged_problem(p,fs,extra_rel=np.array(re))
        else:pr=merged_problem(p,fs)
        ts,ft,rel=pr[-1];A=len(ft);assert A>=2
        orig=[[int(tuple(t)in{tuple(sorted(u))for u in f})for t in ts]for f in fs]
        sel=[spec[orig.index(row)]for row in ft.astype(int).tolist()]
        pr=addcov(pr);x=shared_locate(pr,eps=1e-8,maxouter=14)
        if kind=='shared'and x is not None:
            want=(ft[:-1]-ft[-1]).astype(int).tolist();old=rel.astype(int).tolist()
            order=[old.index(row)for row in want];assert len(order)==len(old)
            ns=9*A+8*len(ts);x=x.copy()
            x[ns:ns+45*(A-1)]=x[ns:ns+45*(A-1)].reshape(A-1,45)[order].ravel()
    assert x is not None and np.all(np.isfinite(x)) and(expected_sel is None or sel==expected_sel)
    sc=max(abs(float(v))for v in x[:-1]);z=[round(float(v)/sc*10**power)for v in x[:-1]]
    rec=dict(root=r,parent=list(p),kind=kind,fans=[[a,0]for a in sel],z=z)
    if kind in('volume','cycle'):rec['relations']=rel.astype(int).tolist()
    ff=fs if generic else [fan(a,0)for a in sel]
    for Q in integer_matrices(rec,ff):quick_pd(Q)
    return rec
