# material-b3894c166c5e

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# J112 — complete numerical producers preceding and accompanying J111

All five units below were EXECUTED. These are finite nominations and numerical negative trials, NOT exact equilibrium certificates or global exclusions. The exact new result is separately preserved in [internal-source-reference] (J111), not established by these optimizers or sampled integrals.

## Complete dependencies and reconstruction
Create sibling directories j109 and j111. From [internal-source-reference] extract its complete R82.txt FILE block into j109. From [internal-source-reference] extract its complete geometry109.py FILE block into j109. Extract these five FILE blocks into j111. These three complete materials are the entire dependency set; no originating sandbox, worker workspace or encoded source archive is needed. The explicit sibling layout is used only for the local import, not as evidence of an existing file.

Run each of `root_keep111.py`, `depth_capacity111.py`, `tree_mass111.py`, `bridge111.py`, `entry_bridge111.py` with `OPENBLAS_NUM_THREADS=1 python j111/FILENAME`. Executed versions: CPython3.13.5, NumPy2.3.5, SciPy1.17.0. There are no seeds, hidden checkpoints or omitted non-default parameters. The programs write five JSON outputs with all nominated new planes, applicable solver statuses, actual filled-hull mass and nominal own/reference P/Q landscapes. Numerical census thresholds in geometry109.py remain explicit; tiny or weak equilibria are NOT certified absent. Any `lattice_failure` record with empty nominal root lists is an ERROR boundary, never S0/U0. During tree optimization, mass is computed without requiring a triangulation-based edge census, avoiding an intermediate near-degenerate numerical lattice error.

## What was actually learned
1. A new polar root can receive both old roots and preserve old U: the linear constraints q7.r>=|q7|^2, q18.r>=|q18|^2, u.r<=1 are numerically feasible. The minimum-norm boundary solution has |r| about11.5252910842. With root margin.01 and old-U slack.01 the root-only cut has V116/E174/F60, reference S1/U2 but actual S14/U11. Retaining a particular old unstable vertex does not retain the full equilibrium class or fix mass. Sixteen root/vertex-margin choices are retained by the producer.
2. The compulsory-depth quadrature can give positive relaxed moment capacity: at the old minimum-norm root times3 the numerical positive slab moment is .00153342284213, exceeding the depth2 negative core by about .0005083. At scale1.0001 the depth3 relaxed difference is already about .0006448. These are NOT feasible convex mass corrections. J111 proves the contrary for depths<=3 in the stated cube using convexity. Its explicit nonconvex balanced sandwich explains why the moment relaxation can be positive without contradiction.
3. Seventy-two finite great-circle spoke-tree models were actually optimized with simultaneous filled-body mass residuals. Two root policies, depths2/3/4, root scales1/2/4/8 and3/4/5 equally spaced azimuthal routes were tested. Each route has an independently optimized strength in[.001,1], all radial guards positive. No own-centred S1 solution was reached. The smallest absolute centre norm .008439651924 occurs after shrinking the body by the root scale; the best scale-invariant |r|*|g| is about .787316183082, not near0. For example the depth4 three-route retained-U-root model has13 active facets and numerical actual S13/U4; global scaling only shrinks its centre displacement. This is a failed finite spoke parameterization, not an exclusion of depth4, asymmetric trees or moving old supports.
4. A direct old-q7 to old-q18 geodesic bridge has numerical angle145.7391179835 degrees and norm ratio1.3483546961573. The first strict equal-step length is11 links, i.e.10 new planes, just beyond the older nine-cut OLD-root gate. The resulting body retires only4 old facets: V172/E258/F88,C516, reference S1/U4 but actual S39/U37, centre shift(.134382418555,.047068794516,-.070575120509), volume1.396290902211. More links leave the same mass problem and exceed budget further. Entry into the old elder-reaching component at higher-radius points33 and79 instead requires numerically42 and94 links, respectively. These tests concern the current unchanged endpoints and their numerical radial graph; they do not exclude changed endpoints, changed fans, joint metric/shape motion or more general trees.

