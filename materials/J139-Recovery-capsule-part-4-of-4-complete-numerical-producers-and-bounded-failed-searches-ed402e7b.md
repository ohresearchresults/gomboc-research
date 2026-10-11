# material-ed402e7b52aa

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# J139 recovery capsule, part 4/4: executed numerical methods

This closes the four-part J139 recovery set. Part1/proofs is [internal-source-reference]; part2/exact cycle checkpoints and auditor is [internal-source-reference]; part3/exact all-path exclusions and ray escape is [internal-source-reference]. Both unchanged J137 dependencies remain required for the whole set: [internal-source-reference]/exact137.py and [internal-source-reference]/LOW43.json. This part's numerical programs need only the latter input and the complete seven sources below. No hidden optimizer checkpoint is required to define these searches. The exact HIGH/ROOT bodies are instead recovered directly from part2's literal rational checkpoints, without rerunning a floating optimizer.

These are numerical nominations and finite failures, not exact class or global exclusion certificates. Numerical dependency versions: CPython3.13.5, NumPy2.3.5, SciPy1.17.0, PyTorch2.10.0+cpu for rayflow139 only. One BLAS/OpenMP/Torch thread. No randomness. Every nondefault parameter in the executed selected runs is specified below. No Clarabel/CVXPY computation was performed. Floating trajectories and output hashes can depend on the arithmetic environment; the exact part2/3 inputs and results do not depend on reproducing them.

Extract each file with regex `r'### File: ([^\n]+)\n```[^\n]*\n(.*?)```'`, re.S, and write group2 verbatim UTF-8, retaining its final newline.

## Executed commands and interpretation
```
python radial139.py base 0
python radial139.py high -0.1
python radial139.py root -0.1
python rayflow139.py 80 0.03
python envelope139_scout.py
python reflect139_scout.py
python pointcone139.py 34 0.1 500
python pointcone139.py 42 4 500
python rayinsert139.py
python pointcone_added139.py 0 0.99 1000
```

The global reciprocal-radius producer uses actual hull rebuilding, positive-weight balancing and a finite smooth-max fan bundle. HIGH and ROOT numerical centroids reach norms about1.46e-9 and5.81e-10. Their selected rational checkpoints and exact all-global-minimizer failures are in parts1/2. A generic implementation edge case is preserved honestly: if solve_bundle exhausts maxfans exactly after appending a new fan, its returned fan list can be one longer than the last lambda vector. The executed HIGH/ROOT calls ended earlier and are unaffected. A successor changing the cap should handle that final append explicitly, rather than treating mismatched lengths as an accepted mixture.

The rayflow run accepted18 steps, then stalled on attempted step18, with numerical principal P .5336028463920628 -> .5333688691900722. It reconstructs actual mass at endpoints but uses a state-dependent guard floor and floating admission. It is NOT an exact clean121 trajectory, a cancellation, or a radial-family exclusion. It illustrates the limitations of this particular local witness/floor policy.

The two fixed all-path-tree centering runs were failures, NOT feasibility proofs for the remaining roots. The preserved actual outputs are: root34,power.1,maxiter500 => status9/iteration limit,500 iterations,2535 evaluations,best normalized squared centroid objective .06468826369353446; root42,power4,maxiter500 => status8/positive directional derivative,373 iterations,1348 evaluations,best objective .1495158101451755. Their approximate own S/U counts are14/25 and8/6, respectively; neither is an exact census. The extra-ray root0,.99 per-edge attenuation,maxiter1000 run ends status9,1000 iterations,6670 evaluations,best objective .07554327733644903, approximate S/U12/13. Opening the necessary outer reflection gate therefore did NOT close actual mass under this finite selected tree/bound policy. These final saved outputs, not any earlier transient trial or displayed intermediate count, define the recorded numerical failures.

The all-pair new-ray scout evaluates764 acute-pair bisectors;236 pass its floating outer-reflection test. Its best pair is old0/10. The rational direction and exact strict-interior witness are preserved and proved in part3; no float scout sign supplies that acceptance.

## Source receipts
radial139.py7655B,SHAe4a403a95febb125ec5baf57c691668f13d775efc9708edb398509c791213711;
rayflow139.py5088B,SHA3f66060098489aba8f0f4afe0193b247ccb8dee6cc539d7795f25cb4efde55e7;
pointcone139.py2714B,SHAf9fe62192f9f1092a4adda3ff35795a57d6f76e7f2fa9af06a62692175a1aa5e;
pointcone_added139.py2955B,SHA7df0541654e03594e2cf9a183d07ba4a72b2a76fef6b7c93e9b081ad4fa68513;
envelope139_scout.py961B,SHA5f0187e5a14bcb0fb806561d194c02af56ec2bfb62f49f2b35a20bd115eff61d;
reflect139_scout.py1540B,SHAafac410a4939f12dd58aa302bb69bf62ffd87bb9420349af3dbb354d24c21460;
rayinsert139.py1161B,SHAc440b034b20e2ab2862692ba0962b3fbc9cecc7e597601fe6d0e7c37d5dac9e0.

