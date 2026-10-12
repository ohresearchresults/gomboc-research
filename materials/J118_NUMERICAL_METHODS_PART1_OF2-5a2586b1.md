# material-5a2586b189bc

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# J118 numerical methods — complete source part 1 of 2

This part preserves all four complete common/normal-continuation source units, including failed policies. Part2 supplies finite-cut/retirement producers. Depend on the complete geometry115.py in [internal-source-reference] (4471B,SHA604a9d9e7dbb3703d3770e259f13b900ba467431fb0c15cc1acfce3d372de2c4) and the literal J117_SCALED12_G14.txt in [internal-source-reference] (3299B,SHA55eb2db715dedc6459eef2fe9baf22d0c7a2a40f039d2374bd937a2e28d8f0aa). Do not replace it with another J117 body. The new rational C408 recovery is separately in [internal-source-reference] plus its exact115 dependency. Numerical methods require Python3.13.5,NumPy2.3.5,SciPy1.17.0,Torch2.10.0+cpu in the executed environment; set OMP_NUM_THREADS=1 and OPENBLAS_NUM_THREADS=1. No random seed or omitted optimizer setting is used.

## Scientific limits and completed execution
`python bottleneck118.py J117_SCALED12_G14.txt BOTTLENECK118_FREE.json 60 .02 free` evaluated32 finite proposals and accepted0. The widest directed-chord bottleneck rho starts-.05274251657925919; old sigma~9.94379e-13. The debug program evaluated4 radii times7 alphas: LP prediction is feasible but finite actual mass produces polar births, e.g radius.02/full step rho-.03548142746,sigma-.00278654504,actualS50/U17. This is a failure of first-order guard protection, not a family exclusion.
`python correct118.py J117_SCALED12_G14.txt CORRECT118_BOT.json 5 .04 1e-5` completed5 accepted steps. Q-only repair preservesS1 but creates many U; endpointF68/E198,rho-.04493147023760441,19P,totalP.37142790610662424,Q[]. `python correct118.py CORRECT118_BOT.json CORRECT118_BOT2.json 30 .08 1e-5` completed4 accepted steps then no admissible next step; rho-.04037467672846825,19P,totalP.38448568509401754,Q[],F68/E198. These are proxy improvements with WORSE whole P, not own121 or progress to110.
`python class118.py J117_SCALED12_G14.txt CLASS118.json 4 .01 1e-5` was execution-timeout interrupted AFTER initial actual-class repair and one fully saved accepted step. Only that prefix is claimed: repair3iterations/4calls yieldsS1/U2,P.3302868150980584; rejected targets.3202868/.3262868/.3286868; acceptedtarget.32964681509805843 in5iterations/6calls,P.3296468150980579. The interrupted second iteration has no preserved completion claim.
`python class118.py CLASS118.json CLASS118_SMALL.json 12 .0006 1e-5` completedone accepted step toP.3294068150980576,F69/E201,then no step. Several large-target SLSQP failures left the local virtual-triple chamber; they are not infeasibility proofs. The full floating checkpoints are preserved separately for continuing exact completed prefixes.

No `clean` call is an exact certificate. It is a floating admission filter; every frozen body's exact P/Q and direct census must be obtained using exact115 without a floor. All accepted endpoints rebuild actual maximal geometry, true edges and uniform mass. Virtual old intersections guide local repair only and can fail when the actual fan changes.