The constructive implication is not to repeat shallow same-root controls or a shrinking symmetric spoke family. A useful escape must change the witness geometry substantially (depth>=4 without the same scale-invariant mass defect), change the old interface/shape, or use a root policy outside J111. Simultaneous actual mass and complete primal/polar control remain essential.

## Observed manifests
Inputs supplied by J109 materials:
- R82.txt1888B SHA9765712b5ffaa464ed4d677974256294c6d867b77fe77b930d166853f66a92a7.
- geometry109.py4286B SHA5a61893fd75b1e7e8d261bbbe0f42ca88a2c53dadf65da8e38aa723068189479.
Source units:
- root_keep111.py1846B SHA427cf760d69640fcac1b5eee790a6e824a32a0013dfc9cd990d80739986ad408.
- depth_capacity111.py1806B SHAacac74dcc4e9a13c11514a230c0c8a1817996f3c89a405ac6f37de18662206b4.
- tree_mass111.py3161B SHAd443b151244239d5de844a363c1a1b7e1c3f203caf4d51446d7216022d8c9285.
- bridge111.py1512B SHA9d711f751a192c9e072852f78aa83e5b5f95bb63c241e68bc730499474ea1676.
- entry_bridge111.py1781B SHA24a8595522debf5447878e15e74a4aa51210ad36a66e9446ed900aa6b3323c6d.
Generated outputs:
- ROOT_KEEP111.json120262B SHAf78c06e3a221ea7874da455fee351553ea764ec782385473871681b26d4c09b4.
- DEPTH_CAPACITY111.json4741B SHA5ba43edb1859e782a403bab937434bb06bd1de3430771e1e855fa010d4221747.
- TREE_MASS111.json741496B SHAdb615e011ee6675b7c095f20a487b09bc2556db5cafcc74f8ff49765398d36fd.
- BRIDGE111.json269798B SHA2ce81626dac032f54af011ac41598fd6154d18bf7ecf5f528b1e70aa70122159.
- ENTRY_BRIDGE111.json230949B SHAcc5f1b9dd034c04c65cc17bb19c156f3be82f9db0c9ce58c8e31a7563a1a5c98.
Hashes identify observed numerical outputs, not a cross-platform bitwise guarantee. All outputs are regenerated from the complete deterministic input/parameter procedures. Elapsed time is printed but is not in TREE_MASS111.json. Expected terminal rows:16 root-cut rows,9 depth-capacity rows, `TREE_MASS111_FINISHED 72 calls 2410`,11 direct-bridge rows and9 elder-entry rows; the five JSON writes must all succeed.