## Observed numerical output receipts
These identify the executed reports; they are not portable mathematical acceptance markers. A rerun prints FINAL/BUNDLE, FINAL/RAYFLOW, or the POINTCONE filename and solver status; the envelope scouts write the named reports. Exact PASS markers are specified separately in parts2/3.
BUNDLE139_base_0.0.json15328B,SHA05954a3144e16cf8517dcdd26b41433446c7f148e3be3de25b3c4d74f1d75b55;
BUNDLE139_high_-0.1.json207740B,SHA779296c2513eb7ac901e7c7778f1e161d9459e39e6c21b2d9af30b168ad0a5ca;
BUNDLE139_root_-0.1.json110572B,SHA3247a50827bb4e8a3b7ae1b9f0a3d3b551e9301bd164750bb6598af8dcefa7b8;
RAYFLOW139.json16628B,SHAb9b0d5507e64c33a20906f6e6b26dfb5f45b66df9dc24133dc7170e6f3fb9963;
POINTCONE139_r34_p0.1.json110254B,SHA3f25e376271145431812cb9113834b77126da90020f7097a2e2ec774bdced2a1;
POINTCONE139_r42_p4.0.json80756B,SHA8d7e8408cead2b3259290a54a9e62c6722b05291febc7b851ee1f6ac7249a2d7;
POINTCONE_ADDED139_r0_p0.99.json20998B,SHA1d4f64ff52fd91fd73a1e3ec1e5b16a9cca9c1e607577071f9079f73499f9d61;
ENVELOPE139_SCOUT.json60525B,SHA1d623dd538202588d3a304e7e05d961bd1069cd85f2938851621101f31509544;
REFLECT139_SCOUT.json66470B,SHAb1f2dca7f663dd63a4ffdd73329a3e281af13842aca7067e466d85b62e531082;
RAYINSERT139_SCOUT.json4534B,SHA264f629772a962fe650d5cca6c42201b6a8b2802427f44e7874a6c62259ecb5d.

