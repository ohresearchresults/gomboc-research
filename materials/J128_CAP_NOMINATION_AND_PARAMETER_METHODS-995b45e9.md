# material-995b45e9a20d

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# J128 complete numerical nomination and parameter-discovery sources

These source units accompany exact recovery material [internal-source-reference], J128_EXACT_CAP_CHARTS_AND_MASS_CLOSED_SIMPLEX.md. That material supplies the literal DETACHED_G6.txt and the complete rational RESEARCH128.py. None of these floating methods establishes an exact equilibrium census, a global optimum, or a family exclusion. No record is advanced. The rationalized SCOUT48_G8 and balanced-simplex data and proofs are reconstructed and exactly checked by the accompanying material independently of rerunning these floating searches.

Executed environment: Python3.13.5, NumPy2.3.5, SciPy1.17.0, OPENBLAS_NUM_THREADS=1. Save each complete fenced unit under its indicated filename. Run `python explore.py` to regenerate base.npz. For the actual one-apex nomination use `python apex_scan.py` then `python apex_opt.py`. Optional geometric discovery: `python envelope.py`, `python flower_probe.py`, `python cap_trial.py`, `python balanced_probe.py`, `python balanced_probe211.py`, `python metric_bound.py`. The balanced211 probe selected faces [5,38,45], [34,36,46], [39,44,43], relative height .001 and rho .05; exact generation uses the rational projector formula, not a saved approximate NPZ. The extra probes preserve the actual exploratory methods, not additional accepted results.

The corrected 30000-proposal scout (seed1282026) was rerun and returned 353 floating U1 outside nominations. Its leading S2 candidate has apex approximately (-.09934332053208299,.44086278118560795,.010039875113306174), Q~.46076247742545295, nominal V48/E138/F92. Exact rounding to (-9934332,44086278,1003988)/1e8 is SCOUT48_G8 from the exact capsule. No own110 was nominated. This is a finite heuristic result, not an exact exclusion of all30000 bodies. A previous program test wrongly used vertex count47 to reject no-change hulls, thereby also rejecting hulls in which the new apex retired one old vertex. The preserved source instead tests whether submitted apex47 belongs to H.vertices, and the entire reported scout was rerun after that correction. Earlier counts are not authoritative.

The 20 SLSQP continuations use all-point physical witness maxima at actual mass, fixed retained root6, epsilon1e-10 and explicit parameters below. The saved best feasible pilot was floating S4/U1 with Q approximately (.4521641292280636,.0006747744826187674,.00019964013174944562), apex(-.14187161695545208,.3969619626746279,.025191185946854877). It is fragmented, not a better whole-Q cancellation. It was not promoted to an exact body. The numerical bar routine has a1e-12 floor and must not be used to certify absence of positive defects. Numerical E is the triangulated general-position upper bound3V-6; the exact capsule counts the actual maximal facets and edges.

Source bytes/SHA256:
- explore.py 1136; 89eb6a1691e0da4108a2634353961acfd941afbec0e8998cb7fb8e231d888176
- apex_scan.py 3204; 19ea75e5e561a0eb13fffb37835d462573f54a559c08cc72b3c7543bc858a038
- apex_opt.py 1260; 9956ece534ef1cc0d9bdfdb6b46b913aaaf49854cc3f611bd0be52cfea31925d
- cap_trial.py 1735; a18c118c6dcf75313b874afdcc70fc15f49e79e0595ba8707eeb3d6f1c1cbcc0
- balanced_probe.py 1874; 44d777d89d02f05cbd8de49ab3bfa81e715f9385d0f50441befc0d78cbb1dff4
- balanced_probe211.py 1905; c70aa6e8cf0e5d5fc29c0c0338008825c5f46e5eebf4092c67d81ae105a87fa6
- metric_bound.py 871; 857b1ecfb782328c28339c5b192179fd5390224d1534c48334ed8f764ae07a1e
- envelope.py 1071; 654fbf314ace6a296daba51b2a7d94817da865496550b1b881c57270dc7afd18
- flower_probe.py 1149; 44df46c409d923decd4a58eeb1f88a565bc3f0f284725cf86662456948abe668

Observed deterministic-report receipts in that environment: apex_scan_result.json7817 bytes, SHAaa6b751ef7f40c0658b4304f13ab9e6931e9f1bf641c9d559d0a96fc880f58fc; apex_opt_result.json12448 bytes, SHA28903f0f3d384087aa04a2278f2531b4309dd03a36aedca91b8c00d3c966619a. Floating optimizer results need not be bit-identical on another numerical stack. Exact body recovery does not depend on them.

