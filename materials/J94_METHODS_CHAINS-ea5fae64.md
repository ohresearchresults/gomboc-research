# material-ea5fae645e76

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# J94 finite chain, dome and protected-support methods

Complete runnable unencoded source units. Dependencies are J94_METHODS_CONTINUATION [internal-source-reference] plus the five complete J90/J91 bundles [internal-source-reference], [internal-source-reference], [internal-source-reference], [internal-source-reference], [internal-source-reference]. Extract every file block including final newline into the same directory as those sources and the reconstructed J90_DETACHED_C390_G8_AUDIT.json. Environment: Python3.13.5, NumPy2.3.5, SciPy1.17.0, PyTorch2.10.0+cpu, OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1. Exact body J94_CHAIN_C444_G8 is separately reconstructible from [internal-source-reference] plus the full J90 core; no numerical optimizer portability is required for that body.

## Executed scope and evidence limits

`python chains94.py` was interrupted after45 seconds, not a completed Cartesian grid. The source fully specifies six scales, n2/3/4, two largest-guard old endpoints and four separated old-Q directions. Full retraction can erase the proposed chain by moving it back inside the hull. This is why the fixed-chain method below changes the mass-repair variables.

`python fixedmass94.py 0`, `python fixedmass94.py 2`, and `python fixedmass94.py 4` each completed four least-added-volume eligible trials. Which0=scale1.002: all four close mass and retain numerical U1 with extra S. The fourth produces the exact J94_CHAIN_C444_G8 own312/weak000/primitivezero000 after G8 freeze, with the literal selected state preserved in J94_METHODS_CONTINUATION. Its first new point has no strict chord to any original vertex but escapes through the second new point to old23, proved exactly in J94_EXACT_RECOVERY. Which2=scale1.03: four trials close mass but have U2 and S7/10/8/8, V121–124,E224–232. Which4=scale1.1 tests amplitude beyond the fixed-centre necessary root-support rise of about9.3%; the four smallest initial added volumes are .02293359431948705 to old28 in4links, .023573987612656166 to old33 in3links, .023740504154928788 to old33 in4links, .024731578488658812 to old38 in4links. All four close the numerical mass equation but have U2, not U1. Final V/E/F and S are110/210/102 S5;109/207/100 S5;110/210/102 S5;109/211/104 S9. Their complete positive numerical Q lists are respectively [.12926851202234013,.10513915669959217,.019654351556994798,.00033675852680736806], [.1271423928432539,.10405675189178565,.02190546922998149,.00033675852680736806], [.12687253063486248,.10345444876076548,.022592515076005237,.00033675852680781215], [.12963401569529276,.08947848421965021,.03264790636675896,.0006187679974853921,.00043525259008003747,.0003367585268075901,.0002402288344690584,.00009414777193750279]. The script writes full P/Q, own moments, actual input apexes and trial metadata to each output, not only these Q excerpts. Which1,3,5 were NOT executed. The reported min_all_guard=0 includes each point's diagonal self-vote and indicates a failed strict escape, not a positive certificate. No which4 exact class or weak census is claimed.

`python dome94.py` completed240 cases: counts1,2,3,4,6,8,12,18,25,37; six slacks; four blends. It selects directions from the C434 dying polar component, but the NOMINATED hull is conv(original130 C390 points, proposed dome), omitting the five C434 apexes. Therefore its `added_volume` against C434 is only a numerical difference, not necessarily added material, and it cannot automatically use a C434-subset obstruction. This explicit code scope is authoritative over a broad verbal description. No S1 was found; the discrete37 directions are not a certified continuous angular covering.

`python clip94.py old 75 .001 J94_CLIP` completed75 additions, preserving the original elder support in reference geometry. The final loop's step74 report is the hull BEFORE its75th point is added:132/317/187, reference S42/U1 with largest Q~.06375, own S25/U26. The saved final apex state includes the75th addition, so do not identify it with that preceding report. Best within-budget checkpoint remained the starting C434. No other clip parameter run is claimed.