## bottleneck118.py — 5565B, SHA7f79c218e1e92dc30c5058d3fee7e269f3116b1a856f3da469abf5676d7fce43
```python
"""Actual-mass widest-chord continuation. Numerical candidates, not certificates.
The globally optimized bottleneck over rooted arborescences sees an entire
basin, rather than only the current birth vertex or the displayed saddle.
All normal coordinates move, and actual mass/fan are rebuilt at every trial.
"""
import os
os.environ.setdefault('OMP_NUM_THREADS','1');os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import json,sys,time
from pathlib import Path
import numpy as np,torch
from scipy.optimize import linprog
from geometry115 import geometry,read_h,bars
torch.set_num_threads(1);torch.set_default_dtype(torch.float64)

def tree(x,root=None):
    sq=np.einsum('ij,ij->i',x,x)
    weights=(x@x.T-sq[:,None])/sq[:,None]
    np.fill_diagonal(weights,-np.inf)
    if root is None:root=int(np.argmax(sq))
    cap=np.full(len(x),-np.inf);cap[root]=np.inf
    parent=np.full(len(x),-1,int);done=np.zeros(len(x),bool)
    for _ in range(len(x)):
        i=int(np.argmax(np.where(done,-np.inf,cap)));done[i]=True
        cand=np.minimum(weights[:,i],cap[i]); take=(cand>cap)&~done
        cap[take]=cand[take];parent[take]=i
    ids=np.array([i for i in range(len(x)) if i!=root],int)
    v=weights[ids,parent[ids]]
    return root,ids,parent[ids],v

def report(n):
    m=geometry(n);t=tree(m['p']);qt=tree(m['q'][m['active']])
    # Re-index polar parents into full submitted support indices.
    qt=(int(m['active'][qt[0]]),m['active'][qt[1]],m['active'][qt[2]],qt[3])
    P=bars(m['p'],m['edges']);Q=bars(m['q'],m['dual_edges'])
    def strict_roots(x):
        w=x@x.T-np.einsum('ij,ij->i',x,x)[:,None];np.fill_diagonal(w,-np.inf)
        return np.where(np.max(w,axis=1)<0)[0].tolist()
    return m,t,qt,dict(V=len(m['p']),E=len(m['edges']),F=len(m['faces']),volume=m['volume'],g=m['g'].tolist(),
        P=P,Q=Q,U=strict_roots(m['p']),S=strict_roots(m['q'][m['active']]),rho=float(min(t[3])),sigma=float(min(qt[3])))

def tensors(flat,m):
    nt=flat.reshape(m['n'].shape)
    vv=torch.linalg.solve(nt[m['triples']],torch.ones((len(m['triples']),3,1))).squeeze(-1)
    tet=vv[m['tetrahedra']];vol=torch.linalg.det(tet)/6
    g=(vol[:,None]*tet.sum(dim=1)/4).sum(dim=0)/vol.sum()
    return vv-g,nt/(1-nt@g)[:,None],vol.sum()

def read_source(path):
    return np.asarray(json.loads(Path(path).read_text())['normals']) if str(path).endswith('.json') else read_h(path)

def run(source,out,steps=100,radius=.02,policy='free'):
    n=read_source(source);trace=[];start=time.time();evaluated=[]
    for it in range(steps):
        m,t,qt,c=report(n)
        if c['rho']>1e-8 and c['sigma']>1e-8:
            print('NUMERICAL_POSITIVE_TREES_REQUIRE_EXACT_AUDIT',c,flush=True);break
        def f(z):
            p,q,v=tensors(z,m)
            vp=(p[t[1]]*(p[t[2]]-p[t[1]])).sum(dim=1)/(p[t[1]]**2).sum(dim=1)
            vq=(q[qt[1]]*(q[qt[2]]-q[qt[1]])).sum(dim=1)/(q[qt[1]]**2).sum(dim=1)
            return torch.cat((vp,vq,torch.log(v).reshape(1)))
        x=torch.tensor(n.ravel());v=f(x).detach().numpy();J=torch.func.jacrev(f)(x).detach().numpy()
        k=len(t[1]);scale=np.repeat(np.linalg.norm(n,axis=1),3);D=J*scale
        found=False
        # LP maximizes the entire tree bottleneck, while protecting sole S.
        for r in [radius,radius*.4,radius*.16,radius*.064]:
            A=np.c_[-D[:-1],np.r_[np.ones(k),np.zeros(len(qt[1]))]]
            qtarget=np.minimum(np.maximum(v[k:-1]*.3,1e-12),1e-7)
            b=v[:-1]-np.r_[np.zeros(k),qtarget]
            if policy=='keepP':
                keep=np.where(v[:k]>0)[0]
                A=np.r_[A,np.c_[-D[keep],np.zeros(len(keep))]]
                b=np.r_[b,v[keep]-np.minimum(v[keep]*.3,1e-8)]
            opt=linprog(np.r_[np.zeros(n.size),-1.],A_ub=A,b_ub=b,
                A_eq=np.c_[D[-1:,:],np.zeros((1,1))],b_eq=[0.],
                bounds=[(-r,r)]*n.size+[(-1.,.01)],method='highs')
            if not opt.success:continue
            d=(opt.x[:-1]*scale).reshape(n.shape)
            for alpha in [1,.5,.25,.125,.0625,.03125,.015625,.0078125]:
                z=n+alpha*d
                try:_,_,_,cc=report(z)
                except (ValueError,AssertionError):continue
                evaluated.append(dict(it=it,r=r,alpha=alpha,rho=cc['rho'],sigma=cc['sigma'],P=sum(x[0] for x in cc['P']),Q=sum(x[0] for x in cc['Q']),E=cc['E']))
                if cc['E']<=249 and cc['sigma']>1e-12 and cc['rho']>c['rho']+max(1e-13,abs(c['rho'])*1e-7):
                    n=z;found=True
                    trace.append(dict(it=it,r=r,alpha=alpha,predicted_rho=opt.x[-1],**cc))
                    Path(out).write_text(json.dumps(dict(normals=n.tolist(),trace=trace,source=Path(source).name,
                        params=dict(steps=steps,radius=radius,policy=policy),evaluated=evaluated),indent=2)+'\n')
                    print('ACCEPT',it,cc['rho'],cc['sigma'],len(cc['U']),len(cc['S']),sum(x[0] for x in cc['P']),cc['E'],flush=True)
                    break
            if found:break
        if not found:print('NO_STEP',it,c,flush=True);break
    Path(str(out)+'.scan.json').write_text(json.dumps(evaluated,indent=2)+'\n')
    print('DONE',len(trace),time.time()-start,report(n)[3],flush=True)
    if not Path(out).exists():Path(out).write_text(json.dumps(dict(normals=n.tolist(),trace=trace,source=Path(source).name,params=dict(steps=steps,radius=radius,policy=policy)),indent=2)+'\n')

if __name__=='__main__':
    run(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 100,float(sys.argv[4]) if len(sys.argv)>4 else .02,sys.argv[5] if len(sys.argv)>5 else 'free')
```