## File: explore.py
```python
import numpy as np, scipy, scipy.spatial as ss
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
p=Path(__file__).with_name('DETACHED_G6.txt');raw=p.read_bytes()
assert len(raw)==1034 and sha256(raw).hexdigest()=='a5b7cb7cd10de4a8ba08a997945ee3a932385cf03a5e259946be867954772a50'
X=np.loadtxt(p,skiprows=1)/1000000
V0=F(4052900436758915819,6000000000000000000)
g0=np.array([float(F(38946985201102467703899,2315943106719380468000000)),float(F(36285365677586521554829,4052900436758915819000000)),float(F(-276840702507758878921281,8105800873517831638000000))])
Y=X-g0
H=ss.ConvexHull(X);N=H.equations[:,:3];h=-H.equations[:,3]-N@g0
Z=N/h[:,None]
U=np.flatnonzero(np.max(Y@Y.T-(Y*Y).sum(1)[:,None]-np.eye(len(Y))*1e10,axis=1)<0)
S=np.flatnonzero(np.max(Z@Z.T-(Z*Z).sum(1)[:,None]-np.eye(len(Z))*1e10,axis=1)<0)
print('versions',np.__version__,scipy.__version__)
print('shape',X.shape,'volume',H.volume,'g',g0,'U',U,'S',[(i,H.simplices[i].tolist(),h[i])for i in S])
print('farthest',U, np.linalg.norm(Y,axis=1).max())
np.savez(p.with_name('base.npz'),X=X,Y=Y,g=g0,N=N,h=h,Z=Z,faces=H.simplices,S=S,U=U)
```

## File: apex_scan.py
```python
import json,time
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
B=np.load(Path(__file__).with_name('base.npz'));X=B['X'];g0=B['g'];Y=B['Y'];N=B['N'];h=B['h'];faces=B['faces'];r=np.linalg.norm(Y,axis=1);V=ConvexHull(X).volume
area=np.linalg.norm(np.cross(X[faces[:,1]]-X[faces[:,0]],X[faces[:,2]]-X[faces[:,0]]),axis=1)/2
bc=X[faces].mean(1);d=h+N@g0
D=X[None,:,:]-X[:,None,:];old0=np.einsum('ik,ijk->ij',X,D);old0[np.diag_indices(len(X))]=-np.inf

def mass(A):
 mu=np.maximum(A@N.T-d,0)*area/3;VV=V+mu.sum(1)
 M=V*g0+mu@(3*bc)/4+mu.sum(1)[:,None]*A/4
 return VV,M/VV[:,None],mu

def countU(A,G):
 old=old0[None,:,:]-np.einsum('nk,ijk->nij',G,D)
 score=np.max(old,axis=2);da=A[:,None,:]-X
 score=np.maximum(score,np.einsum('nik,nik->ni',X[None,:,:]-G[:,None,:],da))
 newscore=np.max(np.einsum('nk,nik->ni',A-G,-da),axis=1)
 return (score<0).sum(1)+(newscore<0),score,newscore

def state(a):
 H=ConvexHull(np.vstack([X,a]));vv,g,_=mass(a.reshape(1,3));g=g[0];Z=H.equations[:,:3]/(-H.equations[:,3]-H.equations[:,:3]@g)[:,None]
 if 47 not in H.vertices:return None
 AA=Z@Z.T-(Z*Z).sum(1)[:,None];np.fill_diagonal(AA,-np.inf);S=np.flatnonzero(AA.max(1)<0)
 # Polar edges correspond to adjacent primal facets.
 edges=set()
 for i,row in enumerate(H.neighbors):
  for j in row:
   if j>=0:edges.add(tuple(sorted((i,int(j)))))
 radii=(Z*Z).sum(1);links=[]
 for i,j in edges:
  dx=Z[j]-Z[i];tt=np.clip(-Z[i]@dx/(dx@dx),0,1);lev=np.dot(Z[i]+tt*dx,Z[i]+tt*dx);links.append((float(lev),i,j))
 parent=list(range(len(Z)));peak=radii.copy();bars=[]
 def root(a):
  while parent[a]!=a:parent[a]=parent[parent[a]];a=parent[a]
  return a
 for lev,i,j in sorted(links,reverse=True):
  p,q=root(i),root(j)
  if p==q:continue
  if peak[p]<peak[q]:p,q=q,p
  bar=1-lev/peak[q]
  if bar>1e-12:bars.append(bar)
  parent[q]=p
 return {'S':len(S),'Q':sorted(bars,reverse=True),'V':len(H.vertices),'E':3*len(H.vertices)-6,'g':g.tolist(),'vol':float(vv[0]),'a':a.tolist()}

def run(num=30000):
 rng=np.random.default_rng(1282026);A=[];k=num//3
 # Material witness-ball proposals, deliberately including several radial shells.
 ids=rng.integers(0,len(X),k);u=rng.normal(size=(k,3));u/=np.linalg.norm(u,axis=1)[:,None]
 A.append(g0+Y[ids]/2+.5*r[ids,None]*(rng.uniform(.8,1,k)[:,None])*u)
 for scale in [1.05,2.5]:
  u=rng.normal(size=(k,3));u/=np.linalg.norm(u,axis=1)[:,None];A.append(g0+scale*r.max()*rng.random(k)[:,None]**(1/3)*u)
 A=np.vstack(A);accepted=[];counts={};start=time.time()
 for off in range(0,len(A),500):
  Z=A[off:off+500];vv,g,mu=mass(Z);outside=mu.sum(1)>1e-12
  cnt,old,new=countU(Z,g)
  for c in cnt[outside]:counts[str(c)]=counts.get(str(c),0)+1
  use=np.flatnonzero((cnt==1)&outside)
  for i in use:
   s=state(Z[i]);
   if s is not None:accepted.append(s)
 print('scout',len(A),'seconds',time.time()-start,'outside_U_counts',counts,'U1outside',len(accepted),flush=True)
 accepted.sort(key=lambda z:(z['S'],sum(z['Q'])))
 print('best',accepted[:3],flush=True)
 Path(__file__).with_name('apex_scan_result.json').write_text(json.dumps({'seed':1282026,'proposals':len(A),'U_counts':counts,'U1':len(accepted),'best':accepted[:20]},indent=2)+'\n')
if __name__=='__main__':run()
```