`python ball94.py` completed440 eligible cases,332 with actual E<=249, no S1. Its full finite sphere/basin sampling and parameters are literal below. It retains the original C434 apexes, unlike dome94.py. Every accepted proposal is strictly below the protected elder support and inside an old-point witness ball before integrating own mass; this is reference U1 only. All negative observations are bounded numerical searches, NOT shape-family exclusions. Selected new exact nonwinners and the tiny-bar control are recorded separately in J94_EXACT_RECOVERY.

## chains94.py
2971 bytes; SHA256 8e67643760f15bd245494474473fbd17de1f2b556d5805385c8cf4c69edef87a.
```python
"""Finite multi-link physical witness chains, with full nonlinear mass repair.
A spherical chain of n equal angles delta and geometric radii ratio t has
p_k.(p_{k+1}-p_k)=|p_k|^2*(t*cos(delta)-1).  Positive chords are sufficient
for non-instability, even if an intermediate point is not an extreme vertex.
Only numerical nominations; exact VF audit remains the acceptance boundary.
"""
import json,sys
from pathlib import Path
import numpy as np
from surgery94 import initial,save
from outerflow91 import retract
from envelope91 import hullpoly
from dome94 import component
from j90 import report
ROOT=Path(__file__).resolve().parent

def link(a,z,n):
 r=np.linalg.norm(a);s=np.linalg.norm(z);u=a/r;v=z/s;phi=np.arccos(np.clip(u@v,-1,1))
 margin=(s/r)**(1/n)*np.cos(phi/n)-1
 if margin<=1e-7:return None,margin
 if phi<1e-8: dirs=np.array([(1-k/n)*u+k/n*v for k in range(n)])
 else: dirs=np.array([(np.sin((1-k/n)*phi)*u+np.sin(k/n*phi)*v)/np.sin(phi) for k in range(n)])
 return dirs*(r*(s/r)**(np.arange(n)/n))[:,None],margin

def run():
 old,W,g=initial();z=hullpoly(np.vstack([old,W]));r=report(z);bar=r['Q'][0];fis=component(z,bar);q=z['y'];root=bar['root'];ids=[root]
 # Four separated directions in the current whole dying component.
 N=q/np.linalg.norm(q,axis=1)[:,None]
 while len(ids)<4:
  j=max((i for i in fis if i not in ids),key=lambda i:min(1-N[i]@N[j] for j in ids));ids.append(j)
 table=[];best=None;besttwo=None
 for fi in ids:
  n=N[fi];h=1/np.linalg.norm(q[fi]);
  for scale in [1.002,1.01,1.03,1.06,1.1,1.2]:
   a=h*scale*n
   for count in [2,3,4]:
    choices=[]
    for vi,v in enumerate(old):
     pts,guard=link(a,v,count)
     if pts is not None:choices.append((guard,vi,pts))
    choices.sort(key=lambda x:-x[0])
    for guard,vi,pts in choices[:2]:
     try:
      w,zz,closed=retract(old,np.vstack([W,pts]),tol=3e-14,maxit=10);rr=report(zz)
     except Exception as e:
      table.append(dict(fi=fi,scale=scale,count=count,vi=vi,error=str(e)));continue
     pp=np.vstack([old,w]);guards=np.einsum('ik,ijk->ij',w,pp[None]-w[:,None]).max(1)
     oo=np.einsum('ik,ijk->ij',w,old[None]-w[:,None]).max(1)
     rec=dict(face=fi,scale=scale,links=count,endpoint=vi,initial_chain_guard=float(guard),closed=bool(closed),min_all_guard=float(min(guards)),min_old_guard=float(min(oo)),report=rr)
     table.append(rec)
     if not closed or min(guards)<=1e-10 or rr['E']>249 or len(rr['U'])!=1 or rr['P']:continue
     key=(len(rr['S']),sum(b['depth'] for b in rr['Q']),rr['E'])
     if best is None or key<best:
      best=key;save('J94_CHAINS_BEST',old,w,g,dict(info=rec));print('BEST',len(table),key,fi,scale,count,vi,'old_guard',min(oo),flush=True)
     if len(rr['S'])==2 and (besttwo is None or key<besttwo):
      besttwo=key;save('J94_CHAINS_TWO',old,w,g,dict(info=rec))
 (ROOT/'J94_CHAINS_TABLE.json').write_text(json.dumps(table,indent=2)+'\n')
 print('J94_FINITE_MULTILINK_SCOUT_DONE',len(table),best,flush=True)
if __name__=='__main__':run()
```

