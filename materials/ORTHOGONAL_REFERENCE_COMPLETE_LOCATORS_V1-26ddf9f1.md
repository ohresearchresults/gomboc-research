# material-26ddf9f12814

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Complete auxiliary orthogonal-reference locator methods

These three complete source units materially guided the rational reference in [internal-source-reference]. They are numerical discovery methods, NOT proof or exact regional certification. Their only nonstandard source dependency is h5_hybrid_explore.py,2681B,SHA25685b8dd3efa42aeae02d3ae88a423c47a31ea57c07f9628e1557657c4f7b2e024, completely preserved in [internal-source-reference]. Save each block with the indicated filename and final LF. No randomness, hidden starting checkpoint, or external input is used; all numerical tolerances and nondefault parameters are literal. The rounded rational W in the exact theorem is now an explicit exact input, not a required floating output.

Versions actually used: CPython3.13.5,SymPy1.14.0,NumPy2.3.5,SciPy1.17.0. Original commands used OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1. Run the search and refine sources independently with python; their output path is explicitly /mnt/data, which must exist or be changed only as an output location. Reference refine has its starting five-parameter vector literally in the source and does not need a previous output file.

Original floating output pins identify the local numerical run, not a bitwise guarantee on every platform:
- orthogonal_reference_search.json12863B,SHA25647e8098ce96b83b321efff26d95e419f72cbf19501c95e6e9b84b09b391dd96f.
- orthogonal_reference_refine.json2890B,SHA256663fabdd598d52f6954f81424b461f76d8f3962d1df5ce929de31607a76eb945.

## orthogonal_pair_locator.py
3400B,SHA256bc0a1f905b8feff67a97d2ac8680d13e262d5ead108ffe6b5d22abee4dc57379.
```python
"""Finite true-edge-pair locator of the reference orthogonal shell coefficient.
Float discovery only. Exact certification is a separate rational calculation.
"""
import numpy as np
from numpy.polynomial import polynomial as pol
from h5_hybrid_explore import make,FACES

def edges():
    d={}
    for f,face in enumerate(FACES):
        for i,a in enumerate(face):
            b=face[(i+1)%len(face)];d.setdefault(tuple(sorted((a,b))),[]).append(f)
    assert len(d)==17 and all(len(v)==2 for v in d.values())
    return list(sorted(d)),[tuple(d[e]) for e in sorted(d)]

def scalars(v,q,C):
    Ci=np.linalg.inv(C);pe,qe=edges();best=(-1.,None)
    for ei,(i,j) in enumerate(pe):
        a=v[i];u=v[j]-a
        pp=np.array([a@Ci@a,2*a@Ci@u,u@Ci@u])
        for fi,(f,g) in enumerate(qe):
            n=q[f];b=q[g]-n
            A=a@n;B=u@n;dd=a@b;D=u@b
            scale=max(1,abs(A),abs(B),abs(dd),abs(D));tol=2e-12*scale
            def consider(s,t):
                nonlocal best
                if -1e-8<=s<=1+1e-8 and -1e-8<=t<=1+1e-8:
                    w=a+s*u;nn=n+t*b
                    if abs(w@nn)>1e-7*max(1,np.linalg.norm(w)*np.linalg.norm(nn)):return
                    val=(w@Ci@w)*(nn@C@nn)
                    if val>best[0]:best=(val,dict(primal_edge=[i,j],polar_edge=[f,g],s=float(s),t=float(t),pair=[ei,fi]))
            if abs(dd)<tol and abs(D)<tol:
                if abs(B)>tol:
                    s=-A/B;consider(s,0);consider(s,1)
                elif abs(A)<tol:
                    for s in [0,1]:
                        for t in [0,1]:consider(s,t)
                continue
            N0=dd*n-A*b;N1=D*n-B*b
            qq=np.array([N0@C@N0,2*N0@C@N1,N1@C@N1])
            P=pol.polymul(pp,qq)
            deriv=pol.polysub(pol.polymul(pol.polyder(P),[dd,D]),2*D*P)
            while len(deriv)>1 and abs(deriv[-1])<1e-12*max(1,np.max(np.abs(deriv))):deriv=deriv[:-1]
            roots=pol.polyroots(deriv) if len(deriv)>1 else []
            cuts=[0.,1.]
            for num,den in [(dd,D),(A,B),(A+dd,B+D)]:
                if abs(den)>tol:
                    s=-num/den
                    if 0<s<1:cuts.append(s)
            cuts=sorted(set(cuts))
            for s in cuts:
                den=dd+D*s
                if abs(den)>tol:consider(s,-(A+B*s)/den)
                elif abs(A+B*s)<tol:
                    consider(s,0);consider(s,1)
            for root in roots:
                if abs(root.imag)>1e-7:continue
                s=float(root.real);den=dd+D*s
                if abs(den)>tol:consider(s,-(A+B*s)/den)
    return best

def canonical(theta,g,k):
    h=1-g[2];m=np.array([theta[-1]/3]*2)-g[:2]
    D=np.array([[2.,-1.],[-1.,2.]])
    return np.block([[k*D+np.outer(m,m),(h*m)[:,None]],[(h*m)[None,:],np.array([[h*h]])]])

if __name__=='__main__':
    for l in [.087,.12,.2,.4]:
        theta=[.15,.15,.15,.45,l];z,v,q,g,S=make(theta,False)
        v=np.array(v,dtype=float)[:,:,0];q=np.array(q,dtype=float)[:,:,0];g=np.array(g,dtype=float)[:,0];S=np.array(S,dtype=float)
        Cs=[('covariance',S),('fixed',np.array([[296.,-103.,-122.],[-103.,271.,-112.],[-122.,-112.,422.]])),('canonical',canonical(theta,g,.15))]
        for label,C in Cs:
            Ci=np.linalg.inv(C);G=np.max(np.einsum('ij,jk,ik->i',v,Ci,v))*np.max(np.einsum('ij,jk,ik->i',q,C,q))
            print(theta,label,'Gamma',G,'orthogonal',scalars(v,q,C),flush=True)
```