## File: apex_opt.py
```python
from apex_scan import *
from scipy.optimize import minimize
saved=json.loads(Path(__file__).with_name('apex_scan_result.json').read_text())
starts=[z['a']for z in saved['best']]
root=6;keep=np.array([i for i in range(47)if i!=root])
best=None;outputs=[];st=time.time()

def cons(a):
 _,g,_=mass(a.reshape(1,3));cnt,old,new=countU(a.reshape(1,3),g)
 return np.r_[old[0,keep],new[0]]-1e-10

def fun(a):
 try:
  s=state(a)
  if s is None:return .46246611091319517
  return sum(s['Q'])
 except Exception:return 5.
for i,a in enumerate(starts):
 z=minimize(fun,np.array(a),method='SLSQP',constraints={'type':'ineq','fun':cons},bounds=[(-2,2)]*3,options={'maxiter':250,'ftol':1e-12,'eps':1e-7})
 s=state(z.x);mm=float(min(cons(z.x)))
 outputs.append({'start':i,'message':z.message,'success':bool(z.success),'nfev':z.nfev,'min_guard_minus_epsilon':mm,'state':s})
 if s is not None and mm>=-1e-10 and (best is None or sum(s['Q'])<sum(best['Q'])):best=s
 print('opt',i,z.success,'guard',mm,'S',None if s is None else s['S'],'Q',None if s is None else s['Q'],'seconds',time.time()-st,flush=True)
Path(__file__).with_name('apex_opt_result.json').write_text(json.dumps({'root':6,'epsilon':1e-10,'outputs':outputs,'best':best},indent=2)+'\n')
print('BEST',best,flush=True)
```