## fixedmass94.py
2694 bytes; SHA256 d2974aa339d1a2a7e0e180fff46cca97fa1d7c561270da95caa180da07fba6c6.
```python
"""Keep an outer escape chain fixed while repairing mass with existing five apexes.
Chain candidates are ranked by actual added hull volume, not largest chord
margin (which can select a costly nonlocal endpoint). Numerical only.
"""
import json,sys
from pathlib import Path
import numpy as np,torch
from chains94 import link
from surgery94 import initial,save
from envelope91 import hullpoly
from outerflow91 import chart
from j90 import report
ROOT=Path(__file__).resolve().parent

def repair(old,W,fixed,tol=2e-14,maxit=20):
 w=W.copy();n=len(w)
 for it in range(maxit):
  z,f=chart(old,np.vstack([w,fixed]));a=torch.tensor(np.vstack([w,fixed]));M=f(a)[1].numpy()
  if max(abs(M))<tol:return w,z,True
  J=torch.func.jacrev(lambda x:f(x)[1])(a).numpy()[:,:n,:].reshape(3,-1)
  if np.linalg.matrix_rank(J,tol=1e-12)<3:return w,z,False
  d=np.linalg.lstsq(J,-M,rcond=None)[0].reshape(w.shape);good=False
  for bt in range(16):
   trial=w+d*2**-bt
   try:zt,ft=chart(old,np.vstack([trial,fixed]));Mt=ft(torch.tensor(np.vstack([trial,fixed])))[1].numpy()
   except Exception:continue
   if np.linalg.norm(Mt)<np.linalg.norm(M):w=trial;good=True;break
  if not good:return w,z,False
 z,_=chart(old,np.vstack([w,fixed]));return w,z,max(abs(z['g']))<tol

def run(which):
 old,W,g=initial();z=hullpoly(np.vstack([old,W]));r=report(z);fi=r['Q'][0]['root'];n=z['y'][fi]/np.linalg.norm(z['y'][fi]);h=1/np.linalg.norm(z['y'][fi]);scales=[1.002,1.01,1.03,1.06,1.1,1.2];scale=scales[which];a=scale*h*n
 opts=[]
 for cnt in [2,3,4]:
  for vi,v in enumerate(old):
   p,guard=link(a,v,cnt)
   if p is None:continue
   q=hullpoly(np.vstack([old,W,p]));rr=report(q)
   if rr['E']<=249:opts.append((rr['volume'],vi,cnt,p,guard,rr))
 opts.sort(key=lambda t:t[0]);print('MIN_VOLUME_CHAIN',which,[(t[0]-r['volume'],t[1],t[2]) for t in opts[:4]],flush=True)
 table=[]
 for ordinal,t in enumerate(opts[:4]):
  volume,vi,cnt,p,guard,rr=t
  w,zz,ok=repair(old,W,p);r2=report(zz);ww=np.vstack([w,p]);pool=np.vstack([old,ww]);votes=np.einsum('ik,ijk->ij',ww,pool[None]-ww[:,None]);us=votes.max(1)
  rec=dict(scale=scale,endpoint=vi,links=cnt,guard=float(guard),initial=rr,closed=bool(ok),own=r2,min_all_guard=float(min(us)),fixed_primary=p[0].tolist(),history_scope='four least-added-volume chains among n=2,3,4 and all130 old endpoints')
  table.append(rec);save(f'J94_FIXEDCHAIN_{which}_{ordinal}',old,ww,g,dict(info=rec));print('FIXED_REPAIR',which,ordinal,ok,'VEF',r2['V'],r2['E'],r2['F'],'SU',len(r2['S']),len(r2['U']),'Q',[b['depth'] for b in r2['Q']],'Uguard',min(us),flush=True)
 (ROOT/f'J94_FIXEDCHAIN_{which}_TABLE.json').write_text(json.dumps(table,indent=2)+'\n')
if __name__=='__main__':run(int(sys.argv[1]))
```

