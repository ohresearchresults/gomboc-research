# material-852bc0b1061d

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Complete C508/C426 radial-persistence search source

Numerical search method, not an exclusion theorem. Exact C426 endpoints are separately recovered by [internal-source-reference] (RECOVER_FULL92_C426.py), dependent on RECOVER_C508.py from [internal-source-reference], SHA256 12c3e1fa064498a760c0c7eb5ef0d79d00276584b0053dab531b7c6cc5cb3838. Both complete source files below must be placed beside RECOVER_C508.py. Environment: Python3.13.5, NumPy2.3.5, SciPy1.17.0. BLAS thread count1 is set before NumPy import. Deterministic optimizer checkpoint replay may depend on environment; exact endpoint reconstruction does not need the optimizer.

The source carries exact original input through RECOVER_C508.py, which embeds the original G6 points and original C508 G12 normal checkpoint. No missing random seed affects the production search. Derivative check uses seed190930.

Commands actually used in this finite scout:

    python chain_persistence.py --check
    python chain_persistence.py --steps 700 --out CHAIN_PERSISTENCE_700
    python chain_persistence.py --steps 700 --out CHAIN_FREEVOL_700 --free-volume
    python full_active_persistence.py --steps 1000 --out FULL92_B02
    python full_active_persistence.py --steps 1000 --source FULL92_B02_BEST.json --out FULL92_CYCLE2
    python full_active_persistence.py --steps 1000 --source FULL92_CYCLE2_BEST.json --out FULL92_CYCLE3
    python full_active_persistence.py --steps 1000 --source FULL92_CYCLE3_BEST.json --out FULL92_CYCLE4
    python full_active_persistence.py --steps 1000 --source FULL92_CYCLE4_BEST.json --out FULL92_CYCLE5
    python full_active_persistence.py --steps 1000 --source FULL92_CYCLE5_BEST.json --out FULL92_CYCLE6

Default full-active parameters: eps1e-6, coordinate trust box0.2 per stage, ftol1e-11, objective sum, free volume and actual centroid constrained0. All273 nonroot coordinates may vary. The fixed root is a similarity gauge. Each stage rebuilds an acyclic normal escape tree. Initial active92 planes imply F<=92 and hence C<=540 throughout bounded convex members, regardless of triangulation. Cycles can lose inactive input planes. Exact C426 endpoint has73active of92 supplied.

Observed finite outcomes: fixed84/variable60 normal-chain search reached mass-feasible C514 with S1/U10 at fixed volume and S1/U8 at free volume, without eliminating secondary radial basins. Releasing the old inactive constraints and varying all91 nonroot normals reduced the normalized sum of physical positive merge bars from about0.561418 to0.174749014262139 after six stages. Stage6 mass-feasible numerical C426 has S1/U31; exact G12/G6 census is independently stored as (1,31,30)/000. Largest physical squared-radius bar fell from original C5080.489119650754390 to0.115659445872020, but many small peaks were created. This is useful finite progress, not class110 and not proof that the family cannot solve the target. Stage7 was interrupted before a terminal receipt and is not accepted.

To start a fresh search directly from the exact C426 checkpoint without redoing optimization, run the exact recovery then create a source JSON with normals equal to its 92 integer new_normals divided by its grid; pass that file via --source. No other history checkpoint is needed.