## File: envelope.py
```python
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import minimize, differential_evolution
from pathlib import Path
b=np.load(Path(__file__).with_name('base.npz'));Y=b['Y'];N=b['N'];h=b['h'];S=b['S'];r=np.linalg.norm(Y,axis=1)
ns=N[S];print('S normals',ns,'angle',np.arccos(ns[0]@ns[1])*180/np.pi)
def supp(n,m):
 n=np.array(n)/np.linalg.norm(n)
 th=np.arccos(np.clip(Y@n/r,-1,1))
 return float(np.max(r*np.cos(th/(m+1))**(m+1)))
for m in range(1,7):print('m',m,'at roots',[supp(n,m)for n in ns])

def circle_r(w):
 w=np.asarray(w);w=w/np.linalg.norm(w)
 e=np.eye(3)[np.argmin(np.abs(w))];e=np.cross(w,e);e/=np.linalg.norm(e);f=np.cross(w,e)
 hull=ConvexHull(np.column_stack([Y@e,Y@f]));return float(np.min(-hull.equations[:,-1]))
w=ns[1]-ns[0];w/=np.linalg.norm(w)
print('hemisphere best initial',w,circle_r(w))
for i in range(2):
 for m in [1,2,3]:
  opt=minimize(lambda v:supp(v,m),ns[i],method='Nelder-Mead',options={'maxiter':600,'xatol':1e-10,'fatol':1e-12})
  v=opt.x/np.linalg.norm(opt.x)
  print('free env min',i,m,v,opt.fun,'dotw',v@w)
```

## File: flower_probe.py
```python
import numpy as np
from scipy.optimize import minimize, linprog
from pathlib import Path
b=np.load(Path(__file__).with_name('base.npz'));Y=b['Y'];r=np.linalg.norm(Y,axis=1)
ns=[np.array([.356792,-.93132955,.07297077]),np.array([-.42784698,.85837802,.28307973])]
for z in ns:
 opt=minimize(lambda v:np.max((r+Y@(v/np.linalg.norm(v)))/2),z,method='Nelder-Mead',options={'maxiter':2500,'xatol':1e-12,'fatol':1e-14});n=opt.x/np.linalg.norm(opt.x);vals=(r+Y@n)/2;t=max(vals);act=np.flatnonzero(t-vals<1e-7)
 A=Y[act]/2+r[act,None]*n/2
 sol=linprog(np.zeros(len(act)),A_eq=np.r_[np.ones((1,len(act))),A.T],b_eq=np.r_[1,t*n],bounds=(0,None),method='highs')
 print('normal',n,'t',t,'hK',max(Y@n),'active',act,'lambda',sol.x if sol.success else sol.message)
 if sol.success:
  m=sol.x@A;print('m',m,'flowergap',m@m-max(Y@m),'new witnessboundaryguards',np.max(A@Y.T-(A*A).sum(1)[:,None],axis=1))
  A2=Y[act]/2+.49*r[act,None]*n
  m2=sol.x@A2
  print('inner m',m2,'gap',m2@m2-max(Y@m2),'newguards',np.max(A2@Y.T-(A2*A2).sum(1)[:,None],axis=1))
  np.savez(Path(__file__).with_name('flower_example_'+str(act[0])+'.npz'),normal=n,act=act,weights=sol.x,A=A2,m=m2)
```

## File: cap_trial.py
```python
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
b0=np.load(Path(__file__).with_name('base.npz'));X=b0['X'];g0=b0['g'];V=ConvexHull(X).volume

def census(X):
 H=ConvexHull(X);T=X[H.simplices];cr=np.cross(T[:,1]-T[:,0],T[:,2]-T[:,0]);sg=np.sign((cr*H.equations[:,:3]).sum(1));T=T.copy();T[sg<0]=T[sg<0][:,[0,2,1]]
 det=np.einsum('ij,ij->i',T[:,0],np.cross(T[:,1],T[:,2]));VV=det.sum()/6;g=(det[:,None]*T.sum(1)).sum(0)/(24*VV)
 Y=X[H.vertices]-g;W=H.equations[:,:3]/(-H.equations[:,3]-H.equations[:,:3]@g)[:,None]
 def U(A):
  score=A@A.T-(A*A).sum(1)[:,None];np.fill_diagonal(score,-np.inf);return np.flatnonzero(np.max(score,axis=1)<-1e-11),np.max(score,axis=1)
 u,pu=U(Y);s,pq=U(W)
 return {'V':len(Y),'E':len(H.simplices)*3//2,'F':len(H.simplices),'U':H.vertices[u].tolist(),'S':[H.simplices[i].tolist()for i in s],'g':g.tolist(),'vol':VV,'min_nonroot_P':float(np.min(np.delete(pu,u)))}
for face in [[5,38,45],[5,34,46]]:
 T=X[face];bb=T.mean(0);nn=np.cross(T[1]-T[0],T[2]-T[0]);nn/=np.linalg.norm(nn)
 if nn@(bb-g0)<0:nn=-nn
 h=nn@(bb-g0);A=np.linalg.norm(np.cross(T[1]-T[0],T[2]-T[0]))/2
 for eta in [1e-3,1e-4,1e-5]:
  mu=A*eta*h/3;q=(V*g0+3*mu*bb/4)/(V+3*mu/4);d=nn@bb+eta*h;p=q+(d-nn@q)*nn
  for rho in [.1,.25,.5]:
   aa=p+rho*(T-bb);out=[census(np.vstack([X,a]))for a in [*aa,p]]
   print('face',face,'eta',eta,'rho',rho,'mu',mu,'counts',[(len(o['S']),len(o['U']))for o in out],'drifts',[float(np.max(np.abs(np.array(o['g'])-g0)))for o in out],flush=True)
   if all(len(o['U'])==1 for o in out[:3])and len(out[-1]['U'])>=2:
    np.savez(Path(__file__).with_name('cap_example.npz'),face=face,eta=eta,rho=rho,aa=aa,p=p,mu=mu,q=q)
    print('FIRSTCOUNTEREXAMPLE',out,flush=True);raise SystemExit
```