## dome94.py
2655 bytes; SHA256 f49acf92edc6ff93d7181b83d886ed40a3d80af1020f1106e4f4b8487bd8cd09.
```python
"""Simultaneous outward dome over the complete current polar dying component.
All proposed points lie strictly inside old-point diameter balls. True finite
hulls and actual homogeneous centroids are recomputed. Reference U1 is not own U1.
"""
import sys,json
from pathlib import Path
import numpy as np
from surgery94 import initial,save
from envelope91 import hullpoly,ref,support_ball
from j90 import report
ROOT=Path(__file__).resolve().parent

def component(z,bar):
 q=z['q'];es=z['dual_edges'];a=q[es[:,0]];d=q[es[:,1]]-a
 t=np.clip(-np.sum(a*d,1)/np.sum(d*d,1),0,1);lev=np.sum((a+t[:,None]*d)**2,1)
 nb={i:[] for i in range(len(q))}
 for (i,j),l in zip(es,lev):
  if l>bar['death']+1e-10:nb[i].append(j);nb[j].append(i)
 seen={bar['root']};todo=list(seen)
 while todo:
  for j in nb[todo.pop()]:
   if j not in seen:seen.add(int(j));todo.append(int(j))
 return sorted(seen)

def run():
 old,W,g=initial();z=hullpoly(np.vstack([old,W]));r=report(z);ids=component(z,r['Q'][0]);normals=z['q'][ids];normals/=np.linalg.norm(normals,axis=1)[:,None]
 # Greedy spherical farthest-point order covers the WHOLE component, seeded at root.
 order=[ids.index(r['Q'][0]['root'])]
 while len(order)<len(ids):
  dist=np.min(1-normals@normals[order].T,axis=1);dist[order]=-1
  order.append(int(np.argmax(dist)))
 table=[];best=None;num=0
 for count in [1,2,3,4,6,8,12,18,25,37]:
  for slack in [.5,.2,.1,.03,.01,.001]:
   pts=np.array([support_ball(old,normals[i],slack)[0] for i in order[:count]])
   for blend in [.25,.5,.75,1.]:
    # Blending each proposal with its old witnessing vertex stays in that ball.
    wi=[support_ball(old,normals[i],slack)[1] for i in order[:count]]
    wp=blend*pts+(1-blend)*old[wi]
    try:zz=hullpoly(np.vstack([old,wp]));rr=report(zz);rf=ref(zz)
    except Exception as e:continue
    rec=dict(count=count,slack=slack,blend=blend,selected_faces=[ids[i] for i in order[:count]],witnesses=wi,reference=rf,own=rr,added_volume=zz['vol']-z['vol'])
    table.append(rec);num+=1
    # Reference all positive Q depths, budget first. No actual-mass win inferred.
    kk=(rr['E']>249,len(rf['U'])!=1,sum(b['depth'] for b in rf['Q']))
    if best is None or kk<best[0]:
     best=(kk,wp,rec);save('J94_DOME_BEST',old,wp,g,dict(info=rec))
     print('DOME_BEST',num,kk, 'count',count,'slack',slack,'blend',blend,'VEF',rr['V'],rr['E'],rr['F'],'refSU',len(rf['S']),len(rf['U']),'ownSU',len(rr['S']),len(rr['U']),'g',rr['centroid'],flush=True)
 (ROOT/'J94_DOME_TABLE.json').write_text(json.dumps(dict(component=ids,order=order,results=table),indent=2)+'\n')
 print('J94_DOME_NUMERICAL_ONLY',len(table),flush=True)
if __name__=='__main__':run()
```

