# material-077545009f88

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# J128 executed convex slices and actual-centre material chains

Complete new source units, requiring both [internal-source-reference] (literal DETACHED_G6 and exact theorem/generator) and [internal-source-reference] (complete explore.py and apex_scan.py). Run those recovery sources to produce base.npz and apex_scan_result.json; a material ID alone is not a supplied computational dependency. Environment: Python3.13.5, NumPy2.3.5, SciPy1.17.0, OPENBLAS_NUM_THREADS=1.

## Executed results and limits

SLICES128.py used all20 saved one-apex nomination seeds, each with its own fixed visible-face set, fixed added volume, old positive witness forest, and one specified old witness for the new apex. The actual-centroid map is affine on each slice. For each chart48 linear directions in the two-dimensional volume plane were optimized under the certified concave quadratic new-apex guard and affine old-forest/visibility guards. This was909 feasible floating nominations: U histogram {1:909}, S histogram {2:636,3:273}. No S1 candidate. The best S2 boundary nomination has Q~.4608397590454396, slightly worse than the interior SCOUT48_G8. This is an executed use of the input-specific convexity theorem, not a global enumeration of all horizons, volumes, witness choices or full-Q geometries. Numerical SLSQP feasibility and its selected sample points are not a rational certificate for every floating endpoint. No new exact body was promoted. No absence of weak equilibria is inferred from these floating counts.

SECTOR128.py materializes every link of depth1/2/3 support-envelope chains. It uses38/19/12 target directions respectively, so at most85 submitted points. All target angular caps, old-parent selection, contraction factors, phase, centre-root solver and tolerances are explicit in the source. This is84 finite configurations,82 with numerical homogeneous-centre closure residual<1e-8. Among those82 the new-point-to-parent radial guards were all positive (smallest~.00003860412706007283), but current old vertices created many U: U range16..35. The lowest-U trial was depth2,19 directions, angular radius1.8, phase.37, alpha.99, side1, root-only parent6; nominal65/189/126, S5/U16, actual centre~(-.09686719160345508,-.02242332026507733,.015209619314898217), volume~.9368219579484625. Thus closing the actual centre and realizing every NEW link did not preserve the old U1 forest. This is a finite failed set, not an exclusion of all recursive chains, and these bodies have not received exact census or been promoted. The remaining two solver outcomes are not claimed closed-centre bodies.

Commands:
```
OPENBLAS_NUM_THREADS=1 python explore.py
OPENBLAS_NUM_THREADS=1 python apex_scan.py
OPENBLAS_NUM_THREADS=1 python SLICES128.py
OPENBLAS_NUM_THREADS=1 python SECTOR128.py 0
OPENBLAS_NUM_THREADS=1 python SECTOR128.py 1
OPENBLAS_NUM_THREADS=1 python SECTOR128.py 2
```
Expected final slice marker: SLICES128_DONE 909. The output histograms are {1:909} and {2:636,3:273}. Each sector part runs28 indexed cases0..27 and stores the complete generated point arrays whenever centre closure passes the specified tolerance. These are fully reproducible source inputs/parameters, not omitted NPZ checkpoints.

Source/output byte counts and observed hashes:
- SLICES128.py3292 bytes; SHA408529020e00195dbfaad45001146d4c95af59570faa43f672fe0528b8aa9266.
- SECTOR128.py4225 bytes; SHAd40c25000b62ede8c702ef5e012d9bc67461f9898a27a5b7599ecc07ca4bde66.
- SLICES128_RESULTS.json15701 bytes; SHA183000f44e0d8fefd4e003ab9edfb830f81de0b4e2247a114c24793fb31c3d19.
- SECTOR128_part0.json231902 bytes; SHAe5b1d3339af79df78a17904392d50d32f5cd260c56bbb1294b87bf43f82c889a.
- SECTOR128_part1.json225080 bytes; SHA4480763888c559e43df6ddfc66e1061c3aa6f2584114ed68eb5d2cf04dd22c31.
- SECTOR128_part2.json219305 bytes; SHAb025459538449e688a894a75c30980571e07c797ac44b19c6c0eddaec7eac4ff.
Floating numerical-stack changes may alter last bits or active-set solver paths. All exact accepted claims remain those of the separate rational capsule, not these report hashes.