### File: radial139.py
```python
"""Global reciprocal-radius volume bundle; actual hull is re-integrated.
Numerical experiments only: no floating tolerance is an exact class proof.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import json, sys, math, hashlib, warnings
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
from scipy.special import logsumexp
from scipy.linalg import solve

class Fan:
 def __init__(self,R,tri):
  self.R=R;self.tri=np.asarray(sorted(tuple(sorted(map(int,f))) for f in tri),int)
  self.key=tuple(map(tuple,self.tri));self.a=np.abs(np.linalg.det(R[self.tri]))/6
  if np.min(self.a)<=0:raise ValueError('degenerate radial triangle')
 def evaluate(self,t,hessian=False):
  q=self.tri; inv=1/t[q];v=self.a*np.prod(inv,axis=1);V=float(v.sum());g=np.zeros(len(t))
  np.add.at(g,q.ravel(),(-v[:,None]*inv).ravel())
  if not hessian:return V,g
  H=np.zeros((len(t),len(t)))
  for i in range(3):
   for j in range(3):np.add.at(H,(q[:,i],q[:,j]),v*inv[:,i]*inv[:,j]*(2 if i==j else 1))
  return V,g,H
 def moment(self,t):
  q=self.tri;v=self.a/np.prod(t[q],axis=1)
  return np.sum(v[:,None]*np.sum(self.R[q]/t[q,None],axis=1)/4,axis=0)

def actual(R,t):
 X=R/t[:,None];h=ConvexHull(X)
 if np.max(h.equations[:,3])>=0:raise ValueError('origin outside actual hull')
 f=Fan(R,h.simplices);v,_=f.evaluate(t);m=f.moment(t)
 return f,v,m/v,X,h

def soft(fans,t,w,mu,hess=True):
 ev=[f.evaluate(t,hess) for f in fans];vs=np.array([a[0] for a in ev]);gs=np.array([a[1] for a in ev])
 vmax=vs.max();ls=logsumexp((vs-vmax)/mu);weights=np.exp((vs-vmax)/mu-ls)
 g=weights@gs;obj=vmax+mu*ls+w@t
 if not hess:return obj,g+w,weights,vs
 hs=np.array([a[2] for a in ev]);diff=gs-g
 H=np.einsum('i,ijk->jk',weights,hs)+(diff.T*weights)@diff/mu
 return obj,g+w,H,weights,vs

def newton(fans,w,t,mu,maxiter=120):
 t=t.copy();records=[]
 for it in range(maxiter):
  obj,g,H,lam,vs=soft(fans,t,w,mu)
  # Diagonal scaling is important when tiny LOW-platform rays have tiny weights.
  d=1/np.sqrt(np.maximum(np.diag(H),1e-30));HH=(d[:,None]*H)*d[None,:]
  try:p=d*solve(HH,-g*d,assume_a='pos',check_finite=False)
  except Exception:p=d*np.linalg.lstsq(HH,-g*d,rcond=1e-14)[0]
  dec=-float(g@p)
  records.append([it,float(obj),float(np.max(np.abs(g))),dec])
  if dec<2e-23:return t,records,'decrement'
  if dec<=0:return t,records,'non_descent'
  a=min(1.,.99*min((-t[p<0]/p[p<0]),default=100))
  for _ in range(60):
   tt=t+a*p
   if np.min(tt)>0 and soft(fans,tt,w,mu,False)[0]<=obj+min(1e-4*a*(g@p),-1e-16*abs(obj)):break
   a*=.5
  else:return t,records,'line_search'
  if a*np.max(np.abs(p))<1e-14:return t,records,'step_floor'
  t=tt
 return t,records,'iteration_limit'

def solve_bundle(R,w,t=None,maxfans=120,mu=1e-10,gap_tol=1e-9,initial_fans=None,verbose=False):
 t=np.ones(len(R)) if t is None else t.copy()
 f,*_=actual(R,t);fans=[] if initial_fans is None else list(initial_fans);keys={x.key for x in fans}
 if f.key not in keys:fans.append(f);keys.add(f.key)
 hist=[]
 for k in range(maxfans):
  t,nh,status=newton(fans,w,t,mu)
  f,V,g,X,h=actual(R,t);obj,res,H,lam,vs=soft(fans,t,w,mu);vbar=lam@vs
  Mbar=sum((l*ff.moment(t) for l,ff in zip(lam,fans)),np.zeros(3))
  rmax=float(np.linalg.norm(X,axis=1).max());delta=V-vbar
  bound=(rmax*max(0,delta)+np.linalg.norm(R.T@res)/4+np.linalg.norm(R.T@w)/4)/V
  rec={'round':k,'fans':len(fans),'triangles':len({q for ff in fans for q in ff.key}),'V':V,'vbar':float(vbar),'separation':float(V-max(vs)),'gap_relative':float(delta/V),'centroid_norm':float(np.linalg.norm(g)),'centroid_bound':float(bound),'mass_identity_error':float(np.linalg.norm(Mbar+(R.T@(res-w))/4)),'stationarity_linf':float(np.max(np.abs(res))),'newton_status':status,'newton_steps':len(nh),'newton_decrement':nh[-1][-1]}
  hist.append(rec)
  if verbose:print(json.dumps(rec),flush=True)
  if delta/V<gap_tol and np.linalg.norm(g)/rmax<gap_tol*2:break
  if f.key in keys:
   if mu>1e-13:mu*=.1;continue
   break
  fans.append(f);keys.add(f.key)
 return {'t':t.tolist(),'weights':w.tolist(),'R':R.tolist(),'mu':mu,'fans':[ff.tri.tolist() for ff in fans],'lambda':lam.tolist(),'history':hist,'points':X.tolist(),'centroid':g.tolist()},fans

def balance(R,w):
 """Exponential tilt of positive baseline, solved in three dimensions."""
 b=np.zeros(3)
 for _ in range(80):
  ww=w*np.exp(R@b);g=R.T@ww;H=R.T@(ww[:,None]*R)
  p=solve(H,-g,assume_a='pos')
  if np.linalg.norm(g)<1e-15*ww.sum():break
  a=1.;f=ww.sum()
  for z in range(50):
   if np.sum(w*np.exp(R@(b+a*p)))<=f+1e-4*a*g@p:break
   a*=.5
  b+=a*p
 return w*np.exp(R@b),b

def load_rays(path='LOW43.json'):
 src=json.loads(Path(path).read_text());x=np.asarray(src['rows'],float)/src['denominator'];h=ConvexHull(x)
 tri=h.simplices.copy()
 for k,q in enumerate(tri):
  # Outward orientation, valid also when raw origin is outside.
  if np.dot(np.cross(x[q[1]]-x[q[0]],x[q[2]]-x[q[0]]),h.equations[k,:3])<0:tri[k,[1,2]]=tri[k,[2,1]]
 d=np.linalg.det(x[tri]);vol=d.sum()/6;g=(d[:,None]*x[tri].sum(axis=1)).sum(axis=0)/(24*vol)
 R=x-g;f,V,c,X,h=actual(R,np.ones(len(R)));w=-f.evaluate(np.ones(len(R)))[1]
 if np.min(w)<=0:raise ValueError('initial fan omits some rays')
 return R,w,f,g

def numeric_census(X,tol=1e-8):
 h=ConvexHull(X);d=np.abs(np.linalg.det(X[h.simplices]))
 # This function is called only after translating to an interior point.
 V=d.sum()/6;g=(d[:,None]*X[h.simplices].sum(axis=1)).sum(axis=0)/(24*V)
 X=X-g;h=ConvexHull(X);norm=h.equations[:,:3]/(-h.equations[:,3,None]);keep=[]
 for n in norm:
  if not any(np.linalg.norm(n-m)<=tol*(1+np.linalg.norm(n)) for m in keep):keep.append(n)
 Q=np.array(keep);P=X[h.vertices]
 def scores(A):
  D=A[None,:,:]-A[:,None,:];num=np.einsum('ik,ijk->ij',A,D);den=np.linalg.norm(A,axis=1)[:,None]*np.linalg.norm(D,axis=2)
  z=np.divide(num,den,out=np.full_like(num,-np.inf),where=den>1e-20);return z.max(axis=1)
 p,q=scores(P),scores(Q)
 return {'approxV':len(P),'approxF':len(Q),'S':int(np.sum(q<0)),'U':int(np.sum(p<0)),'nearzeroP':int(np.sum(np.abs(p)<tol)),'nearzeroQ':int(np.sum(np.abs(q)<tol)),'rootP':p[p<0].tolist(),'rootQ':q[q<0].tolist(),'volume':float(V),'raw_centroid':g.tolist()}

if __name__=='__main__':
 mode=sys.argv[1] if len(sys.argv)>1 else 'base';strength=float(sys.argv[2]) if len(sys.argv)>2 else -.1
 R,w,f,rawg=load_rays();eta=np.zeros(len(R))
 if mode=='high':
  # Actual source's graph-superlevel component, not the full chord complement.
  _,_,_,X,h=actual(R,np.ones(len(R)));rad=np.sum(R*R,axis=1);adj=[set() for _ in R]
  for q in h.simplices:
   for i in range(3):a,b=q[i],q[(i+1)%3];adj[a].add(b);adj[b].add(a)
  z=numeric_census(R);scores=(R@R.T)-rad[:,None];np.fill_diagonal(scores,-np.inf)
  roots=np.flatnonzero(scores.max(axis=1)<0);junior=roots[np.argmin(rad[roots])];death=.23912616515768817
  seen={int(junior)};todo=[int(junior)]
  while todo:
   i=todo.pop()
   for j in adj[i]:
    if rad[j]>death and j not in seen:seen.add(j);todo.append(j)
  eta[list(seen)]=strength
 elif mode=='root':
  rad=np.sum(R*R,axis=1);scores=(R@R.T)-rad[:,None];np.fill_diagonal(scores,-np.inf);roots=np.flatnonzero(scores.max(axis=1)<0);eta[roots[np.argmin(rad[roots])]]=strength
 elif mode!='base':raise ValueError(mode)
 ww,b=balance(R,w*np.exp(eta));result,fans=solve_bundle(R,ww,maxfans=160,mu=1e-9,gap_tol=1e-8,verbose=True)
 result.update({'mode':mode,'strength':strength,'eta':eta.tolist(),'balancing_b':b.tolist(),'raw_parent_centroid':rawg.tolist(),'census':numeric_census(np.array(result['points']))})
 out=Path('BUNDLE139_'+mode+'_'+str(strength)+'.json');out.write_text(json.dumps(result,indent=2)+'\n');print('FINAL',out,result['census'],flush=True)
```