## clip94.py
2749 bytes; SHA256 d9b2d546013f719e6a6842d706cd37ed8532953d049434c2821af05e3d3bc488.
```python
"""U-safe support envelopes clipped below a retained stable supporting plane.
Finite recursive/old-witness hull growth, with full own/reference census.
All calculations here are numerical; source exact host comes from surgery94.
"""
import json,sys
from pathlib import Path
import numpy as np
from surgery94 import initial,save
from envelope91 import hullpoly,ref
from j90 import report
ROOT=Path(__file__).resolve().parent

def clipped_ball(pool,n,ns,hs,slack=.001):
 n=n/np.linalg.norm(n);C=pool/2;rad=(1-slack)*np.linalg.norm(pool,axis=1)/2
 W=C+rad[:,None]*n
 t=hs-C@ns;proj=n-(n@ns)*ns;pn=np.linalg.norm(proj)
 ok=t>=-rad
 active=(W@ns>hs)&ok
 if pn<1e-13:
  # A deterministic perpendicular for the degenerate parallel objective.
  e=np.eye(3)[np.argmin(abs(ns))];proj=e-(e@ns)*ns;pn=np.linalg.norm(proj)
 rr=np.sqrt(np.maximum(0,rad**2-t**2))
 W[active]=C[active]+t[active,None]*ns+rr[active,None]*proj/pn
 vals=W@n;vals[~ok]=-np.inf
 i=int(np.argmax(vals));return W[i],i,float(W[i]@(pool[i]-W[i]))

def run(mode='old',steps=70,slack=.001,tag='J94_CLIP',source=None):
 old,W,g=initial()
 if source:W=np.array(json.loads(Path(source).read_text())['apexes'])
 points=np.vstack([old,W]);z=hullpoly(points);rr=ref(z)
 elder=int(np.argmax(np.sum(z['y']**2,1)));ns=z['y'][elder]/np.linalg.norm(z['y'][elder]);hs=1/np.linalg.norm(z['y'][elder]);plane=hs-1e-7
 hist=[];best=(999,999)
 for k in range(steps):
  z=hullpoly(points);rr=ref(z);own=report(z)
  rec=dict(step=k,reference=rr,own=own)
  print(tag,k,'VEF',rr['V'],rr['E'],rr['F'],'refSU',len(rr['S']),len(rr['U']),'Q', [round(b['depth'],8) for b in rr['Q']],'ownSU',len(own['S']),len(own['U']),flush=True)
  kk=(len(rr['S']),sum(b['depth'] for b in rr['Q']))
  if rr['E']<=249 and kk<best:
   best=kk;save(tag+'_BEST',old,points[len(old):],g,dict(info=rec,mode=mode,slack=slack,elder_normal=ns.tolist(),elder_height=hs))
  if len(rr['S'])==1:
   rec['outcome']='reference110, not an own-mass claim';hist.append(rec);break
  peak=rr['Q'][0]['root'];n=z['y'][peak]
  pool=old if mode=='old' else points
  w,vi,guard=clipped_ball(pool,n,ns,plane,slack)
  if np.max(z['y']@w)<1+1e-8:
   rec['outcome']='no strict clipped outward support at current root';hist.append(rec);break
  points=np.vstack([points,w]);rec.update(point=w.tolist(),witness=vi,guard=guard);hist.append(rec)
 save(tag,old,points[len(old):],g,dict(history=hist,mode=mode,slack=slack,elder_normal=ns.tolist(),elder_height=hs))
 print('CLIPPED_ENVELOPE_NUMERICAL_ONLY',flush=True)
if __name__=='__main__':run(sys.argv[1] if len(sys.argv)>1 else 'old',int(sys.argv[2]) if len(sys.argv)>2 else 70,float(sys.argv[3]) if len(sys.argv)>3 else .001,sys.argv[4] if len(sys.argv)>4 else 'J94_CLIP',sys.argv[5] if len(sys.argv)>5 else None)
```

