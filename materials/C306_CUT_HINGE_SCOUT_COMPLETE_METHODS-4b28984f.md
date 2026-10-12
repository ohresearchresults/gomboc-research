# material-4b28984fd34e

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# C306 actual-filled-mass cut and whole-region hinge numerical methods

Complete runnable producer units are below. The exact input is the complete farthest_merged_G10000.json in immutable material [internal-source-reference], SHA f86dc15bccb15df88836b33a6d6852b2a33a1f66cc77168c4c51fb4a31af7f21. That material is an explicit required recovery dependency and must accompany this unit for workers. It contains the entire53point integer/10000 array,102oriented triangles and exact_tri_audit.py, not an external sandbox reference. Input2051bytes(no ending newline),SHA89599e0825f7075c151639b70d9db5959fcdc058c0be555d1a96d8598ccdea3e. No C318 geometry/indices are substituted.

The unchanged input was freshly checked: V53/E153/F102,C306,strict121,weak000,Sface0,Uinput0/14,H44–46,volume1690203202641/10^12,centroid(409355912737/135216256211280000,855529297349/67608128105640000,5154137003/270432512422560). C306_G4_EXACT.json346bytes SHA50939b89e946cb8c47c43bc07268489a44af1a48bc528f7b580d4e52e53adf61. No new exact body is promoted here.

## Executed finite experiments
cut_search.py scan: seed260919,6000attempted/6000valid,405(S,U)keys,minS1,minU2,min(S+U)3,noSU11. Best S1U2 merit k4552,z=(-.7332772778282877,.39058887864477154,.9887794112712907),n=(.6839660477811079,-.6161418451636856,.39058887864477154),h=.639854492015265,V70,F101,vol1.6881242144823971,c=(-.0006348431146914056,.00026234872954221237,-.0005046701689881132),all-pair bu=-.556053423630146,bs=.0011511781009169541. Optional cut DE mode was NOT run.

hinge_search.py scan: seed731919,6000attempted/6000valid,420(S,U)keys,minS2,minU2,min(S+U)4. Terminal HINGE_SCAN_DONE 6000 2 2 420. The physical body is the convex hull of all original vertices and original edge/plane intersections after x maps to x+v*max(0,n.x-h). The image union is NOT assumed convex: actual hull and ordinary volume centroid are rebuilt each time. This is a C306 whole-region experiment, not a claim that hinges are globally new; old near-record cut/hinge methods are in [internal-source-reference].

hinge_search.py joint: DE150iterations,48initial points chosen from scan,seed940919,then Nelder–Mead max2000iterations. Best update evaluation9481;merit.0022666191388286943,V68,F117,S2,U2,du7.246556891257765e-6,ds.00025937258193743645,mu.0026919243904140362,ms.01610504523177242,vol3.017018000412076,c=(-2.5799054211628825,-1.4607292844369943,.47170245888624907). Complete frozen six controls z=(-1.4164963695264179,-.5769244964450613,.10844451415152233,-2.545691688388401,-1.4766613096704861,.44410347553288076). H and weak features not exactly audited, so not an accepted222body.

All classifications float64/Qhull,facet equations grouped to9decimals and strict threshold1e-9. Numerical S/U are scouts, not exact acceptance; near-coalescent/mixed incidences need exact maximal hull. Local normalized escape can improve by coalescence. Positive all-pair rooted paths suffice for uniqueness; negative all-pair bottleneck is NOT a true-edge persistence barrier. These finite failures do not exclude multiple interfaces, root turnover, general cutting, or coupled mass deformations. C622 incumbent unchanged.

## Reconstruction and reproducibility
Restore exact input from the explicit immutable dependency into one directory and save both Python units below there with LF/one final newline. No missing source helpers exist. Run from this directory. Executed environment CPython3.13.5 GCC14.2.0,NumPy2.3.5,SciPy1.17.0,float64,OPENBLAS_NUM_THREADS=1. Floating optimization on another platform may vary; hashes are observed bytes, not geometric certificates.
```sh
OPENBLAS_NUM_THREADS=1 python -u cut_search.py scan > cut_scan.log
OPENBLAS_NUM_THREADS=1 python -u hinge_search.py scan > hinge_scan.log
OPENBLAS_NUM_THREADS=1 python -u hinge_search.py joint > hinge_joint.log
python - <<'PY'
import json
for f in ('cut_scan.json','hinge_scan.json'):
 a=json.load(open(f));r=a['records']
 assert a['attempted']==len(r)==6000
 assert not any(x['g']['S']==x['g']['U']==1 for x in r)
 print(f,min(x['g']['S'] for x in r),min(x['g']['U'] for x in r),len(a['best']))
a=json.load(open('hinge_joint.json'));assert a['g']['S']==a['g']['U']==2
print('C306_FINITE_CUT_HINGE_SCOUT_REPLAY_PASS')
PY
```
Expected CUT_SCAN_DONE6000(with405keys),HINGE_SCAN_DONE6000 2 2 420,HINGE_OPT_DONE(withS2U2),and C306_FINITE_CUT_HINGE_SCOUT_REPLAY_PASS. The last marker tests finite outcomes, not a general impossibility result. The final checking heredoc is supplied for replay; the original outcomes were inspected directly in the executed JSON/log files.