## chain_persistence.py
```python
"""Finite C508 normal-chain redesign using complete radial merge persistence.
A numerical scout, not an exact candidate certificate. New60 normals vary;
all original84 remain as constraints. Actual exposed hull and filled centroid
are rebuilt. Full source input comes from RECOVER_C508.py, hash-pinned below.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
 os.environ[key]='1'
import json,sys,hashlib,time,argparse
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import minimize
from RECOVER_C508 import original_planes,G6,CHECKPOINT
sys.set_int_max_str_digits(0)
EXPECTED_SOURCE='12c3e1fa064498a760c0c7eb5ef0d79d00276584b0053dab531b7c6cc5cb3838'
assert hashlib.sha256(Path(__file__).with_name('RECOVER_C508.py').read_bytes()).hexdigest()==EXPECTED_SOURCE

class Model:
 def __init__(self,eps=5e-6):
  planes=original_planes(G6);self.old=np.array([[x/a[3] for x in a[:3]] for a in planes])
  self.start=np.array(CHECKPOINT['new_normals'],float)/CHECKPOINT['grid'];self.m=len(self.start);self.D=3*self.m;self.eps=eps
  a=self.old@self.old.T-np.sum(self.old**2,axis=1)[:,None];np.fill_diagonal(a,-np.inf)
  roots=np.where(a.max(1)<0)[0];assert len(roots)==1
  self.root=self.old[roots[0]].copy();self.cache=None;self.evals=0
  self.initial=self.geometry(self.start.ravel());self.volume=self.initial['volume']
 def geometry(self,z):
  if self.cache is not None and np.array_equal(z,self.cache[0]):return self.cache[1]
  new=z.reshape(self.m,3);N=np.vstack([self.old,new]);dh=ConvexHull(N)
  # A polar facet gives a physical vertex. Coplanar triangulation facets
  # nominate duplicates; round only for nomination identity, never final proof.
  assert np.all(dh.equations[:,3]<-1e-8),'polar does not contain origin'
  As=N[dh.simplices];inv=np.linalg.inv(As);ps=inv.sum(2)
  keys=np.round(ps,10);_,idx,ids=np.unique(keys,axis=0,return_index=True,return_inverse=True)
  p=ps[idx];owners=dh.simplices[idx];iv=inv[idx];nv=len(p)
  pj=np.zeros((nv,3,self.D))
  for v in range(nv):
   for col,n in enumerate(owners[v]):
    if n>=len(self.old):pj[v,:,3*(n-len(self.old)):3*(n-len(self.old))+3]=-iv[v,:,col,None]*p[v,None,:]
  faces=[];active=[]
  for n in dh.vertices:
   vs=np.unique(ids[np.where((dh.simplices==n).any(1))[0]])
   if len(vs)<3:continue
   drop=np.argmax(np.abs(N[n]));ax=[k for k in range(3) if k!=drop]
   xy=p[vs][:,ax];mid=xy.mean(0);vs=vs[np.argsort(np.arctan2(xy[:,1]-mid[1],xy[:,0]-mid[0]))].tolist()
   if np.dot(np.cross(p[vs[1]]-p[vs[0]],p[vs[2]]-p[vs[1]]),N[n])<0:vs.reverse()
   faces.append(vs);active.append(int(n))
  edgefaces={};tri=[];towner=[]
  for f,vs in enumerate(faces):
   for i,j in zip(vs,vs[1:]+vs[:1]):edgefaces.setdefault(tuple(sorted((i,j))),[]).append(f)
   for k in range(1,len(vs)-1):tri.append((vs[0],vs[k],vs[k+1]));towner.append(active[f])
  assert all(len(fs)==2 for fs in edgefaces.values())
  assert nv-len(edgefaces)+len(faces)==2
  t=p[np.array(tri)];co=np.cross(t[:,1]-t[:,0],t[:,2]-t[:,0]);six=np.einsum('ij,ij->i',t[:,0],np.cross(t[:,1],t[:,2]))
  assert six.min()>0
  V=six.sum()/6;M=(six[:,None]*t.sum(1)).sum(0)/24;c=M/V
  H=np.zeros((self.m,3,3))
  for a,nn,cr in zip(t,towner,co):
   if nn<len(self.old):continue
   n=N[nn];s=a.sum(0);H[nn-len(self.old)]+=np.dot(cr,n)/(24*np.dot(n,n))*(np.outer(s,s)+a.T@a)
  J=np.einsum('ijk,ik->ij',H,new);Vj=-J.ravel();Mj=-H.transpose(1,0,2).reshape(3,self.D);cj=(Mj-c[:,None]*Vj)/V
  x=p-c;xj=pj-cj[None,:,:];r2=(x*x).sum(1);rj=2*np.einsum('vi,vij->vj',x,xj)
  edges=np.array(sorted(edgefaces));ei,ej=edges.T;d=x[ej]-x[ei];dd=(d*d).sum(1)
  assert dd.min()>1e-22
  tt=np.clip(-np.einsum('ij,ij->i',x[ei],d)/dd,0,1);foot=x[ei]+tt[:,None]*d
  h=(foot*foot).sum(1);hj=2*np.einsum('ei,eij->ej',foot,(1-tt)[:,None,None]*xj[ei]+tt[:,None,None]*xj[ej])
  par=list(range(nv));pk=list(range(nv));members=[{i} for i in range(nv)];bars=[]
  def root(i):
   while par[i]!=i:par[i]=par[par[i]];i=par[i]
   return i
  for e in np.argsort(-h,kind='stable'):
   i,j=edges[e];a,b=root(i),root(j)
   if a==b:continue
   if (r2[pk[a]],-pk[a])<(r2[pk[b]],-pk[b]):a,b=b,a
   delta=r2[pk[b]]-h[e]
   if delta>1e-12:
    bars.append(dict(delta=float(delta),peak=int(pk[b]),edge=edges[e].tolist(),basin=sorted(members[b]),gradient=rj[pk[b]]-hj[e]))
   par[b]=a;members[a]|=members[b]
  val=sum(b['delta'] for b in bars)/V**(2/3)
  grad=sum((b['gradient'] for b in bars),np.zeros(self.D))/V**(2/3)-(2/3)*val*Vj/V
  Q=N[np.array(active)];Q=Q/(1-Q@c)[:,None]
  def crit(a):
   e=a@a.T-np.sum(a*a,axis=1)[:,None];np.fill_diagonal(e,-np.inf);m=e.max(1)
   return np.where(m<-1e-10)[0].tolist(),m
  ss,sm=crit(Q);uu,um=crit(x)
  ans=dict(value=val,gradient=grad,volume=V,volume_gradient=Vj,moment=M,moment_gradient=Mj,centroid=c,centroid_gradient=cj,points=p,edges=edges,faces=faces,active=active,normals=N,
   bars=bars,S=len(ss),U=len(uu),S_inputs=[active[s] for s in ss],U_vertices=uu,C=2*len(edges),vertex_count=nv,facet_count=len(active),minedge=float(np.sqrt(dd.min())),R=float(np.sqrt(r2.max())))
  self.evals+=1;self.cache=(z.copy(),ans);return ans
 def flow(self,z):
  new=z.reshape(self.m,3);nxt=np.vstack([self.root,new[:-1]])
  f=np.einsum('ij,ij->i',new,nxt)-(1+self.eps)*np.einsum('ij,ij->i',new,new)
  jac=np.zeros((self.m,self.D))
  for i in range(self.m):
   jac[i,3*i:3*i+3]=nxt[i]-2*(1+self.eps)*new[i]
   if i:jac[i,3*(i-1):3*i]=new[i]
  return f,jac
 def mass(self,z,fix_volume=True):
  a=self.geometry(z)
  if fix_volume:return np.r_[a['centroid'],np.log(a['volume']/self.volume)],np.vstack([a['centroid_gradient'],a['volume_gradient']/a['volume']])
  return a['centroid'],a['centroid_gradient']
 def summary(self,z):
  a=self.geometry(z)
  return {k:a[k] for k in ('value','volume','S','U','C','vertex_count','facet_count','minedge','R')}|{'centroid':a['centroid'].tolist(),'minimum_flow':float(self.flow(z)[0].min()),'bars':[{'delta':b['delta'],'peak':b['peak'],'edge':b['edge'],'basin_vertices':len(b['basin'])} for b in sorted(a['bars'],key=lambda b:-b['delta'])]}

def run(steps,out,eps,fix_volume,bound,check):
 model=Model(eps);x=model.start.ravel().copy()
 if check:
  rng=np.random.default_rng(190930);v=rng.normal(size=len(x));v/=np.linalg.norm(v);a=model.geometry(x)
  for step in [1e-6,1e-7,1e-8]:
   b=model.geometry(x+step*v);c=model.geometry(x-step*v)
   print('DERIVATIVE',step,'value',(b['value']-c['value'])/(2*step),a['gradient']@v,'mass',(b['centroid']-c['centroid'])/(2*step),a['centroid_gradient']@v,flush=True)
  return
 trace=[];best=[None];start=time.time()
 def fun(z):
  a=model.geometry(z);return a['value'],a['gradient']
 def callback(z):
  row=model.summary(z);row['iteration']=len(trace)+1;trace.append(row)
  if row['minimum_flow']>=-1e-9 and np.linalg.norm(row['centroid'])<1e-8 and row['C']<622 and (not fix_volume or abs(np.log(row['volume']/model.volume))<1e-8):
   if best[0] is None or row['value']<best[0]['summary']['value']:best[0]={'normals':z.reshape(-1,3).tolist(),'summary':row};Path(out+'_BEST.json').write_text(json.dumps(best[0],sort_keys=True,indent=2)+'\n')
  if len(trace)%10==0:print('STEP',json.dumps(row),flush=True)
 res=minimize(fun,x,jac=True,method='SLSQP',bounds=list(zip(x-bound,x+bound)),
  constraints=[{'type':'eq','fun':lambda z:model.mass(z,fix_volume)[0],'jac':lambda z:model.mass(z,fix_volume)[1]},
  {'type':'ineq','fun':lambda z:model.flow(z)[0],'jac':lambda z:model.flow(z)[1]}],
  callback=callback,options={'maxiter':steps,'ftol':1e-11,'disp':False})
 report={'status':'finite numerical scout, no exact construction or exclusion','steps_requested':steps,'steps_executed':int(res.nit),'success':bool(res.success),'message':str(res.message),'eps':eps,'fix_volume':fix_volume,'bound':bound,'elapsed_seconds':time.time()-start,'evaluations':model.evals,'final':model.summary(res.x),'normals':res.x.reshape(-1,3).tolist(),'trace':trace,'best':best[0]}
 Path(out+'.json').write_text(json.dumps(report,sort_keys=True,indent=2)+'\n');print('FINAL',json.dumps({k:v for k,v in report.items() if k not in ('trace','normals','best')}),flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--steps',type=int,default=200);ap.add_argument('--out',default='CHAIN_PERSISTENCE');ap.add_argument('--eps',type=float,default=5e-6);ap.add_argument('--bound',type=float,default=1.0);ap.add_argument('--free-volume',action='store_true');ap.add_argument('--check',action='store_true');a=ap.parse_args();run(a.steps,a.out,a.eps,not a.free_volume,a.bound,a.check)
```