### File: rayflow139.py
```python
"""Finite actual-centred, fixed-ray deformation with all-root guard admission.
A bounded scout; LP derivatives use the current fan, finite endpoints rebuild it.
"""
from radial139 import *
import torch
from scipy.optimize import linprog
DT=torch.float64;torch.set_num_threads(1)

def geom(R,t):
 f,V,g,X,h=actual(R,t);q=f.tri;vv=f.a/np.prod(t[q],axis=1);Y=X[q];s=Y.sum(axis=1)
 second=np.sum(vv[:,None,None]*(np.einsum('nki,nkj->nij',Y,Y)+s[:,:,None]*s[:,None,:])/20,axis=0)/V
 return f,V,g,second,X,h

def center(R,t):
 t=t.copy()
 for _ in range(25):
  f,V,g,Q,X,h=geom(R,t)
  if np.linalg.norm(g)<2e-13:return t
  b=solve(5*Q-4*np.outer(g,g),g,assume_a='pos');dt=R@b
  a=min(1.,.9*min((-t[dt<0]/dt[dt<0]),default=100))
  for k in range(40):
   if np.linalg.norm(actual(R,t+a*dt)[2])<np.linalg.norm(g)*(1-.05*a):break
   a*=.5
  else:raise RuntimeError('projective Newton failed')
  t+=a*dt
 raise RuntimeError('projective Newton limit')

def bars(X,edges):
 rad=np.sum(X*X,axis=1);events=[(-float(r),0,i) for i,r in enumerate(rad)]
 for k,(a,b) in enumerate(edges):
  e=X[b]-X[a];q=X[a]+np.clip(-X[a]@e/(e@e),0,1)*e;events.append((-float(q@q),1,k))
 events.sort();uf=list(range(len(X)));elder=list(range(len(X)));out=[]
 def root(i):
  while uf[i]!=i:uf[i]=uf[uf[i]];i=uf[i]
  return i
 for v,typ,k in events:
  if typ==0:continue
  a,b=map(root,edges[k])
  if a==b:continue
  u,z=elder[a],elder[b]
  if (rad[u],-u)<(rad[z],-z):a,b=b,a;u,z=z,u
  if rad[z]+v>1e-13:out.append((float((rad[z]+v)/rad[z]),int(z),edges[k]))
  uf[b]=a;elder[a]=u
 return sorted(out,reverse=True)

def topology(R,t):
 f,V,g,X,h=actual(R,t);X=X-g
 # This scout rejects coplanar/retired-point events rather than counting diagonals as real edges.
 if len(h.vertices)!=len(R):return None
 pol=h.equations[:,:3]/(-h.equations[:,3,None]-h.equations[:,:3]@g[:,None])
 if len(set(tuple(np.round(n,10)) for n in pol))!=len(pol):return None
 edges=sorted({tuple(sorted((int(q[i]),int(q[(i+1)%3])))) for q in h.simplices for i in range(3)})
 def guards(A):
  D=A[None,:,:]-A[:,None,:];num=np.einsum('ik,ijk->ij',A,D);den=np.linalg.norm(A,axis=1)[:,None]*np.linalg.norm(D,axis=2)
  B=np.divide(num,den,out=np.full_like(num,-np.inf),where=den>1e-20);return B.max(axis=1),B.argmax(axis=1)
 pg,pj=guards(X);qg,qj=guards(pol);P=bars(X,edges)
 return h,edges,pg,pj,qg,qj,P,g,V

def torch_values(R,t,h,ps,qs,bar):
 x=R/t[:,None];tri=torch.as_tensor(h.simplices.copy(),dtype=torch.long);Y=x[tri];d=torch.linalg.det(Y).abs()/6;V=d.sum();g=(d[:,None]*Y.sum(dim=1)/4).sum(dim=0)/V;X=x-g
 Rf=R[tri];n=torch.linalg.solve(Rf,t[tri].unsqueeze(-1)).squeeze(-1);pol=n/(1-n@g)[:,None]
 def value(A,pairs):
  i,j=pairs;D=A[j]-A[i];return (A[i]*D).sum(dim=1)/(torch.linalg.vector_norm(A[i],dim=1)*torch.linalg.vector_norm(D,dim=1))
 p=value(X,ps);q=value(pol,qs);_,birth,(a,b)=bar;e=X[b]-X[a];foot=X[a]-(X[a]@e)/(e@e)*e;dep=1-(foot@foot)/(X[birth]@X[birth])
 return torch.cat((dep[None],g,V[None],p,q))

def run(nsteps=80,trust=.03):
 R,w,f,rawg=load_rays();t=np.ones(len(R));history=[];RT=torch.tensor(R,dtype=DT);best=t.copy()
 for k in range(nsteps):
  top=topology(R,t)
  if top is None:break
  h,e,pg,pj,qg,qj,P,g,V=top;Us=np.flatnonzero(pg<0);Ss=np.flatnonzero(qg<0)
  if len(Us)>2 or len(Ss)!=1 or len(P)>1:raise RuntimeError('unexpected fragmented current geometry')
  if len(Us)==1:break
  pi=np.flatnonzero(pg>0);qi=np.flatnonzero(qg>0);ps=(torch.tensor(pi),torch.tensor(pj[pi]));qs=(torch.tensor(qi),torch.tensor(qj[qi]))
  T=torch.tensor(t,dtype=DT,requires_grad=True)
  fun=lambda tt:torch_values(RT,tt,h,ps,qs,P[0])
  val=fun(T).detach().numpy();J=torch.autograd.functional.jacobian(fun,T).detach().numpy()
  floor=np.minimum(np.concatenate((pg[pi],qg[qi]))*.5,1e-6)
  opt=linprog(J[0],A_ub=-J[5:],b_ub=val[5:]-floor,A_eq=J[1:5],b_eq=np.zeros(4),bounds=[(-trust*v,trust*v) for v in t],method='highs')
  if not opt.success:
   history.append({'step':k,'status':'LP_failure','message':opt.message});break
  p=opt.x;a=1.;accepted=False
  for ls in range(35):
   try:tt=center(R,t+a*p);tt*=t[0]/tt[0];nxt=topology(R,tt)
   except Exception:nxt=None
   if nxt is not None:
    hh,ee,pp,_,qq,_,PB,gg,VV=nxt
    if np.sum(pp<0)<=2 and np.sum(qq<0)==1 and len(PB)<=1 and (not PB or PB[0][0]<P[0][0]-1e-12):accepted=True;break
   a*=.5
  rec={'step':k,'depth':P[0][0],'LP_derivative':float(J[0]@p),'fraction':a,'accepted':accepted,'min_P_guard':float(pg[pi].min()),'min_Q_guard':float(qg[qi].min()),'t_range':[float(t.min()),float(t.max())],'status':'accepted' if accepted else 'finite_policy_stall'}
  history.append(rec);print(json.dumps(rec),flush=True)
  if not accepted:break
  t=tt;best=t.copy()
 result={'R':R.tolist(),'t':t.tolist(),'points':(R/t[:,None]).tolist(),'history':history,'census':numeric_census(R/t[:,None]),'parent_raw_centroid':rawg.tolist(),'bar':topology(R,t)[6]}
 Path('RAYFLOW139.json').write_text(json.dumps(result,indent=2)+'\n');print('FINAL',result['bar'],result['census'],flush=True)
if __name__=='__main__':run(int(sys.argv[1]) if len(sys.argv)>1 else 80,float(sys.argv[2]) if len(sys.argv)>2 else .03)
```