## ball94.py
2884 bytes; SHA256 cb47e013aeadb87ded415864f0e782c13343626e1c008fd07d5b56713285f636.
```python
"""Finite outer spherical-cap candidates with a protected elder support plane.
Numerical exploration, not a proof or an exact own-centred construction.
Every added point has a strict witness in the unchanged C390 host. Therefore
reference U1 is retained; the own mass and both landscapes are still recomputed.
"""
import json,sys
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from surgery94 import initial,save
from envelope91 import hullpoly
from dome94 import component
from j90 import report
ROOT=Path(__file__).resolve().parent

def run():
 old,W,g=initial();z=hullpoly(np.vstack([old,W]));r=report(z);q=z['y'];elder=int(np.argmax((q*q).sum(1)))
 ns=q[elder]/np.linalg.norm(q[elder]);hs=1/np.linalg.norm(q[elder]);b=r['Q'][0];rlevel=1/np.sqrt(b['death'])
 fis=component(z,b);N=q[fis]/np.linalg.norm(q[fis],axis=1)[:,None]
 t1=np.cross(ns,np.eye(3)[np.argmin(abs(ns))]);t1/=np.linalg.norm(t1);t2=np.cross(ns,t1)
 print('DOME',len(N),hs,rlevel,'angle_cos',min(N@ns),max(N@ns),flush=True)
 idx=np.arange(48); zz=1-2*(idx+.5)/len(idx);aa=idx*np.pi*(3-np.sqrt(5));ss=np.sqrt(1-zz*zz);dirs=np.c_[ss*np.cos(aa),ss*np.sin(aa),zz]
 table=[];best=None
 for margin in [0,.02,.05,.1,.2]:
  fit=minimize(lambda c:(.5*c@c,c),-.25*ns,jac=True,constraints=[{'type':'ineq','fun':lambda c:(N-ns)@c-(rlevel+margin-hs),'jac':lambda c:N-ns}],method='SLSQP',options={'ftol':1e-13,'maxiter':100})
  cbase=fit.x;print('BALL_FIT',margin,fit.success,cbase,'R',hs-ns@cbase,'res',min((N-ns)@cbase-(rlevel+margin-hs)),flush=True)
  for f in [.5,.75,1,1.25,1.5,2]:
   for a in [-.2,0,.2]:
    for bb in [-.2,0,.2]:
     c=f*cbase+a*t1+bb*t2;R=hs-ns@c-1e-7
     if R<=0:continue
     for mode,d in [('basin',N),('sphere',dirs)]:
      pp=c+R*d;votes=np.einsum('ik,ijk->ij',pp,old[None]-pp[:,None]);safe=votes.max(1)>1e-8
      pp=pp[safe]
      if not len(pp):continue
      # New points are all strictly below the protected support and strictly
      # in some old-vertex witness ball, before the true own mass is integrated.
      w=np.vstack([W,pp]);zt=hullpoly(np.vstack([old,w]));own=report(zt)
      ref=zt.copy();ref.update(p=zt['x'],q=zt['y'],g=np.zeros(3));rr=report(ref)
      rec=dict(margin=margin,f=f,a=a,b=bb,mode=mode,center=c.tolist(),radius=float(R),safe_points=int(safe.sum()),own=own,ref=rr)
      table.append(rec)
      key=(own['E']>249,len(rr['S']),sum(p['depth'] for p in rr['Q']),len(own['S'])+len(own['U']))
      if best is None or key<best:
       best=key;save('J94_BALL_BEST',old,w,g,dict(info=rec));print('BEST',len(table),key,'VEF',own['V'],own['E'],own['F'],'ownSU',len(own['S']),len(own['U']),'refSU',len(rr['S']),len(rr['U']), 'Q', [x['depth'] for x in rr['Q']],flush=True)
 (ROOT/'J94_BALL_TABLE.json').write_text(json.dumps(table,indent=2)+'\n')
 print('J94_FINITE_BALL_SCOUT_DONE',len(table),best,flush=True)
if __name__=='__main__':run()
```