### FILE root_keep111.py
```python
"""Finite direct-root nominations retaining or replacing the actual old U.
Numerical exploration only; complete input/helper dependencies are J109.
"""
import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'j109'))
from geometry109 import *
from scipy.optimize import linprog,minimize
q,g,old=load();p=old['v']-g
U=census(old)['U'];assert len(U)==1
u=p[U[0]];Q=q[[7,18]];bb=np.einsum('ij,ij->i',Q,Q)
A=np.vstack([-Q,u]);b=np.r_[-bb,1.]
lin=linprog(np.zeros(3),A_ub=A,b_ub=b,bounds=[(None,None)]*3,method='highs')
print('LP',lin.success,lin.message)
r0=Q.T@np.linalg.solve(Q@Q.T,bb)
records=[]
for root_margin in [0.,.0001,.01,.1]:
 for vertex_margin in [0.,.001,.01,.05]:
  rhs=np.r_[-bb*(1+root_margin),1.-vertex_margin]
  lp=linprog(np.zeros(3),A_ub=A,b_ub=rhs,bounds=[(None,None)]*3,method='highs')
  rec=dict(root_margin=root_margin,vertex_margin=vertex_margin,lp_success=bool(lp.success),lp_message=lp.message)
  if lp.success:
   opt=minimize(lambda x:float(x@x)/2,lp.x,jac=lambda x:x,
      constraints=[dict(type='ineq',fun=lambda x:rhs-A@x,jac=lambda x:-A)],method='SLSQP',
      options=dict(ftol=1e-12,maxiter=1000))
   r=opt.x;s=fast_h(np.vstack([q,r]));rec.update(root=r.tolist(),optimizer_success=bool(opt.success),residual=(rhs-A@r).tolist(),oldU_support=float(u@r),norm=float(np.linalg.norm(r)),own=census(s),reference=census(s,np.zeros(3)))
   print(root_margin,vertex_margin,'norm',rec['norm'],'Udot',u@r,'V',len(s['v']),'own',len(rec['own']['S']),len(rec['own']['U']),'ref',len(rec['reference']['S']),len(rec['reference']['U']),flush=True)
  records.append(rec)
Path(__file__).with_name('ROOT_KEEP111.json').write_text(json.dumps(dict(old_U=u.tolist(),old_U_index=U[0],qroots=Q.tolist(),old_centre=g.tolist(),r0=r0.tolist(),r0_oldU_dot=float(r0@u),rootcuts=records),indent=2)+'\n')
```
### FILE depth_capacity111.py
```python
"""Numerical capacity of compulsory bounded-depth polar-cut envelopes.
Uses Gauss-Legendre angular quadrature only for nomination, not exact proof.
Inputs R82 and numerical geometry helper are the exact J109 material dependencies.
"""
import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'j109'))
from geometry109 import *
from numpy.polynomial.legendre import leggauss
q,g,old=load();Q=q[[7,18]];r0=Q.T@np.linalg.solve(Q@Q.T,(Q*Q).sum(axis=1))
tt,ww=leggauss(192);tt=(tt-1)/2;ww=ww/2
phi=np.linspace(0,2*np.pi,384,endpoint=False)
rows=[]
for scale in [1.0001,1.25,1.5,2.,3.,4.,6.,8.,12.]:
 r=scale*r0;rho=np.linalg.norm(r);n=r/rho;h=1/rho
 e=np.cross(n,[0,0,1]);e/=np.linalg.norm(e);f=np.cross(n,e)
 d=(tt[:,None,None]*n+np.sqrt(1-tt*tt)[:,None,None]*(np.cos(phi)[None,:,None]*e+np.sin(phi)[None,:,None]*f)).reshape(-1,3)
 oldrad=1/np.max(d@q.T,axis=1).reshape(len(tt),len(phi))
 B=fast_h(np.vstack([q,r]));v=B['v'];z=v@n
 positive=list(v[z>=-1e-12])
 for a,b in B['edges']:
  if z[a]*z[b]<0:positive.append(v[a]+(v[b]-v[a])*(-z[a]/(z[b]-z[a])))
 vp=np.unique(np.round(np.asarray(positive),14),axis=0);Vp,cp,_=mass(vp);Jp=Vp*(cp@n)
 out=dict(scale=scale,root=r.tolist(),h=h,positive_moment=Jp,negative_envelope_moments={})
 for depth in [1,2,3,4,6,8,12]:
  env=h/np.cos(np.arccos(tt)/(depth+1))**(depth+1)
  rad=np.minimum(oldrad,env[:,None])
  Jm=np.sum(ww*(-tt)*np.mean(rad**4,axis=1))*np.pi/2
  out['negative_envelope_moments'][str(depth)]=float(Jm)
 print(scale,'h',h,'pos',Jp,'upper',[round(Jp-out['negative_envelope_moments'][str(m)],7) for m in [1,2,3,4,6,8,12]],flush=True)
 rows.append(out)
Path(__file__).with_name('DEPTH_CAPACITY111.json').write_text(json.dumps(dict(gauss_nodes=192,azimuth_nodes=384,numerical_only=True,rows=rows),indent=2)+'\n')
```
### FILE tree_mass111.py
```python
"""Finite polar route cuts with homogeneous mass solved simultaneously.
This is numerical nomination, not an exact body certificate.
Source dependencies: geometry109.py and literal R82.txt (J109 materials).
"""
from __future__ import annotations
import sys,json,math,time
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'j109'))
from geometry109 import *
from scipy.optimize import least_squares
q,g,old=load();Q=q[[7,18]];bb=(Q*Q).sum(axis=1);r0=Q.T@np.linalg.solve(Q@Q.T,bb)
output=[];count=0;t0=time.time()
for base in ('minimum_norm','retained_U'):
 if base=='minimum_norm':rbase=r0*1.01
 else:
  u=(old['v']-g)[census(old)['U'][0]]
  rbase=np.linalg.solve(np.vstack([Q,u]),np.r_[bb*1.01,.99])
 for depth in (2,3,4):
  for scale in (1.,2.,4.,8.):
   r=rbase*scale;rho=np.linalg.norm(r);n=r/rho;e=np.cross(n,[0,0,1.]);e/=np.linalg.norm(e);f=np.cross(n,e)
   for routes in (3,4,5):
    if routes*depth+1>25:continue
    # Source direction attaining the depth-envelope support opposite n.
    angle=depth*np.pi/(depth+1);step=angle/depth;eta=.02
    spec=dict(base=base,depth=depth,scale=scale,routes=routes,angle=angle,shrink=eta,root=r.tolist())
    template=[];parents=[]
    for k in range(routes):
     azimuth=2*np.pi*k/routes;d=np.cos(azimuth)*e+np.sin(azimuth)*f
     for j in range(1,depth+1):
      template.append(rho*(np.cos(step)*(1-eta))**j*(np.cos(j*step)*n+np.sin(j*step)*d))
      parents.append(82 if j==1 else 82+len(template)-1)
    template=np.array(template)
    def points(lam):return np.vstack([q,r,template*np.repeat(lam,depth)[:,None]])
    def residual(lam):
     global count
     count+=1
     aq=points(lam);dh=ConvexHull(aq)
     vv=np.linalg.solve(aq[dh.simplices],np.ones((len(dh.simplices),3,1)))[:,:,0]
     return mass(vv)[1]
    opt=least_squares(residual,np.full(routes,.6),bounds=(np.full(routes,.001),np.ones(routes)),
          ftol=2e-11,xtol=2e-11,gtol=2e-11,max_nfev=180,diff_step=1e-5)
    aq=points(opt.x);dh=ConvexHull(aq)
    vv=np.linalg.solve(aq[dh.simplices],np.ones((len(dh.simplices),3,1)))[:,:,0]
    c=mass(vv)[1]
    try:
     s=fast_h(aq);report=census(s);ref=census(s,np.zeros(3))
    except ValueError as exc:
     report=dict(S=[],U=[],V=None,E=None,F=None,lattice_failure=str(exc));ref=None
    scores=[float(aq[83+i]@(aq[j]-aq[83+i])) for i,j in enumerate(parents)]
    assert min(scores)>0
    row=dict(spec=spec,strengths=opt.x.tolist(),centroid_norm=float(np.linalg.norm(c)),nfev=int(opt.nfev),optimizer_success=bool(opt.success),message=opt.message,minimum_route_score=min(scores),own=report,reference=ref,new_planes=aq[82:].tolist(),numerical_only=True)
    output.append(row)
    if row['centroid_norm']<1e-7 or (report['V'] is not None and len(report['S'])<=2):
     print(base,depth,scale,routes,'normg',row['centroid_norm'],'ownSU',len(report['S']),len(report['U']),'VEF',report['V'],report['E'],report['F'],'lam',opt.x,flush=True)
    Path(__file__).with_name('TREE_MASS111.json').write_text(json.dumps(dict(rows=output,total_mass_calls=count),indent=2)+'\n')
print('TREE_MASS111_FINISHED',len(output),'calls',count,'seconds',time.time()-t0,flush=True)
```
### FILE bridge111.py
```python
"""Literal R82: finite shortest polar bridges to the retained old stable root.
The construction parameters and own/reference nominal full landscapes are saved.
Qhull output remains numerical; no exact endpoint classification is asserted.
"""
from __future__ import annotations
import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'j109'))
from geometry109 import *
q,g,old=load();a,b=q[[7,18]];ra,rb=np.linalg.norm(a),np.linalg.norm(b);phi=np.arccos(a@b/ra/rb)
e=a/ra;f=(b/rb-np.cos(phi)*e)/np.sin(phi)
rows=[]
for links in (11,12,13,14,16,18,20,24,32,48,64):
 t=np.arange(1,links)/links
 chain=(ra*(rb/ra)**t)[:,None]*(np.cos(phi*t)[:,None]*e+np.sin(phi*t)[:,None]*f)
 path=np.vstack([a,chain,b]);scores=np.einsum('ij,ij->i',path[:-1],np.diff(path,axis=0))
 assert np.min(scores)>0
 aq=np.vstack([q,chain]);s=fast_h(aq);own=census(s);ref=census(s,np.zeros(3))
 item=dict(links=links,new_planes=chain.tolist(),path_scores=scores.tolist(),own=own,reference=ref,old_retired=[i for i in range(82) if i not in s['active']],retained_new=[int(i) for i in s['active'] if i>=82])
 rows.append(item)
 print('links',links,'VEF',own['V'],own['E'],own['F'],'own',len(own['S']),len(own['U']),'ref',len(ref['S']),len(ref['U']),'g',own['centroid'],'vol',own['volume'],'retired',len(item['old_retired']),flush=True)
Path(__file__).with_name('BRIDGE111.json').write_text(json.dumps(dict(old_centre=g.tolist(),angle=phi,norm_ratio=rb/ra,rows=rows,numerical_only=True),indent=2)+'\n')
```
### FILE entry_bridge111.py
```python
"""Current-polar-component entry bridges, with complete finite nominations.
Numerical R82 geometry helper/input are supplied by J109 materials.
"""
from __future__ import annotations
import sys,json,math
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'j109'))
from geometry109 import *
q,g,old=load();cent=fast_h(q);edges=cent['qedges']
can={18};changed=True
while changed:
 changed=False
 for i,j in edges:
  for u,v in [(i,j),(j,i)]:
   if v in can and u not in can and q[u]@(q[v]-q[u])>1e-12:can.add(int(u));changed=True
rows=[]
a=q[7];ra=np.linalg.norm(a)
for end in sorted(can):
 b=q[end];rb=np.linalg.norm(b)
 if rb<=ra:continue
 phi=np.arccos(np.clip(a@b/ra/rb,-1,1));e=a/ra;f=(b/rb-np.cos(phi)*e)/np.sin(phi)
 minimum=next((n for n in range(2,129) if (rb/ra)*np.cos(phi/n)**n>1+1e-8),None)
 if minimum is None:continue
 for extra in (0,1,3):
  links=minimum+extra;t=np.arange(1,links)/links
  chain=(ra*(rb/ra)**t)[:,None]*(np.cos(phi*t)[:,None]*e+np.sin(phi*t)[:,None]*f)
  path=np.vstack([a,chain,b]);scores=np.einsum('ij,ij->i',path[:-1],np.diff(path,axis=0));assert min(scores)>0
  aq=np.vstack([q,chain]);s=fast_h(aq);own=census(s);ref=census(s,np.zeros(3))
  row=dict(end=end,minimum_links=minimum,extra=extra,links=links,new_planes=chain.tolist(),path_scores=scores.tolist(),own=own,reference=ref,old_retired=[i for i in range(82) if i not in s['active']])
  rows.append(row)
  print(end,links,'VEF',own['V'],own['E'],own['F'],'own',len(own['S']),len(own['U']),'ref',len(ref['S']),len(ref['U']),'g',round(float(np.linalg.norm(s['centroid'])),6),flush=True)
Path(__file__).with_name('ENTRY_BRIDGE111.json').write_text(json.dumps(dict(old_centre=g.tolist(),can_reach_elder=sorted(can),rows=rows,numerical_only=True),indent=2)+'\n')
```