## debug118.py — 1206B, SHA3289e1e9e680d25c786477b48b876c973047ed9fa9f5b295abc03cae24d5df3c
```python
import numpy as np,torch
from bottleneck118 import *
n=read_h('J117_SCALED12_G14.txt');m,t,qt,c=report(n)
def f(z):
 p,q,v=tensors(z,m)
 return torch.cat(((p[t[1]]*(p[t[2]]-p[t[1]])).sum(1)/(p[t[1]]**2).sum(1),(q[qt[1]]*(q[qt[2]]-q[qt[1]])).sum(1)/(q[qt[1]]**2).sum(1),torch.log(v).reshape(1)))
x=torch.tensor(n.ravel());v=f(x).detach().numpy();J=torch.func.jacrev(f)(x).detach().numpy();k=len(t[1]);scale=np.repeat(np.linalg.norm(n,axis=1),3);D=J*scale
for r in [.02,.008,.0032,.00128]:
 A=np.c_[-D[:-1],np.r_[np.ones(k),np.zeros(len(qt[1]))]];target=np.minimum(np.maximum(v[k:-1]*.3,1e-12),1e-7)
 b=v[:-1]-np.r_[np.zeros(k),target]
 opt=linprog(np.r_[np.zeros(n.size),-1.],A_ub=A,b_ub=b,A_eq=np.c_[D[-1:,:],np.zeros((1,1))],b_eq=[0.],bounds=[(-r,r)]*n.size+[(-1.,.01)],method='highs')
 print('LP',r,opt.message, 'objective',opt.fun)
 if not opt.success:continue
 d=(opt.x[:-1]*scale).reshape(n.shape)
 for alpha in [1,.5,.1,.01,.001,1e-4,1e-5]:
  try:mm,tt,qq,cc=report(n+alpha*d);print(alpha,cc['rho'],cc['sigma'],len(cc['U']),len(cc['S']),max([x[0] for x in cc['P']],default=0))
  except Exception as e:print(alpha,type(e).__name__,str(e))
print('vgrad',np.min(v),np.max(abs(J)),np.linalg.norm(J[-1]))
```