### File: pointcone139.py
```python
"""Finite numerical centering inside a root-changing physical-arrow cone.
All trial moments use the rebuilt actual hull; failures are not exclusions.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,sys
from pathlib import Path
from scipy.optimize import minimize,LinearConstraint,Bounds
from radial139 import load_rays,actual,numeric_census

def run(r,power,maxiter=800):
 R,w,f,g0=load_rays();G=R@R.T;n=len(R);p=np.zeros(n);p[r]=1;par=np.full(n,-1);todo=set(range(n))
 while todo:
  j=max(todo,key=lambda i:(p[i]*p[i]*G[i,i],-i));todo.remove(j)
  for i in sorted(todo):
   c=max(0,G[i,j]/G[i,i])*p[j]
   if c>p[i]:p[i]=c;par[i]=j
 pi=p*np.sqrt(np.diag(G)/G[r,r]);s=p*pi**power;t0=1/s
 A=np.zeros((n-1,n));k=0
 for i in range(n):
  if i==r:continue
  j=par[i];A[k,i]=G[i,j]/G[i,i]*t0[i];A[k,j]=-t0[j];A[k]/=max(abs(A[k]).max(),1e-30);k+=1
 # Independent constant strict margin, not a decaying min(current,floor).
 eps=1e-7;cons=LinearConstraint(A,np.full(n-1,eps),np.full(n-1,np.inf));calls=0;hist=[];best=None
 def obj(u):
  nonlocal calls,best
  t=u*t0;f,V,g,X,h=actual(R,t);tri=f.tri;vv=f.a/np.prod(t[tri],axis=1);sumx=X[tri].sum(axis=1);Mf=vv[:,None]*sumx/4
  Mjac=np.zeros((3,n));Vjac=np.zeros(n)
  for k in range(3):
   ids=tri[:,k];np.add.at(Vjac,ids,-vv/t[ids])
   for d in range(3):np.add.at(Mjac[d],ids,-(Mf[:,d]+vv*X[ids,d]/4)/t[ids])
  gjac=(Mjac-g[:,None]*Vjac[None,:])/V
  value=float(g@g/V**(2/3));grad=(2*g@gjac/V**(2/3)-(2/3)*value*Vjac/V)*t0
  calls+=1;slack=float(np.min(A@u-eps))
  if slack>=-1e-12 and (best is None or value<best['value']):best={'value':value,'u':u.tolist(),'t':t.tolist(),'g':g.tolist(),'V':V,'points':X.tolist(),'slack':slack,'calls':calls};hist.append({k:v for k,v in best.items() if k not in ('u','t','points')})
  return value,grad
 sol=minimize(obj,np.ones(n),jac=True,method='SLSQP',bounds=Bounds(np.full(n,.03),np.full(n,30)),constraints=[cons],options={'maxiter':maxiter,'ftol':1e-20,'disp':False})
 if best is not None:best['census']=numeric_census(np.array(best['points']));best['reference_min_arrow']=float(np.min(A@np.array(best['u'])))
 out={'root':r,'power':power,'eps':eps,'bounds':[.03,30],'maxiter':maxiter,'status':int(sol.status),'message':sol.message,'iterations':sol.nit,'calls':calls,'best':best,'history':hist,'parent':par.tolist(),'t0':t0.tolist()}
 name='POINTCONE139_r'+str(r)+'_p'+str(power)+'.json';Path(name).write_text(json.dumps(out,indent=2)+'\n');print(name,sol.status,sol.message,'gNormNormalized',best['value']**.5,'own_census',best['census'],flush=True)
 return out
if __name__=='__main__':run(int(sys.argv[1]),float(sys.argv[2]),int(sys.argv[3]) if len(sys.argv)>3 else 800)
```