## orthogonal_reference_search.py
2609B,SHA25623c296a365ab336b7c3dbe6e4815ef29a06c8e7ca35532b3b665f95da864a327.
```python
"""Deterministic sampled-pair reference locator; not a certificate.
Full edge-pair stationary-point evaluation is performed only on the final references.
"""
import json
import numpy as np
from scipy.optimize import minimize
from orthogonal_pair_locator import make,edges,scalars

def metric(t):
 a,b,c,d,e=t
 B=np.array([[np.exp(a),0.,0.],[c,np.exp(b),0.],[d,e,np.exp(-a-b)]])
 return B@B.T

def pairs(V,Q):
 pe,qe=edges();ww=[];nn=[]
 for i,j in pe:
  a=V[i];u=V[j]-a
  for f,g in qe:
   n=Q[f];b=Q[g]-n;A=a@n;B=u@n;C=a@b;D=u@b
   tol=1e-11*max(1,abs(A),abs(B),abs(C),abs(D))
   def save(s,t):
    if -1e-10<=s<=1+1e-10 and -1e-10<=t<=1+1e-10:
     w=a+s*u;q=n+t*b
     if abs(w@q)<1e-8*max(1,np.linalg.norm(w)*np.linalg.norm(q)):ww.append(w);nn.append(q)
   if abs(C)<tol and abs(D)<tol:
    if abs(B)>tol:
     for t in np.linspace(0,1,17):save(-A/B,t)
    elif abs(A)<tol:
     for s in [0,1]:
      for t in [0,1]:save(s,t)
    continue
   cand=list(np.linspace(0,1,17))
   for x,y in [(A,B),(C,D),(A+C,B+D)]:
    if abs(y)>tol:cand.append(-x/y)
   for s in cand:
    den=C+D*s
    if abs(den)>tol:save(s,-(A+B*s)/den)
    elif abs(A+B*s)<tol:
     for t in [0,1]:save(s,t)
 return np.array(ww),np.array(nn)

def loss(t,W,Q,top,qB):
 C=metric(t);Ci=np.linalg.inv(C)
 rr=np.einsum('ij,jk,ik->i',W,Ci,W);qq=np.einsum('ij,jk,ik->i',Q,C,Q)
 up=np.max(rr*qq)
 ch=np.maximum(0,np.einsum('ij,jk,ik->i',top,Ci,top)*(qB@C@qB)/(top@qB)**2-1)
 return np.log(up)+np.arcsinh(np.sqrt(ch.max()))

if __name__=='__main__':
 out=[]
 for lam in [.12,.15,.2]:
  theta=[.15,.15,.15,.45,lam];z,v,q,g,S=make(theta,False)
  v=np.array(v,dtype=float)[:,:,0];q=np.array(q,dtype=float)[:,:,0];S=np.array(S,dtype=float)
  eig,U=np.linalg.eigh(S);sr=(U*np.sqrt(eig))@U.T;si=np.linalg.inv(sr)
  V=v@si;Q=q@sr;W,QQ=pairs(V,Q)
  for root in ['all',7,8,9]:
   T=V[7:] if root=='all' else V[[root]]
   res=minimize(loss,np.zeros(5),args=(W,QQ,T,Q[0]),method='Powell',bounds=[(-2,2)]*5,options={'maxiter':150,'xtol':1e-8,'ftol':1e-9})
   C=sr@metric(res.x)@sr;up,wit=scalars(v,q,C);K=16/27*up**2;TT=v[7:] if root=='all' else v[[root]]
   chi=np.maximum(0,np.einsum('ij,jk,ik->i',TT,np.linalg.inv(C),TT)*(q[0]@C@q[0])/(TT@q[0])**2-1)
   L=((K+1)*np.sqrt(1+chi)+(K-1)*np.sqrt(chi))**2/(4*K)
   obj=dict(theta=theta,root=root,pair_count=len(W),parameters=res.x.tolist(),reference=C.tolist(),sampled_loss=float(res.fun),upsilon=float(up),witness=wit,chi=chi.tolist(),L=L.tolist(),nfev=res.nfev)
   out.append(obj);print(json.dumps(obj),flush=True)
 open('/mnt/data/orthogonal_reference_search.json','w').write(json.dumps(out,indent=2)+'\n')
```