Observed filenames/bytes/SHA256:
- cut_search.py3937 71d96309d3f6f43c6f2895050d8f735cd4059c3671df77216ff49e18b9f4326f
- hinge_search.py4568 875db74467f5de4d44c5aea588283dd9c3e7999afca1587668c89e28136488dc
- cut_scan.json2572724 578c94b3a88295f9ba14c11b2cea5e3d51874fb42b0b839640ddb612bd7e155d
- cut_scan.log25015 f8ebe3b629a0379792a9789a0d15d1c24218a27f71e19bfe0d10211d9877b4a0
- hinge_scan.json2722137 45d88c7a3bbe358e1d21fc7f997a24e43d159be08298d84688889108ae7645ba
- hinge_scan.log29 f2fb1781b716d5f74fa9f16df89ae62247cd1f89c3485180aa832b2db52e8886
- hinge_joint.json6441 6a7350f79b7052cf2f248490acfb4293eebab0b8b9eeb980086f0815e43f0b6a
- hinge_joint.log20178 1dc8504925c3494fdfd5b1299b5f607c0f217c163ce2255f460cda3e1725d075
Large scan outputs are recreated by complete deterministic source rather than copied as bulk. Complete endpoint controls above permit direct evaluation without an optimizer run.

## cut_search.py
```python
"""Deterministic finite actual-filled-mass cut scout, not an exact certificate."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import json,sys,pathlib,time
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import differential_evolution
BASE=json.load(open(pathlib.Path(__file__).with_name('farthest_merged_G10000.json')))
P=np.array(BASE['points'],float)/BASE['grid']
T=np.array(BASE['T'])
E=np.array(sorted({tuple(sorted((int(t[i]),int(t[(i+1)%3])))) for t in T for i in range(3)}))

def cut(P,E,n,h):
 d=P@n-h
 keep=P[d<=0]
 a,b=E.T; ix=(d[a]*d[b]<0)
 x,y=a[ix],b[ix]
 if len(x):keep=np.concatenate([keep,P[x]+(P[y]-P[x])*(d[x]/(d[x]-d[y]))[:,None]])
 return keep

def geom(P):
 hull=ConvexHull(P)
 inds=hull.vertices; X=P[inds]
 t=hull.simplices.copy(); A,B,C=np.moveaxis(P[t],1,0)
 flip=np.sum(np.cross(B-A,C-A)*hull.equations[:,:3],axis=1)<0
 t[flip,1:]=t[flip,1:][:,::-1]
 A,B,C=np.moveaxis(P[t],1,0)
 D=np.einsum('ij,ij->i',A,np.cross(B,C))
 vol=D.sum()/6
 c=(D[:,None]*(A+B+C)).sum(0)/(4*D.sum())
 _,u=np.unique(np.round(hull.equations,9),axis=0,return_index=True)
 N=hull.equations[u,:3]; h=-hull.equations[u,3]
 Q=N/(h-N@c)[:,None]
 X=X-c
 def escapes(X):
  delta=X[None,:,:]-X[:,None,:]
  lens=np.linalg.norm(delta,axis=2); r=np.linalg.norm(X,axis=1)
  W=np.einsum('ik,ijk->ij',X,delta)/np.maximum(r[:,None]*lens,1e-300)
  np.fill_diagonal(W,-np.inf)
  return np.max(W,axis=1),W
 a,wa=escapes(X);b,wb=escapes(Q)
 U=np.flatnonzero(a<-1e-9);S=np.flatnonzero(b<-1e-9)
 def bottleneck(W,root):
  best=np.full(len(W),-np.inf);best[root]=np.inf;done=np.zeros(len(W),bool)
  for _ in range(len(W)):
   j=np.argmax(np.where(done,-np.inf,best));done[j]=True
   best=np.maximum(best,np.minimum(W[:,j],best[j]))
  return np.min(best),best
 # All-pair path scores used only to order numerical controls, never a true-edge claim.
 bu,_=bottleneck(wa,np.argmax(np.sum(X*X,1)))
 bs,_=bottleneck(wb,np.argmax(np.sum(Q*Q,1)))
 return dict(V=len(X),F=len(Q),S=len(S),U=len(U),vol=float(vol),c=c.tolist(),u=inds[U].tolist(),s=u[S].tolist(),bu=float(bu),bs=float(bs)),hull

def param(z):
 n=np.array([np.cos(z[0])*np.sqrt(max(0,1-z[1]**2)),np.sin(z[0])*np.sqrt(max(0,1-z[1]**2)),z[1]])
 pr=P@n; h=pr.min()+z[2]*(pr.max()-pr.min())
 return n,h

def merit(g):return g['S']+g['U']-2 + min(0.49,max(0,-g['bu'])/4+max(0,-g['bs'])/4)

def main():
 mode=sys.argv[1] if len(sys.argv)>1 else 'scan'
 rng=np.random.default_rng(260919)
 baseline,_=geom(P);print('BASELINE',baseline,flush=True)
 best={};records=[];N=6000
 if mode=='scan':
  for k in range(N):
   z=[rng.uniform(-np.pi,np.pi),rng.uniform(-1,1),rng.uniform(.15,.9999)]
   n,h=param(z)
   try:g,_=geom(cut(P,E,n,h))
   except Exception:continue
   key=f"{g['S']}_{g['U']}"
   entry=dict(k=k,z=z,n=n.tolist(),h=float(h),g=g)
   records.append(entry)
   if key not in best or merit(g)<merit(best[key]['g']):
    best[key]=entry
    if g['S']+g['U']<=3:print('IMPROVED',key,entry,flush=True)
   if g['S']==g['U']==1:break
  pathlib.Path('cut_scan.json').write_text(json.dumps(dict(seed=260919,N=N,attempted=k+1,best=best,records=records),separators=(',',':')))
  print('CUT_SCAN_DONE',k+1,{k:(v['g']['bu'],v['g']['bs']) for k,v in best.items()},flush=True)
 elif mode=='de':
  saved=json.load(open('cut_scan.json'))
  low=sorted(saved['records'],key=lambda q:merit(q['g']))[:40]
  pop=np.array([q['z'] for q in low])
  def f(z):
   n,h=param(z)
   try:g,_=geom(cut(P,E,n,h));return merit(g)
   except Exception:return 100.
  res=differential_evolution(f,[(-np.pi,np.pi),(-1,1),(.05,.999999)],init=pop,maxiter=100,popsize=13,seed=1919,polish=False,tol=1e-12,atol=1e-12)
  n,h=param(res.x);g,_=geom(cut(P,E,n,h))
  out=dict(z=res.x.tolist(),n=n.tolist(),h=float(h),g=g,fun=float(res.fun),nfev=int(res.nfev),nit=int(res.nit))
  pathlib.Path('cut_de.json').write_text(json.dumps(out,separators=(',',':')));print(out,flush=True)
if __name__=='__main__':main()
```