### File: pointcone_added139.py
```python
"""Finite numerical centering inside a root-changing physical-arrow cone.
All trial moments use the rebuilt actual hull; failures are not exclusions.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,sys
from pathlib import Path
from scipy.optimize import minimize,LinearConstraint,Bounds
from radial139 import load_rays,actual,numeric_census

def run(r,power,maxiter=800):
 R,w,f,g0=load_rays();R=np.vstack([R,[-.639,.068,-.766]]);G=R@R.T;n=len(R);p=np.zeros(n);p[r]=1;par=np.full(n,-1);todo=set(range(n))
 while todo:
  j=max(todo,key=lambda i:(p[i]*p[i]*G[i,i],-i));todo.remove(j)
  for i in sorted(todo):
   c=max(0,G[i,j]/G[i,i])*p[j]
   if c>p[i]:p[i]=c;par[i]=j
 depth=np.zeros(n,dtype=int)
 for i in range(n):
  j=i
  while j!=r:depth[i]+=1;j=par[j]
 s=p*power**depth;t0=1/s
 A=np.zeros((n-1,n));k=0
 for i in range(n):
  if i==r:continue
  j=par[i];A[k,i]=G[i,j]/G[i,i]*t0[i];A[k,j]=-t0[j];A[k]/=max(abs(A[k]).max(),1e-30);k+=1
 # Independent constant strict margin, not a decaying min(current,floor).
 eps=1e-7;cons=LinearConstraint(A,np.full(n-1,eps),np.full(n-1,np.inf));calls=0;hist=[];best=None
 def obj(u):
  nonlocal calls,best
  t=u*t0;f,V,g,X,h=actual(R,t);tri=f.tri;vv=f.a/np.prod(t[tri],axis=1);sumx=X[tri].sum(axis=1);Mf=vv[:,None]*sumx/4
  Mjac=np.zeros((3,n));Vjac=np.zeros(n)
  for k in range(3):
   ids=tri[:,k];np.add.at(Vjac,ids,-vv/t[ids])
   for d in range(3):np.add.at(Mjac[d],ids,-(Mf[:,d]+vv*X[ids,d]/4)/t[ids])
  gjac=(Mjac-g[:,None]*Vjac[None,:])/V
  value=float(g@g/V**(2/3));grad=(2*g@gjac/V**(2/3)-(2/3)*value*Vjac/V)*t0
  calls+=1;slack=float(np.min(A@u-eps))
  if slack>=-1e-12 and (best is None or value<best['value']):best={'value':value,'u':u.tolist(),'t':t.tolist(),'g':g.tolist(),'V':V,'points':X.tolist(),'slack':slack,'calls':calls};hist.append({k:v for k,v in best.items() if k not in ('u','t','points')})
  return value,grad
 lower=np.full(n,.03);upper=np.full(n,30);lower[r]=upper[r]=1
 sol=minimize(obj,np.ones(n),jac=True,method='SLSQP',bounds=Bounds(lower,upper),constraints=[cons],options={'maxiter':maxiter,'ftol':1e-20,'disp':False})
 if best is not None:best['census']=numeric_census(np.array(best['points']));best['reference_min_arrow']=float(np.min(A@np.array(best['u'])))
 out={'root':r,'power':power,'eps':eps,'bounds':[.03,30],'root_scale_fixed':True,'new_ray':[-.639,.068,-.766],'parameter_is_per_edge_attenuation':True,'maxiter':maxiter,'status':int(sol.status),'message':sol.message,'iterations':sol.nit,'calls':calls,'best':best,'history':hist,'parent':par.tolist(),'t0':t0.tolist()}
 name='POINTCONE_ADDED139_r'+str(r)+'_p'+str(power)+'.json';Path(name).write_text(json.dumps(out,indent=2)+'\n');print(name,sol.status,sol.message,'gNormNormalized',best['value']**.5,'own_census',best['census'],flush=True)
 return out
if __name__=='__main__':run(int(sys.argv[1]),float(sys.argv[2]),int(sys.argv[3]) if len(sys.argv)>3 else 800)
```