## File: balanced_probe.py
```python
exec(open(__file__.replace('balanced_probe.py','cap_trial.py')).read().split('for face in ')[0])
from itertools import combinations
H=ConvexHull(X);tris=H.simplices
primary=[5,38,45];T=X[primary];b=T.mean(0);n=np.cross(T[1]-T[0],T[2]-T[0]);n/=np.linalg.norm(n)
if n@(b-g0)<0:n=-n
eta=.001;mu0=np.linalg.norm(np.cross(T[1]-T[0],T[2]-T[0]))*eta*(n@(b-g0))/6
d=n@b+eta*(n@(b-g0));bases=[]
for tri in tris:
 if set(tri)&set(primary):continue
 F=X[tri];bi=F.mean(0);nn=np.cross(F[1]-F[0],F[2]-F[0]);nn/=np.linalg.norm(nn)
 if nn@(bi-g0)<0:nn=-nn
 hh=nn@(bi-g0);mu=np.linalg.norm(np.cross(F[1]-F[0],F[2]-F[0]))*eta*hh/6
 ai=bi+eta*hh*nn
 ee=F[1]-F[0];ee/=np.linalg.norm(ee);ff=np.cross(nn,ee)
 bases.append((mu,tri.tolist(),bi,nn,ai,np.column_stack([ee,ff])))
bases.sort(key=lambda t:-t[0]);found=False
for C1,C2 in combinations(bases[:30],2):
 m1,f1,b1,n1,a1,T1=C1;m2,f2,b2,n2,a2,T2=C2
 if set(f1)&set(f2):continue
 Mhost=V*g0+m1*(3*b1+a1)/4+m2*(3*b2+a2)/4;VV=V+m1+m2
 q=(Mhost+3*mu0*b/4)/(VV+3*mu0/4);p=q+(d-n@q)*n
 gstar=(Mhost+mu0*(3*b+p)/4)/(VV+mu0)
 C=np.c_[m1*T1,m2*T2];inv=np.linalg.pinv(C)
 for rho in [.02,.05,.1]:
  DD=rho*(T-b);shift=-(inv@(mu0*DD).T).T
  aa=[np.vstack([p+u,a1+T1@v[:2],a2+T2@v[2:]])for u,v in zip(DD,shift)]
  mids=np.vstack([p,a1,a2]);out=[census(np.vstack([X,Z]))for Z in aa+[mids]]
  drift=max(np.linalg.norm(np.array(o['g'])-gstar)for o in out)
  if all(len(o['U'])==1 for o in out[:3]) and len(out[-1]['U'])==2 and drift<1e-12 and all(o['V']==50 and o['F']==96 for o in out):
   print('FOUND',f1,f2,'rho',rho,'mu',mu0,m1,m2,'gstar',gstar,'gdrift',drift,'counts',[(len(o['S']),len(o['U']))for o in out]);print(out)
   np.savez(Path(__file__).with_name('balanced_example.npz'),faces=np.array([primary,f1,f2]),eta=eta,rho=rho,base=np.vstack([p,a1,a2]),shift=np.array(aa),gstar=gstar);found=True;break
 if found:break
if not found:print('NOTFOUND')
```