## correct118.py — 4408B, SHA7581059b4246f0c571cd22ad337d4d6be49e90ba3a08f772543da41dc492bfca
```python
"""Finite actual-centroid polar-forest correction, not reference-centre fitting.
Complete numerical method; depends on bottleneck118.py and geometry115.py.
"""
import json,sys,time
from pathlib import Path
import numpy as np,torch
from scipy.optimize import minimize,linprog
from bottleneck118 import read_source,report,tensors,tree

class Corrector:
 def __init__(self,n,ids,parents,target=1e-5,bound=.2):
  self.base=n.copy();self.scale=np.linalg.norm(n,axis=1)[:,None];self.ids=ids;self.parents=parents
  self.target=target;self.bound=bound;self.cache=None;self.calls=0;self.invalid=0
 def compute(self,z):
  if self.cache is not None and np.array_equal(z,self.cache[0]):return self.cache[1:]
  n=self.base+z.reshape(self.base.shape)*self.scale
  try:m,_,_,_=report(n)
  except (ValueError,AssertionError):
   self.invalid+=1
   return np.full(len(self.ids),-1e3),np.zeros((len(self.ids),len(z)))
  def fun(x):
   nt=torch.as_tensor(self.base)+x.reshape(self.base.shape)*torch.as_tensor(self.scale)
   _,q,_=tensors(nt.ravel(),m)
   a=q[self.ids];b=q[self.parents]
   return (a*(b-a)).sum(1)/(a*a).sum(1)-self.target
  x=torch.tensor(z);v=fun(x).detach().numpy();J=torch.func.jacrev(fun)(x).detach().numpy()
  self.calls+=1;self.cache=(z.copy(),v,J)
  return v,J
 def run(self,limit=100):
  z=np.zeros(self.base.size)
  result=minimize(lambda z:(.5*float(z@z),z),z,jac=True,method='SLSQP',
   constraints=[dict(type='ineq',fun=lambda z:self.compute(z)[0],jac=lambda z:self.compute(z)[1])],
   bounds=[(-self.bound,self.bound)]*len(z),options=dict(ftol=1e-13,maxiter=limit,disp=False))
  n=self.base+result.x.reshape(self.base.shape)*self.scale
  _,_,_,c=report(n)
  return n,dict(status=int(result.status),message=result.message,iterations=int(result.nit),calls=self.calls,invalid=self.invalid,min_constraint=float(min(self.compute(result.x)[0])),norm=float(np.linalg.norm(result.x)),census=c)

def run(source,out,steps=30,radius=.04,margin=1e-5):
 n=read_source(source);trace=[];scans=[];m,t,qt,c=report(n)
 init=Corrector(n,qt[1],qt[2],target=margin,bound=.25)
 n,receipt=init.run(160);trace.append(dict(kind='initial_repair',repair=receipt))
 print('REPAIR',receipt,flush=True)
 for it in range(steps):
  m,t,qt,c=report(n)
  if c['rho']>1e-8 and c['sigma']>1e-8:
   print('NUMERIC_POSITIVE_TREES_REQUIRES_EXACT',c,flush=True);break
  def f(z):
   p,q,v=tensors(z,m)
   vp=(p[t[1]]*(p[t[2]]-p[t[1]])).sum(1)/(p[t[1]]**2).sum(1)
   vq=(q[qt[1]]*(q[qt[2]]-q[qt[1]])).sum(1)/(q[qt[1]]**2).sum(1)
   return torch.cat((vp,vq,torch.log(v).reshape(1)))
  x=torch.tensor(n.ravel());v=f(x).detach().numpy();J=torch.func.jacrev(f)(x).detach().numpy();k=len(t[1]);scale=np.repeat(np.linalg.norm(n,axis=1),3);D=J*scale
  found=False
  for r in [radius,radius*.4,radius*.16]:
   A=np.c_[-D[:-1],np.r_[np.ones(k),np.zeros(len(qt[1]))]]
   b=v[:-1]-np.r_[np.zeros(k),np.minimum(v[k:-1]*.5,margin)]
   opt=linprog(np.r_[np.zeros(n.size),-1.],A_ub=A,b_ub=b,A_eq=np.c_[D[-1:,:],np.zeros((1,1))],b_eq=[0.],bounds=[(-r,r)]*n.size+[(-1.,.01)],method='highs')
   if not opt.success:continue
   d=(opt.x[:-1]*scale).reshape(n.shape)
   for alpha in [1.,.5,.25]:
    z=n+alpha*d
    try:
     corr=Corrector(z,qt[1],qt[2],target=margin,bound=max(.015,2*r))
     z,rr=corr.run(100);_,_,_,cc=report(z)
    except (ValueError,AssertionError):continue
    rec=dict(it=it,r=r,alpha=alpha,predicted_rho=float(opt.x[-1]),repair=rr)
    scans.append(rec)
    if cc['E']<=249 and cc['sigma']>margin*.9 and cc['rho']>c['rho']+max(1e-10,abs(c['rho'])*1e-5):
     n=z;found=True;trace.append(rec)
     Path(out).write_text(json.dumps(dict(normals=n.tolist(),trace=trace,scans=scans,params=dict(steps=steps,radius=radius,margin=margin),source=Path(source).name),indent=2)+'\n')
     print('ACCEPT',it,'rho',cc['rho'],'P',sum(a[0] for a in cc['P']),'Pcount',len(cc['P']),'Q',len(cc['Q']),'EF',cc['E'],cc['F'],'repair',rr['iterations'],flush=True)
     break
   if found:break
  if not found:print('NO_ACCEPT',it,c,flush=True);break
 Path(out).write_text(json.dumps(dict(normals=n.tolist(),trace=trace,scans=scans,params=dict(steps=steps,radius=radius,margin=margin),source=Path(source).name),indent=2)+'\n')
 print('DONE',report(n)[3],flush=True)

if __name__=='__main__':run(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 30,float(sys.argv[4]) if len(sys.argv)>4 else .04,float(sys.argv[5]) if len(sys.argv)>5 else 1e-5)
```