### File: envelope139_scout.py
```python
"""Finite-ray all-root path envelope and centroid-reflection scout, not a proof."""
from radial139 import *
R,w,f,g=load_rays();n=len(R);G=R@R.T;C=np.maximum(0,G/np.diag(G)[:,None]);np.fill_diagonal(C,0)
p=np.eye(n)
for k in range(n-1):p=np.maximum(p,np.max(C[:,:,None]*p[None,:,:],axis=1))
rows=[]
for r in range(n):
 if np.min(p[:,r])==0:rows.append({'root':r,'disconnected':True});continue
 X=R*p[:,r,None];h=ConvexHull(X);v=-R[r]/3;sl=h.equations[:,:3]@v+h.equations[:,3];j=int(sl.argmax())
 rows.append({'root':r,'gap':float(sl[j]),'relative_gap':float(sl[j]/np.linalg.norm(R[r])),'outside':bool(sl[j]>0),'facet':list(map(int,h.simplices[j])),'envelopeV':len(h.vertices),'min_scale':float(p[:,r].min()),'max_scale':float(p[:,r].max())})
print(json.dumps(rows,indent=2));print('OUTSIDE',sum(r.get('outside',r.get('disconnected',False)) for r in rows),'of',n)
Path('ENVELOPE139_SCOUT.json').write_text(json.dumps({'rows':rows,'p':p.tolist()},indent=2)+'\n')
```