## File: SLICES128.py
```python
#!/usr/bin/env python3
"""J128 finite convex fixed-volume/horizon/selected-witness slice exploration.
This uses the rationally proved cap-concavity lemma, but floating optimization is
only a nomination method. Requires apex_scan.py, explore.py/base.npz and its
saved 20 best seeds. The old selected forest is part of each chart, not an
assumption that arbitrary own-U1 bodies form one convex family.
"""
from apex_scan import *
from scipy.optimize import minimize
EPS=1e-9

def chart(z):
 vis=N@z-d>0;aa=(area[vis,None]*N[vis]).sum(0)/3;bb=float(area[vis]@d[vis]/3)
 mu=float(aa@z-bb);Bmat=np.einsum('ni,nj->ij',bc[vis],area[vis,None]*N[vis])/4
 dm=np.einsum('n,ni->i',area[vis]*d[vis]/4,bc[vis]);A=(mu*np.eye(3)/4+Bmat)/(V+mu);c=(V*g0-dm)/(V+mu)
 _,G,_=mass(z[None,:]);G=G[0];assert np.linalg.norm(A@z+c-G)<1e-12
 M=np.eye(3)-A;assert np.linalg.eigvalsh((M+M.T)/2).min()>.5
 sc=old0-np.einsum('k,ijk->ij',G,D);roots=np.flatnonzero(sc.max(1)<0)
 if len(roots)!=1:return None
 rr=int(roots[0]);inds=np.array([i for i in range(len(X))if i!=rr]);par=sc.argmax(1)[inds];dx=X[par]-X[inds]
 wit=int(np.argmax((z-G)@(X-z).T));
 if (z-G)@(X[wit]-z)<=EPS:return None
 e=np.eye(3)[np.argmin(abs(aa))];e=np.cross(aa,e);e/=np.linalg.norm(e);f=np.cross(aa,e);f/=np.linalg.norm(f);T=np.column_stack([e,f])
 sig=np.where(vis,1.,-1.);L=np.r_[sig[:,None]*(N@T),-dx@A@T];b=np.r_[sig*(N@z-d)-1e-11,np.einsum('ij,ij->i',X[inds]-(A@z+c),dx)-EPS]
 v=X[wit]
 def cons(t):
  w=z+T@t;return np.r_[L@t+b,(w-A@w-c)@(v-w)-EPS]
 def jac(t):
  w=z+T@t;return np.vstack([L,((M.T@v-(M+M.T)@w+c)@T)[None,:]])
 return dict(z=z,T=T,L=L,b=b,cons=cons,jac=jac,witness=wit,root=rr,visible=np.flatnonzero(vis).tolist(),volume=mu,parents=list(zip(inds.tolist(),par.tolist())))

def main():
 raw=json.loads(Path(__file__).with_name('apex_scan_result.json').read_text());seeds=[r['a']for r in raw['best']];allout=[];skip=[];st=time.time()
 for k,z0 in enumerate(seeds):
  ch=chart(np.array(z0))
  if ch is None:skip.append(k);continue
  c=ch;outs=[]
  for j in range(48):
   n=np.array([np.cos(2*np.pi*j/48),np.sin(2*np.pi*j/48)])
   sol=minimize(lambda t:-n@t,np.zeros(2),jac=lambda t:-n,method='SLSQP',constraints={'type':'ineq','fun':c['cons'],'jac':c['jac']},options={'ftol':1e-12,'maxiter':150})
   guard=float(c['cons'](sol.x).min());a=c['z']+c['T']@sol.x
   if guard < -1e-10:continue
   s=state(a)
   if s is None:continue
   _,gg,_=mass(a[None,:]);cnt,_,_=countU(a[None,:],gg)
   s.update(seed=k,direction=j,guard=guard,success=bool(sol.success),U=int(cnt[0]),witness=c['witness'],oldroot=c['root'])
   outs.append(s)
  print('chart',k,'visible',c['visible'],'volume',c['volume'],'feasible',len(outs),'best',min([(o['S'],sum(o['Q']))for o in outs],default=None),flush=True)
  allout+=outs
 allout.sort(key=lambda q:(q['U'],q['S'],sum(q['Q'])))
 from collections import Counter
 result=dict(seeds=len(seeds),directions=48,epsilon=EPS,skipped_seeds=skip,feasible_nomination_count=len(allout),U_histogram=dict(Counter(q['U']for q in allout)),S_histogram=dict(Counter(q['S']for q in allout)),best=allout[:30])
 Path(__file__).with_name('SLICES128_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
 print('SLICES128_DONE',len(allout),'elapsed',time.time()-st,'best',allout[:1],flush=True)
if __name__=='__main__':main()
```

