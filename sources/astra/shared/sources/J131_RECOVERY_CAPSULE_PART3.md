# J131 Recovery capsule part 3 of 3 — producing methods and finite limits

Mandatory source dependencies are part1 att_64baecde7152c2612025_01 and part2 att_40529ef20d49481a8ee9_01. Parts1+2 alone reconstruct all three exact J131_PARALLEL bodies, their full exact endpoint/path diagnostics and the rank137 certificate. This part closes the numerical producing-method dependency. It is NOT a new own110 record and not an infeasibility theorem. The analytical derivation is preserved separately.

Use UNPACK131.py from part2 with all three readable material files. It extracts the complete named units below. The exact parent remains DETACHED_G6.txt,1034B/SHA a5b7cb7cd10de4a8ba08a997945ee3a932385cf03a5e259946be867954772a50, from J130's standalone source att_e24d68f17ea7f7e16750_01. There are no additional hidden geometric starts.

## Producing commands and finite result ledger
Observed environment CPython3.13.5, NumPy2.3.5, SciPy1.17.0; binary64, OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1. SciPy SLSQP/null_space/Qhull use their defaults except the complete explicit options below. The argument seed is recorded0 but the algorithm draws no random numbers. Floating optimizer bit portability is not promised. Exact frozen free heights are complete in part2, so none of those optimizer outcomes has to reproduce bit-for-bit to reconstruct the exact bodies.

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python search131.py --v 1 0 0 --trust .5 --iterations 60
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python search131.py --v 0 1 0 --trust .5 --iterations 60
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python search131.py --v 0 0 1 --trust .5 --iterations 60
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python forest131.py --v 0 1 0 --iterations 60
```

The first three searches protect the parent U6 and both S with selected nonroot witnesses, actual mass, a5% relative guard floor and5% relative convex-hull margin. They minimize the parent's principal polar persistence depth plus the explicit tiny norm penalty. They do not directly prove whole-basin cancellation. Their exact endpoint freezes use round(binary64 t_i*10^12) on the44 free heights, ties to even, exact rational RREF projection for the three pivot heights, then the exact polynomial retraction. The full integer checkpoints are in part2; do not independently round the final point coordinates.

The corrected x search reaches its60-iteration limit, with best objective about.4467927480; the corrected y and z runs return success at27 and32 iterations. Their exact rational bodies, all47/135/90 own211, have Q~.446793221594605,.438150109628924,.440780104846534. A successful optimizer status is not an own110 claim. Exact X/Y entire paths are separately certified; exact Z midpoint is222, as retained in part2.

A first pilot used hscale=max(abs(h0),1e-6) while its linear lower bound incorrectly presumed the initial normalized hull gap was1 for every row. That scaling was corrected to hscale=abs(h0), which is legitimate because the parent triangular hull is exactly strict. All three retained nominations were rerun with the corrected complete parallel131.py in part1. No conclusion is attributed to the discarded pilot. The part1 final source contains the correction; the only material-transcription patch required is its explicitly labelled allocation-line replacement, applied automatically by UNPACK131.py.

The path checker first attempted to protect one fixed outgoing witness for each nonroot. Its failure on X was a proof restriction, not proof of a bad path. The final checker covers the parameter interval by a union of exact positive witnesses, certifying X/Y with dyadic Bernstein depth at most2. The Z path instead has a genuinely exact extra U at s=1/2. Endpoints plus exact mass do not certify all intermediate equilibrium states.

The whole-polar-forest phase-I control is a finite failed policy, not a family exclusion. Its preserved current output FOREST_0_1_0.json is4205B/SHA eef94dca13db59960fcdb148afbac503e071a0fb7e8dcc578709fdf1f3b84e38. It uses the path
[16,12,11,14,68,79,75,74,72,89,87,83,82,81,80,84,18].
At12 iterations SLSQP reports success but the final slack is1.0464254868162435, not zero; residual feasibility is-5.413815923338561e-11 and minimum relative hull gap.04999999999216393. Floating S=[16,18,87],U=[6]. Thus it neither satisfies the intended one-root polar policy nor yields own110. A transient internal summary had different route/slack/iteration/root values; those were not the preserved output and are explicitly superseded by this direct file reading. No exact new endpoint is promoted from this phase-I control.

Producing-source identities:
- search131.py3278B/SHA483e628b45e699feea9ae37af6f014156b39721cdaf4338bfdc292734c8cdd93
- forest131.py3811B/SHAc1e1465f9e498e6b26c36d7106790b3d43442e66d7cbb4499564615194313493
Recorded numerical nomination identities (supplementary observations, not the exact recovery inputs):
- NOM_1_0_0.json19005B/SHAf658883dfc944b47b591ebe567428f4100f1898b23d1418e4103be075d90802c
- NOM_0_1_0.json12363B/SHAf3d1f7be6200f741cc3e2f4c19757662c39417632ef3d122cc06e5de6de6e85004d is NOT a valid identity: see the immediately following exact correction.
- Correct NOM_0_1_0.json SHA is f3d1f7be6200f741cc3e2f4c19757662c39417632ef3d122cc06e5de6e85004d,12363B.
- NOM_0_0_1.json14782B/SHA38a568dd7d562be2e661de59e86e3a5fbeffcf7ef29dd3370ab0488316a095ff
The source-only exact reconstruction does not consume these large histories. The complete frozen heights in part2, their exact input hash, all helpers and every nondefault parameter are sufficient recovery state.

## File: search131.py
```python
#!/usr/bin/env python3
"""Finite floating nomination, not proof of equilibrium counts or infeasibility.
Fixed triangular lattice, selected roots and escape witnesses, actual mass chart.
Reconstruction of a rational endpoint is independent of this optimizer.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize,LinearConstraint
import engine131 as e,parallel131 as p

def nominate(v,trust,maxiter,seed=0):
 X=e.load();base,fs=e.audit(X);c=p.Chart(X,fs,v,(float(base['volume']),base['centroid']));z0=np.zeros(c.d)
 U,dU,S,dS=c.allguards(z0);up=[];sp=[]
 for i in range(c.N):
  if i in base['U']:up.extend((i,j,-1)for j in c.nb[i])
  else:up.append((i,max(c.nb[i],key=lambda j:U[i,j]),1))
 for f in range(len(fs)):
  if f in base['S_indices']:sp.extend((f,k,1)for k in range(3))
  else:sp.append((f,int(np.argmin(S[f])),-1))
 ug=np.array([s*U[i,j]for i,j,s in up]);sg=np.array([s*S[f,k]for f,k,s in sp]);assert min(ug)>0 and min(sg)>0
 us=ug.copy();ss=sg.copy();cache={}
 def guards(z):
  if 'z' not in cache or not np.array_equal(cache['z'],z):
   u,du,s,ds=c.allguards(z)
   vals=np.r_[np.array([sign*u[i,j]for i,j,sign in up])/us,np.array([sign*s[f,k]for f,k,sign in sp])/ss]-.05
   jac=np.r_[np.array([sign*du[i,j]for i,j,sign in up])/us[:,None],np.array([sign*ds[f,k]for f,k,sign in sp])/ss[:,None]]
   cache.update(z=z.copy(),values=vals,jac=jac)
  return cache['values']
 def jac(z):guards(z);return cache['jac']
 b=base['Q'][0]
 def obj(z):
  val,grad=c.bar(z,b['root'],b['edge']);return val+1e-7*np.dot(z,z),grad+2e-7*z
 hist=[];best=[float(b['depth']),z0.copy()]
 def cb(z):
  val,_=obj(z);gmin=float(min(guards(z)));hmin=float(min(c.hullguard(z)));tm=float(max(abs(c.T@z)))
  row=[len(hist),val,gmin,hmin,tm];hist.append(row)
  if gmin>=-1e-6 and hmin>=.05-1e-6 and val<best[0]:best[:]=[val,z.copy()]
  if len(hist)%10==0:print('ITER',v,*row,flush=True)
 constraints=[LinearConstraint(c.hjac,np.full(len(c.h0),-.95),np.inf),LinearConstraint(c.T,-trust,trust),dict(type='ineq',fun=guards,jac=jac)]
 print('BEGIN',v,trust,maxiter,'margins',min(ug),min(sg),'d',c.d,flush=True)
 r=minimize(obj,z0,jac=True,method='SLSQP',constraints=constraints,callback=cb,options=dict(maxiter=maxiter,ftol=1e-11,disp=False))
 cb(r.x);z=best[1];t,Y,n,dg=c.state(z);q=c.ell@t+t@c.B@t;Z=c.X+(t-q/c.V)[:,None]*c.v
 u,du,s,ds=c.allguards(z);Uc=[i for i in range(c.N)if max(u[i,j]for j in c.nb[i])<0];Sc=[i for i in range(len(fs))if min(s[i])>0]
 out=dict(v=list(v),trust=trust,maxiter=maxiter,seed=seed,result=dict(success=bool(r.success),message=str(r.message),nit=int(r.nit),last_objective=float(r.fun)),best_objective=best[0],t=t.tolist(),points=Z.tolist(),floating_roots=dict(S=Sc,U=Uc),hull_min=float(min(c.hullguard(z))),guard_min=float(min(guards(z))),history=hist,up=up,sp=sp)
 name='NOM_'+('_'.join(map(str,v)))+'.json';e.write(name,out)
 print('DONE',name,out['result'],out['best_objective'],out['floating_roots'],out['guard_min'],flush=True)
 return out
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--v',nargs=3,type=int,default=[0,0,1]);ap.add_argument('--trust',type=float,default=.5);ap.add_argument('--iterations',type=int,default=150);ar=ap.parse_args()
 nominate(ar.v,ar.trust,ar.iterations)
```

## File: forest131.py
```python
#!/usr/bin/env python3
"""Whole-polar-forest phase-I test on a common-direction actual-mass chart.
A positive final slack is a finite numerical failure, NOT a family exclusion.
Uses no unprovided files; the parent DETACHED47 is literal in the source pack.
"""
import argparse,numpy as np
from scipy.optimize import minimize,LinearConstraint
from scipy.sparse.csgraph import dijkstra
import engine131 as e,parallel131 as p

def run(v,maxiter=80,trust=.5):
 X=e.load();base,fs=e.audit(X);fs,hs,es,vs=e.hull(X);c=p.Chart(X,fs,v,(float(base['volume']),base['centroid']));zero=np.zeros(c.d)
 U,dU,S,dS=c.allguards(zero);Q=np.array([e.mul(1/(h-e.dot(n,base['centroid'])),n)for n,h in hs],float)
 birth=base['Q'][0]['root'];elder=next(f for f in base['S_indices']if f!=birth);cost=np.full((len(fs),len(fs)),np.inf);edgeidx={}
 for (a,b),(i,j)in es.items():
  for ii,jj in [(i,j),(j,i)]:
   sc=np.dot(Q[ii],Q[jj]-Q[ii])/np.dot(Q[ii],Q[ii]);cost[ii,jj]=max(0,-sc)+1e-7
   k=next(k for k in range(3)if set([fs[ii][k],fs[ii][(k+1)%3]])=={a,b});edgeidx[ii,jj]=k
   assert sc*S[ii,k]<0
 dist,pred=dijkstra(cost,directed=True,indices=birth,return_predecessors=True);path=[elder]
 while path[-1]!=birth:path.append(int(pred[path[-1]]))
 path=path[::-1];policy={f:int(np.argmin(S[f]))for f in range(len(fs))if f!=elder}
 for i,j in zip(path,path[1:]):policy[i]=edgeidx[i,j]
 up=[]
 for i in range(len(X)):
  if i in base['U']:up.extend((i,j,-1)for j in c.nb[i])
  else:up.append((i,max(c.nb[i],key=lambda j:U[i,j]),1))
 us=np.array([sign*U[i,j]for i,j,sign in up]);ss=np.array([abs(S[f,k])for f,k in policy.items()]);rootS=S[elder].copy();cache={}
 def fun(w):
  if 'w' not in cache or not np.array_equal(cache['w'],w):
   z,slack=w[:-1],w[-1];u,du,s,ds=c.allguards(z)
   physical=np.array([sign*u[i,j]for i,j,sign in up])/us-.05
   physical_j=np.array([sign*du[i,j]for i,j,sign in up])/us[:,None]
   roots=s[elder]/rootS-.05;roots_j=ds[elder]/rootS[:,None]
   polar=np.array([-s[f,k]for f,k in policy.items()])/ss-.05+slack
   polar_j=np.array([-ds[f,k]for f,k in policy.items()])/ss[:,None]
   vals=np.r_[physical,roots,polar];jac=np.zeros((len(vals),len(w)));jac[:,:-1]=np.r_[physical_j,roots_j,polar_j];jac[-len(policy):,-1]=1
   cache.update(w=w.copy(),vals=vals,jac=jac)
  return cache['vals']
 def jac(w):fun(w);return cache['jac']
 def obj(w):return w[-1]+1e-6*np.dot(w[:-1],w[:-1])*np.dot(v,v),np.r_[2e-6*w[:-1]*np.dot(v,v),1.]
 hist=[]
 def cb(w):
  row=[len(hist),float(w[-1]),float(min(fun(w))),float(min(c.hullguard(w[:-1])))];hist.append(row)
  if len(hist)%10==0:print('FOREST',v,row,flush=True)
 hj=np.c_[c.hjac,np.zeros(len(c.h0))];TJ=np.c_[c.T,np.zeros(c.N)]
 con=[LinearConstraint(hj,np.full(len(c.h0),-.95),np.inf),LinearConstraint(TJ,-trust/np.linalg.norm(v),trust/np.linalg.norm(v)),dict(type='ineq',fun=fun,jac=jac)]
 w0=np.r_[zero,1.05];r=minimize(obj,w0,jac=True,method='SLSQP',bounds=[(None,None)]*c.d+[(0,None)],constraints=con,callback=cb,options=dict(maxiter=maxiter,ftol=1e-10))
 u,du,s,ds=c.allguards(r.x[:-1]);Sc=[i for i in range(len(fs))if min(s[i])>0];Uc=[i for i in range(c.N)if max(u[i,j]for j in c.nb[i])<0]
 out=dict(direction=v,trust=trust,maxiter=maxiter,path=path,policy=policy,slack=float(r.x[-1]),feasibility=float(min(fun(r.x))),hull_min=float(min(c.hullguard(r.x[:-1]))),success=bool(r.success),message=str(r.message),iterations=int(r.nit),t=(c.T@r.x[:-1]).tolist(),floating_S=Sc,floating_U=Uc,history=hist)
 name='FOREST_'+('_'.join(map(str,v)))+'.json';e.write(name,out);print('FOREST_DONE',name,out['slack'],out['feasibility'],out['message'],Sc,Uc,flush=True)
 return out
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--v',nargs=3,type=int,default=[0,1,0]);ap.add_argument('--iterations',type=int,default=80);ar=ap.parse_args();run(ar.v,ar.iterations)
```