### File: reflect139_scout.py
```python
"""Finite numerical nominations only: radial path and centroid-reflection bounds."""
import json,numpy as np
from scipy.spatial import ConvexHull
from pathlib import Path
from radial139 import load_rays
R,w,X0,center0=load_rays();G=R@R.T;C=np.maximum(0,G/np.diag(G)[:,None]);np.fill_diagonal(C,0)
a=json.loads(Path('ENVELOPE139_SCOUT.json').read_text());P=np.array(a['p']);reports=[]
for r in range(len(R)):
 b=P[:,r].copy();history=[];reason=None
 for k in range(150):
  H=ConvexHull(b[:,None]*R);N=H.equations[:,:3];h=-H.equations[:,3]
  NR=-(N@R.T);bounds=np.where(NR>1e-13,3*h[:,None]/np.maximum(NR,1e-300),np.inf)
  face=bounds.argmin(axis=0);cap=bounds[face,np.arange(len(R))]
  fresh=np.minimum(b,cap);fresh[np.arange(len(R))!=r]=np.minimum(fresh[np.arange(len(R))!=r],(C@np.zeros(len(R))+np.max(C*b[None,:],axis=1))[np.arange(len(R))!=r])
  if fresh[r]<1-1e-10:
   reason='root_reflection_excluded';history.append({'step':k,'root_cap':float(fresh[r]),'facet':H.simplices[face[r]].tolist()});break
  # Root is known to have scale exactly one.
  fresh[r]=1
  ratio=np.max((b-fresh)/np.maximum(b,1e-100));history.append({'step':k,'relative_shrink':float(ratio),'min_bound':float(fresh.min())})
  b=fresh
  if ratio<1e-9:reason='fixed_point';break
 reports.append({'root':r,'reason':reason or 'iteration_limit','steps':k+1,'root_bound':float(fresh[r]),'last_bounds':b.tolist(),'history':history})
 print(r,reason,k+1,float(fresh[r]),float(b.min()),flush=True)
Path('REFLECT139_SCOUT.json').write_text(json.dumps(reports,indent=2)+'\n')
```

### File: rayinsert139.py
```python
"""Numerical all-path envelope ray-insertion scout; NOT a body construction."""
import numpy as np,json
from pathlib import Path
from scipy.spatial import ConvexHull
from radial139 import load_rays
R,*_=load_rays();U=R/np.linalg.norm(R,axis=1)[:,None];r=0

def bound(U):
 C=np.maximum(0,U@U.T);np.fill_diagonal(C,0);p=np.zeros(len(U));p[r]=1;todo=set(range(len(U)))
 while todo:
  j=max(todo,key=lambda i:(p[i],-i));todo.remove(j)
  for i in todo:p[i]=max(p[i],C[i,j]*p[j])
 H=ConvexHull(p[:,None]*U);v=-U[r]/3;gaps=H.equations[:,:3]@v+H.equations[:,3]
 return float(gaps.max()),p,H
base,*_=bound(U);best=None;rows=[]
for i in range(len(U)):
 for j in range(i+1,len(U)):
  if U[i]@U[j]<=0:continue
  z=U[i]+U[j];z/=np.linalg.norm(z);g,p,h=bound(np.vstack([U,z]));row={'pair':[i,j],'direction':z.tolist(),'gap':g};rows.append(row)
  if best is None or g<best['gap']:best=row
out={'base_normalized_gap':base,'best':best,'all_pair_count':len(rows),'strict_pass_count':sum(q['gap']<0 for q in rows),'top20':sorted(rows,key=lambda x:x['gap'])[:20]};Path('RAYINSERT139_SCOUT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)
```