## orthogonal_reference_refine.py
1378B,SHA25635ee0cd42d51f58c980d5eb642e750bc338287e19a5543a79223d92cacb431ef.
```python
"""Deterministic continuation of root9 orthogonal-reference locator; not proof."""
import json
import numpy as np
from scipy.optimize import minimize
from orthogonal_reference_search import make,pairs,loss,metric
from orthogonal_pair_locator import scalars
if __name__=='__main__':
 th=[.15,.15,.15,.45,.12];z,v,q,g,S=make(th,False)
 v=np.array(v,dtype=float)[:,:,0];q=np.array(q,dtype=float)[:,:,0];S=np.array(S,dtype=float)
 eig,U=np.linalg.eigh(S);sr=(U*np.sqrt(eig))@U.T;si=np.linalg.inv(sr);V=v@si;Q=q@sr;W,QQ=pairs(V,Q)
 t=np.array([-.006265451280554392,.0005519239960815055,-.12507245100039052,-.0233332980176664,.10705291024913849])
 out=[]
 for method in ['Nelder-Mead','Powell','Nelder-Mead']:
  opts={'maxiter':3000,'xatol':1e-11,'fatol':1e-11} if method=='Nelder-Mead' else {'maxiter':1000,'xtol':1e-10,'ftol':1e-11}
  r=minimize(loss,t,args=(W,QQ,V[[9]],Q[0]),method=method,options=opts)
  t=r.x;C=sr@metric(t)@sr;up,wit=scalars(v,q,C);K=16/27*up**2;a=v[9];ch=max(0,(a@np.linalg.inv(C)@a)*(q[0]@C@q[0])/(a@q[0])**2-1)
  L=((K+1)*np.sqrt(1+ch)+(K-1)*np.sqrt(ch))**2/(4*K)
  rec=dict(method=method,options=opts,parameters=t.tolist(),reference=C.tolist(),upsilon=float(up),chi=float(ch),L=float(L),witness=wit,nfev=r.nfev)
  out.append(rec);print(json.dumps(rec),flush=True)
 open('/mnt/data/orthogonal_reference_refine.json','w').write(json.dumps(out,indent=2)+'\n')
```