## full_active_persistence.py
```python
"""Mass-closed full-active C508 redesign; keeps at most 92 supporting planes.
The inherited numerical geometry/moment/persistence implementation is unmodified.
The one stable normal is fixed (similarity gauge); all other active normals vary.
Parent polar escape witnesses are actual active facets, never discarded inputs.
No exact assertion is made until RECOVER_C508.audit audits rounded checkpoints.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import json,argparse,time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from chain_persistence import Model

class FullActive(Model):
 def __init__(self,eps=1e-6,source=None):
  seed=Model();a=seed.initial
  if source is None:
   root_index=a['S_inputs'][0];self.original_input_ids=[root_index]+[i for i in a['active'] if i!=root_index]
   normals=a['normals'][self.original_input_ids]
  else:
   d=json.loads(Path(source).read_text());normals=np.array(d['normals']);self.original_input_ids=d.get('original_input_ids')
  self.old=normals[:1].copy();self.start=normals[1:].copy();self.m=len(self.start);self.D=3*self.m;self.eps=eps
  self.root=self.old[0].copy();self.cache=None;self.evals=0
  m=normals@normals.T-(normals*normals).sum(1)[:,None];np.fill_diagonal(m,-np.inf)
  self.parents=np.argmax(m,axis=1)[1:]
  assert np.min(m[np.arange(1,len(normals)),self.parents])>0,'initial normals need S1 at the origin'
  for i in range(1,len(normals)):
   j=i;seen=set()
   while j!=0:
    assert j not in seen;seen.add(j);j=self.parents[j-1]
  self.initial=self.geometry(self.start.ravel());self.volume=self.initial['volume']
 def flow(self,z):
  n=np.vstack([self.old,z.reshape(self.m,3)]);child=n[1:];pa=n[self.parents]
  f=(child*pa).sum(1)-(1+self.eps)*(child*child).sum(1)
  jac=np.zeros((self.m,self.D))
  for i,j in enumerate(self.parents):
   jac[i,3*i:3*i+3]=pa[i]-2*(1+self.eps)*child[i]
   if j:jac[i,3*(j-1):3*j]=child[i]
  return f,jac

def run(a):
 model=FullActive(a.eps,a.source);x=model.start.ravel().copy();initial=model.summary(x)
 trace=[];best=[None];start=time.time();failure=None
 def objective(z):
  d=model.geometry(z)
  if a.objective=='sum':return d['value'],d['gradient']
  if not d['bars']:return 0.,np.zeros_like(z)
  b=max(d['bars'],key=lambda b:b['delta']);val=b['delta']/d['volume']**(2/3)
  return val,b['gradient']/d['volume']**(2/3)-(2/3)*val*d['volume_gradient']/d['volume']
 def save_best(z,row):
  if row['minimum_flow']>=-1e-9 and np.linalg.norm(row['centroid'])<1e-8 and (not a.fix_volume or abs(np.log(row['volume']/model.volume))<1e-8):
   if best[0] is None or row['value']<best[0]['summary']['value']:
    best[0]={'normals':np.vstack([model.old,z.reshape(-1,3)]).tolist(),'original_input_ids':model.original_input_ids,'parents':model.parents.tolist(),'summary':row}
    Path(a.out+'_BEST.json').write_text(json.dumps(best[0],sort_keys=True,indent=2)+'\n')
 def callback(z):
  row=model.summary(z);row['iteration']=len(trace)+1;trace.append(row);save_best(z,row)
  if len(trace)%10==0:print('STEP',json.dumps(row),flush=True)
 save_best(x,initial)
 try:
  res=minimize(objective,x,jac=True,method='SLSQP',bounds=list(zip(x-a.bound,x+a.bound)),constraints=[
   {'type':'eq','fun':lambda z:model.mass(z,a.fix_volume)[0],'jac':lambda z:model.mass(z,a.fix_volume)[1]},
   {'type':'ineq','fun':lambda z:model.flow(z)[0],'jac':lambda z:model.flow(z)[1]}],
   callback=callback,options={'maxiter':a.steps,'ftol':a.ftol,'disp':False})
  final=model.summary(res.x);save_best(res.x,final);normals=np.vstack([model.old,res.x.reshape(-1,3)]).tolist();success=bool(res.success);message=str(res.message)
 except Exception as e:
  failure=repr(e);final=None;normals=None;success=False;message='geometric/numerical trial failed'
 report={'status':'finite numerical scout, no exact construction or exclusion','parameters':vars(a),'initial':initial,'success':success,'message':message,'failure':failure,'elapsed_seconds':time.time()-start,'evaluations':model.evals,'final':final,'normals':normals,'original_input_ids':model.original_input_ids,'parents':model.parents.tolist(),'trace':trace,'best':best[0]}
 Path(a.out+'.json').write_text(json.dumps(report,sort_keys=True,indent=2)+'\n');print('FINAL',json.dumps({k:v for k,v in report.items() if k not in ('trace','normals','best','parents','original_input_ids')}),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--steps',type=int,default=700);p.add_argument('--out',default='FULL_ACTIVE');p.add_argument('--eps',type=float,default=1e-6);p.add_argument('--bound',type=float,default=.2);p.add_argument('--ftol',type=float,default=1e-11);p.add_argument('--fix-volume',action='store_true');p.add_argument('--source');p.add_argument('--objective',choices=['sum','max'],default='sum');run(p.parse_args())
```