## File: SECTOR128.py
```python
#!/usr/bin/env python3
"""Finite material realization of depth-m support envelopes with actual-centre closure.
Dependency: DETACHED_G6.txt and explore.py/base.npz from J128. Numerical nomination
only; all intermediate chain points are material, never virtual shortcuts.
"""
import json,sys,time
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import root
D=Path(__file__).resolve().parent
B=np.load(D/'base.npz');X=B['X'];g0=B['g'];S=B['S'];N=B['N'];Y=B['Y']

def mass(X):
 H=ConvexHull(X);T=X[H.simplices].copy();cr=np.cross(T[:,1]-T[:,0],T[:,2]-T[:,0]);flip=(cr*H.equations[:,:3]).sum(1)<0;T[flip]=T[flip][:,[0,2,1]]
 ds=np.einsum('ij,ij->i',T[:,0],np.cross(T[:,1],T[:,2]));vol=ds.sum()/6;g=(ds[:,None]*T.sum(1)).sum(0)/(24*vol)
 return H,float(vol),g

def census(XX,H,g):
 YY=XX[H.vertices]-g;Z=H.equations[:,:3]/(-H.equations[:,3]-H.equations[:,:3]@g)[:,None]
 def crit(P):
  A=P@P.T-(P*P).sum(1)[:,None];np.fill_diagonal(A,-np.inf);return np.flatnonzero(A.max(1)<-1e-10)
 uu=crit(YY);ss=crit(Z)
 def bars(P,edges):
  rr=(P*P).sum(1);pr=list(range(len(P)));peak=rr.copy();links=[]
  def rt(a):
   while pr[a]!=a:pr[a]=pr[pr[a]];a=pr[a]
   return a
  for i,j in edges:
   d=P[j]-P[i];dd=d@d
   if dd<1e-28:continue
   t=np.clip(-P[i]@d/dd,0,1);p=P[i]+t*d;links.append((float(p@p),i,j))
  out=[]
  for l,i,j in sorted(links,reverse=True):
   i,j=rt(i),rt(j)
   if i==j:continue
   if peak[i]<peak[j]:i,j=j,i
   q=1-l/peak[j]
   if q>1e-11:out.append(float(q))
   pr[j]=i
  return sorted(out,reverse=True)
 ed=set(tuple(sorted((i,int(j))))for i,nb in enumerate(H.neighbors)for j in nb if j>=0)
 return dict(V=len(H.vertices),E_upper=3*len(H.vertices)-6,F_triangles=len(H.simplices),U=H.vertices[uu].tolist(),S=len(ss),Q=bars(Z,ed))

def directions(axis,k,angle,phase):
 axis=np.array(axis);axis/=np.linalg.norm(axis);e=np.eye(3)[np.argmin(abs(axis))];e=np.cross(axis,e);e/=np.linalg.norm(e);f=np.cross(axis,e)
 # Golden-angle disk in a spherical cap, including its centre.
 out=[axis]
 for j in range(1,k):
  th=angle*np.sqrt(j/(k-1));ph=phase+np.pi*(3-np.sqrt(5))*j
  out.append(np.cos(th)*axis+np.sin(th)*(np.cos(ph)*e+np.sin(ph)*f))
 return np.array(out)

def construct(c,dirs,m,alpha,selection):
 Y=X-c;rr=np.linalg.norm(Y,axis=1);un=Y/rr[:,None];out=[];parents=[]
 for n in dirs:
  ang=np.arccos(np.clip(un@n,-1,1));val=rr*np.cos(ang/(m+1))**(m+1)
  i=int(np.argmax(val))if selection=='all'else 6
  u=un[i];theta=ang[i];e=n-np.dot(n,u)*u;ee=np.linalg.norm(e)
  if ee<1e-10:
   e=np.eye(3)[np.argmin(abs(u))];e=e-np.dot(e,u)*u;ee=np.linalg.norm(e)
  e/=ee;phi=theta/(m+1);r=rr[i];prev=i
  for j in range(1,m+1):
   r*=alpha*np.cos(phi);z=c+r*(np.cos(j*phi)*u+np.sin(j*phi)*e)
   parents.append(prev);out.append(z);prev=len(X)+len(out)-1
 return np.vstack([X,np.array(out)]),parents

def trial(cfg):
 m,k,ang,phase,alpha,which,selection=cfg;axis=N[S[which]];dirs=directions(axis,k,ang,phase)
 def fun(c):
  try:XX,_=construct(c,dirs,m,alpha,selection);return mass(XX)[2]-c
  except Exception:return np.ones(3)*10
 sol=root(fun,g0,method='hybr',options={'xtol':1e-10,'maxfev':250})
 XX,parents=construct(sol.x,dirs,m,alpha,selection);H,V,g=mass(XX);res=float(np.linalg.norm(g-sol.x));cens=census(XX,H,g)
 q=dict(config=list(cfg),success=bool(sol.success),residual=res,nfev=sol.nfev,centre=g.tolist(),volume=V,submitted=len(XX),**cens)
 if res<1e-8:
  scores=[float((XX[47+j]-g)@(XX[p]-XX[47+j]))for j,p in enumerate(parents)]
  q['min_new_material_guard']=min(scores);q['vertices']=XX.tolist()
 return q

def main():
 part=int(sys.argv[1])if len(sys.argv)>1 else 0;configs=[]
 for m in [1,2,3]:
  for angle in [.3,.6,1.,1.4,1.8,2.2,2.7]:
   for which in [0,1]:
    for sel in ['all','root']:
     configs.append((m,38//m,angle,.37,.99,which,sel))
 configs=configs[part*28:(part+1)*28];out=[];st=time.time()
 for j,cfg in enumerate(configs):
  try:r=trial(cfg)
  except Exception as e:r={'config':list(cfg),'error':repr(e)}
  out.append(r);print(part,j,'res',r.get('residual'),'S',r.get('S'),'U',len(r.get('U',[])),'Q',r.get('Q'),'sec',time.time()-st,flush=True)
 (D/f'SECTOR128_part{part}.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
```