## File: balanced_probe211.py
```python
exec(open(__file__.replace('balanced_probe211.py','cap_trial.py')).read().split('for face in ')[0])
from itertools import combinations
H=ConvexHull(X);tris=H.simplices
primary=[5,38,45];T=X[primary];b=T.mean(0);n=np.cross(T[1]-T[0],T[2]-T[0]);n/=np.linalg.norm(n)
if n@(b-g0)<0:n=-n
eta=.001;mu0=np.linalg.norm(np.cross(T[1]-T[0],T[2]-T[0]))*eta*(n@(b-g0))/6
d=n@b+eta*(n@(b-g0));bases=[]
for tri in tris:
 if set(tri)&set(primary):continue
 F=X[tri];bi=F.mean(0);nn=np.cross(F[1]-F[0],F[2]-F[0]);nn/=np.linalg.norm(nn)
 if nn@(bi-g0)<0:nn=-nn
 hh=nn@(bi-g0);mu=np.linalg.norm(np.cross(F[1]-F[0],F[2]-F[0]))*eta*hh/6
 ai=bi+eta*hh*nn
 ee=F[1]-F[0];ee/=np.linalg.norm(ee);ff=np.cross(nn,ee)
 bases.append((mu,tri.tolist(),bi,nn,ai,np.column_stack([ee,ff])))
bases.sort(key=lambda t:-t[0]);found=False
for C1,C2 in combinations(bases[:30],2):
 m1,f1,b1,n1,a1,T1=C1;m2,f2,b2,n2,a2,T2=C2
 if set(f1)&set(f2):continue
 Mhost=V*g0+m1*(3*b1+a1)/4+m2*(3*b2+a2)/4;VV=V+m1+m2
 q=(Mhost+3*mu0*b/4)/(VV+3*mu0/4);p=q+(d-n@q)*n
 gstar=(Mhost+mu0*(3*b+p)/4)/(VV+mu0)
 C=np.c_[m1*T1,m2*T2];inv=np.linalg.pinv(C)
 for rho in [.05,.1,.15,.2,.3,.4]:
  DD=rho*(T-b);shift=-(inv@(mu0*DD).T).T
  aa=[np.vstack([p+u,a1+T1@v[:2],a2+T2@v[2:]])for u,v in zip(DD,shift)]
  mids=np.vstack([p,a1,a2]);out=[census(np.vstack([X,Z]))for Z in aa+[mids]]
  drift=max(np.linalg.norm(np.array(o['g'])-gstar)for o in out)
  if all(len(o['U'])==1 and len(o['S'])==2 for o in out[:3]) and len(out[-1]['U'])==2 and drift<1e-12 and all(o['V']==50 and o['F']==96 for o in out):
   print('FOUND',f1,f2,'rho',rho,'mu',mu0,m1,m2,'gstar',gstar,'gdrift',drift,'counts',[(len(o['S']),len(o['U']))for o in out]);print(out)
   np.savez(Path(__file__).with_name('balanced_example.npz'),faces=np.array([primary,f1,f2]),eta=eta,rho=rho,base=np.vstack([p,a1,a2]),shift=np.array(aa),gstar=gstar);found=True;break
 if found:break
if not found:print('NOTFOUND')
```

## File: metric_bound.py
```python
from apex_scan import *
Bfaces=np.einsum('ni,nj->nij',bc,area[:,None]*N)/4
Sfaces=(Bfaces+Bfaces.transpose(0,2,1))/2
upper=np.maximum(Sfaces,0).sum(0);lower=np.minimum(Sfaces,0).sum(0)
G=np.diag(upper).copy()+np.sum(np.maximum(np.abs(upper),np.abs(lower)),axis=1)-np.diag(np.maximum(np.abs(upper),np.abs(lower)))
P=np.zeros((3,3))
for m in Sfaces:
 e,U=np.linalg.eigh(m);P+=(U*np.maximum(e,0))@U.T
print('V',V,'sumB',Bfaces.sum(0),'Gershgorin allsubset rows',G,'bound',max(G),'spectralP',np.linalg.eigvalsh(P))
# Vertex-based recentering is immaterial for the restricted constant-volume plane: B changes by rank one along a.
bcc=bc-g0
Bc=np.einsum('ni,nj->nij',bcc,area[:,None]*N)/4;Sc=(Bc+Bc.transpose(0,2,1))/2
u=np.maximum(Sc,0).sum(0);l=np.minimum(Sc,0).sum(0);ab=np.maximum(abs(u),abs(l));GG=np.diag(u)+ab.sum(1)-np.diag(ab)
print('centred allsubset Gershgorin',GG)
```