## hinge_search.py
```python
"""Finite whole-region piecewise-affine hull deformation with actual filled mass.
Scouting only: all-pair root scores are not true-edge certificates. Qhull incidence
and floating classification are never exact acceptance. Deterministic commands.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import sys,json,pathlib
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import differential_evolution, minimize
from cut_search import P,E

def shape(z,with_interface=True):
 a,b,t,*v=z
 n=np.array([np.cos(a)*np.sqrt(max(0,1-b*b)),np.sin(a)*np.sqrt(max(0,1-b*b)),b])
 pr=P@n; h=pr.min()+t*np.ptp(pr)
 X=P
 if with_interface:
  d=pr-h; a,b=E.T;mask=d[a]*d[b]<0; a=a[mask];b=b[mask]
  C=P[a]+(P[b]-P[a])*(d[a]/(d[a]-d[b]))[:,None]
  X=np.concatenate([P,C])
 return X+np.maximum(0,X@n-h)[:,None]*np.array(v)[None,:]

def geom_fast(X,details=False):
 hull=ConvexHull(X);t=hull.simplices.copy();A,B,C=np.moveaxis(X[t],1,0)
 flip=np.sum(np.cross(B-A,C-A)*hull.equations[:,:3],axis=1)<0
 t[flip,1:]=t[flip,1:][:,::-1]
 A,B,C=np.moveaxis(X[t],1,0);D=np.einsum('ij,ij->i',A,np.cross(B,C));vol=D.sum()/6
 c=(D[:,None]*(A+B+C)).sum(0)/(4*D.sum())
 _,unique=np.unique(np.round(hull.equations,9),axis=0,return_index=True)
 eq=hull.equations[unique];Q=eq[:,:3]/(-eq[:,3]-eq[:,:3]@c)[:,None];Y=X[hull.vertices]-c
 def scores(Y):
  delta=Y[None,:,:]-Y[:,None,:];lens=np.linalg.norm(delta,axis=2)
  W=np.einsum('ik,ijk->ij',Y,delta)/np.maximum(np.linalg.norm(Y,axis=1)[:,None]*lens,1e-300)
  np.fill_diagonal(W,-np.inf)
  e=W.max(1);r=int(np.argmax((Y*Y).sum(1)));sinks=np.flatnonzero(e < -1e-9)
  # Squared escape deficit includes every nonroot; smooth between witness changes.
  deficit=np.maximum(0,1e-5-np.delete(e,r))
  return len(sinks),float((deficit*deficit).sum()),float(deficit.max(initial=0)),sinks,e,W,r,lens
 U,du,mu,ui,eu,wu,ru,lu=scores(Y);S,ds,ms,si,es,ws,rs,ls=scores(Q)
 # Stable uniqueness is preserved lexicographically in mode s1, relaxed in joint mode.
 g=dict(V=len(Y),F=len(Q),S=S,U=U,du=du,ds=ds,mu=mu,ms=ms,vol=float(vol),c=c.tolist(),u=hull.vertices[ui].tolist(),s=unique[si].tolist())
 if details:g.update(points=X.tolist(),triangles=t.tolist())
 return g

def merit(g,mode='joint'):
 if mode=='s1': return max(g['S']-1,0)*10+g['du']+g['ds']
 if mode=='u1': return max(g['U']-1,0)*10+g['du']+g['ds']
 # Continuous escape scores allow finite transitions; number only a smaller tie term.
 return g['du']+g['ds']+0.001*(g['S']+g['U']-2)

def main():
 mode=sys.argv[1] if len(sys.argv)>1 else 'scan'; rng=np.random.default_rng(731919)
 best={};records=[]
 if mode=='scan':
  for k in range(6000):
   # Half generic orientations, half targeted at the positive-z unwanted region.
   if k%2:n=np.array([rng.normal(0,.55),rng.normal(0,.55),1.]);n/=np.linalg.norm(n);a=np.arctan2(n[1],n[0]);b=n[2]
   else:a=rng.uniform(-np.pi,np.pi);b=rng.uniform(-1,1)
   z=[a,b,rng.uniform(.15,.85),*rng.normal(0,.8,3)]
   try:g=geom_fast(shape(z))
   except Exception:continue
   entry=dict(k=k,z=[float(x) for x in z],g=g);records.append(entry);key=f"{g['S']}_{g['U']}"
   if key not in best or merit(g)<merit(best[key]['g']):
    best[key]=entry
    if g['S']+g['U']<=3:print('LOW',entry,flush=True)
   if g['S']==g['U']==1:print('FLOAT_S1U1',entry,flush=True);break
  out=dict(seed=731919,attempted=k+1,best=best,records=records)
  pathlib.Path('hinge_scan.json').write_text(json.dumps(out,separators=(',',':')))
  print('HINGE_SCAN_DONE',k+1, min(r['g']['U'] for r in records),min(r['g']['S'] for r in records),len(best),flush=True)
 else:
  saved=json.load(open('hinge_scan.json'));criterion=mode
  pop=np.array([r['z'] for r in sorted(saved['records'],key=lambda r:merit(r['g'],criterion))[:48]])
  nfev=0;low=1e10;best=None
  def f(z):
   nonlocal nfev,low,best
   nfev+=1
   try:g=geom_fast(shape(z));val=merit(g,criterion)
   except Exception:return 1e6
   if val<low:
    low=val;best=dict(z=z.tolist(),g=g,fun=val,nfev=nfev)
    if nfev%10==0 or g['S']+g['U']<=3:print('OPT',best,flush=True)
   return val
  res=differential_evolution(f,[(-np.pi,np.pi),(-1,1),(.05,.95),(-3,3),(-3,3),(-3,3)],init=pop,seed=940919,maxiter=150,polish=False,tol=1e-12,atol=1e-12)
  print('DE_DONE',best,flush=True)
  z=res.x
  rr=minimize(f,z,method='Nelder-Mead',options={'maxiter':2000,'xatol':1e-11,'fatol':1e-12})
  best['details']=geom_fast(shape(best['z']),True)
  pathlib.Path('hinge_'+criterion+'.json').write_text(json.dumps(best,separators=(',',':')))
  print('HINGE_OPT_DONE',best['g'],best['z'],flush=True)
if __name__=='__main__':main()
```