## class118.py — 5405B, SHAf5a7f3aa0a218477bfcd5b62d91e9abf108359b3a210527b448fb7d1ca73320d
```python
"""Moving-fan, actual-mass two-root class repair and P-level continuation.
Virtual old triple intersections guide local guards, but every accepted step
is rebuilt and judged using the actual body; virtual-point success is NOT
an equilibrium certificate. No discarded positive bar is accepted as exact.
"""
import os
os.environ.setdefault('OMP_NUM_THREADS','1');os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import json,sys
from pathlib import Path
import numpy as np,torch
from scipy.optimize import minimize
from bottleneck118 import read_source,report,tree,tensors

def angular_policy(x,excluded):
 d=x[None,:,:]-x[:,None,:]
 den=np.sqrt(np.sum(x*x,axis=1)[:,None]*np.sum(d*d,axis=2)+1e-30)
 w=np.einsum('ik,ijk->ij',x,d)/den;np.fill_diagonal(w,-np.inf)
 ids=np.array([i for i in range(len(x)) if i not in excluded],int)
 return ids,np.argmax(w[ids],axis=1)

class ClassRepair:
 def __init__(self,n,margin=1e-5,bound=.1,Ptarget=None):
  self.base=n.copy();self.scale=np.linalg.norm(n,axis=1)[:,None];self.margin=margin;self.bound=bound;self.Ptarget=Ptarget
  self.m,self.t,self.qt,self.c=report(n);p=self.m['p'];q=self.m['q']
  birth=self.c['P'][0][1] if self.c['P'] else self.t[0]
  self.pi,self.pj=angular_policy(p,[self.t[0],birth]);self.qi,self.qj=angular_policy(q,[self.qt[0]])
  self.birth=birth;self.saddle=self.c['P'][0][2] if self.c['P'] else [0,1]
  self.cache=None;self.calls=0;self.invalid=0
 def compute(self,z):
  if self.cache is not None and np.array_equal(z,self.cache[0]):return self.cache[1:]
  n=self.base+z.reshape(self.base.shape)*self.scale
  from geometry115 import geometry
  count=len(self.pi)+len(self.qi)+(self.Ptarget is not None)
  try:live=geometry(n)
  except (ValueError,AssertionError):
   self.invalid+=1;return np.full(count,-100.),np.zeros((count,len(z)))
  def fun(x):
   nt=torch.as_tensor(self.base)+x.reshape(self.base.shape)*torch.as_tensor(self.scale)
   # Geometry of the current actual fan controls the uniform centroid.
   vp=torch.linalg.solve(nt[live['triples']],torch.ones((len(live['triples']),3,1))).squeeze(-1)
   tet=vp[live['tetrahedra']];vol=torch.linalg.det(tet)/6
   g=(vol[:,None]*tet.sum(1)/4).sum(0)/vol.sum()
   vv=torch.linalg.solve(nt[self.m['triples']],torch.ones((len(self.m['triples']),3,1))).squeeze(-1)
   p=vv-g;q=nt/(1-nt@g)[:,None]
   def score(x,i,j):
    a=x[i];d=x[j]-a
    return (a*d).sum(1)/torch.sqrt((a*a).sum(1)*(d*d).sum(1)+1e-30)-self.margin
   val=torch.cat((score(p,self.pi,self.pj),score(q,self.qi,self.qj)))
   if self.Ptarget is not None:
    a,b=p[self.saddle];d=b-a;t=torch.clamp(-(a@d)/(d@d),0,1);foot=a+t*d
    depth=1-(foot@foot)/(p[self.birth]@p[self.birth])
    val=torch.cat((val,(self.Ptarget-depth).reshape(1)))
   return val
  x=torch.tensor(z);v=fun(x).detach().numpy();J=torch.func.jacrev(fun)(x).detach().numpy();self.calls+=1
  self.cache=(z.copy(),v,J);return v,J
 def run(self,limit=100):
  z=np.zeros(self.base.size)
  result=minimize(lambda z:(.5*float(z@z),z),z,jac=True,method='SLSQP',
   constraints=[dict(type='ineq',fun=lambda z:self.compute(z)[0],jac=lambda z:self.compute(z)[1])],
   bounds=[(-self.bound,self.bound)]*len(z),options=dict(ftol=1e-13,maxiter=limit,disp=False))
  n=self.base+result.x.reshape(self.base.shape)*self.scale
  _,_,_,c=report(n)
  return n,dict(status=int(result.status),message=result.message,iterations=int(result.nit),calls=self.calls,invalid=self.invalid,min_constraint=float(min(self.compute(result.x)[0])),norm=float(np.linalg.norm(result.x)),census=c)

def clean(c):
 # This is a numerical admission condition; exact absence still needs audit.
 return len(c['U'])<=2 and len(c['S'])==1 and len([z for z in c['P'] if z[0]>1e-14])<=1 and c['sigma']>1e-10

def run(source,out,steps=10,drop=.01,margin=1e-5):
 n=read_source(source);trace=[];scans=[]
 n0=n.copy()
 for repairround in range(4):
  n,rr=ClassRepair(n,margin=margin,bound=.15).run(100);scans.append(dict(stage='repair',receipt=rr))
  print('REPAIR',repairround,rr,flush=True)
  if clean(rr['census']):break
 if not clean(rr['census']):
  Path(out).write_text(json.dumps(dict(normals=n.tolist(),trace=trace,scans=scans,source=Path(source).name,params=dict(steps=steps,drop=drop,margin=margin)),indent=2)+'\n');print('FAILED_INITIAL_REPAIR');return
 for it in range(steps):
  c=report(n)[3];old=sum(z[0] for z in c['P']);found=False
  for amount in [drop,drop*.4,drop*.16,drop*.064]:
   target=max(0,old-amount)
   z,rr=ClassRepair(n,margin=margin,bound=.2,Ptarget=target).run(100)
   cc=report(z)[3];scans.append(dict(stage='flow',it=it,target=target,receipt=rr))
   if clean(cc) and sum(v[0] for v in cc['P'])<old-1e-7:
    n=z;trace.append(dict(it=it,target=target,receipt=rr));found=True
    Path(out).write_text(json.dumps(dict(normals=n.tolist(),trace=trace,scans=scans,source=Path(source).name,params=dict(steps=steps,drop=drop,margin=margin)),indent=2)+'\n')
    print('ACCEPT',it,cc['P'],cc['E'],cc['F'],rr['norm'],flush=True);break
  if not found:print('NO_STEP',it,flush=True);break
 Path(out).write_text(json.dumps(dict(normals=n.tolist(),trace=trace,scans=scans,source=Path(source).name,params=dict(steps=steps,drop=drop,margin=margin)),indent=2)+'\n')
 print('DONE',report(n)[3],flush=True)
if __name__=='__main__':run(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 10,float(sys.argv[4]) if len(sys.argv)>4 else .01,float(sys.argv[5]) if len(sys.argv)>5 else 1e-5)
```
