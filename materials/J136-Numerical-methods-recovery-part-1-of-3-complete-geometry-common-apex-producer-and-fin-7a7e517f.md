# material-7a7e517fddc3

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# J136 numerical methods recovery part 1/3

Object: J136 finite polar-forest and common-apex investigations from FLEX78_G8, including the numerical producer of the two exact APEX136 bodies. These methods did NOT produce own110. Parts1/2/3 together preserve every selected producing source, exact input reconstruction, nondefault settings and frozen continuation parameters. Numerical trajectories are not promised bit-portable. The exact cut/corridor endpoints are reconstructed separately by [internal-source-reference] PLUS mandatory correction [internal-source-reference], with engine131.py from [internal-source-reference] and poly134.py from [internal-source-reference]. All four are required exact dependencies; naming them does not deliver their files.

The retained rotate135.py and scout134.py below are COMPLETE minimal import units: the original source prefixes through report and bars respectively, with unused legacy optimizers/entrypoints removed. Every retained function/import is literal, including the unused chart_basis and input_points helpers. input_points() is never called by J136; DETACHED_G6.txt is NOT a J136 dependency. The six new 136.py producers in parts1/2 are unchanged complete original files. Their imports have full closure here. Keep the trailing blank line after these two prefix units for the listed hashes.

Environment used: CPython3.13.5, NumPy2.3.5, SciPy1.17.0, Torch2.10.0+cpu, BLAS/OMP/Torch one thread. Exact Fraction arithmetic needs standard Python; numerical hull nomination is not a proof. scout134.bars retains every floating-positive bar with dep>0 and NO final depth floor. Near-degenerate transformed facets can make floating bar counts disagree with floating direct S/U counts; those are inconsistent NOMINATIONS, not exact census or hidden cancellations. No numerical110 was found.

## Scientific scope
The common-apex producer uses p.q=offset and a planar angular/radial path, then physically intersects all resulting supports. Actual uniform centroid is recomputed, not assigned. The first20 scouts vary10 link counts and two windings; the volume-sensitive96 positive-guard scouts vary k=[10,12,14,16,20,24,30,40], offset=[.947,.96,1], allocation=[.01,.25,.5,1], first_tangent=True. Their finite negative results do not exclude other parameters. The two exact freezes use k10/offset1/allocation1 and k30/offset1/allocation.01, winding1/bulge0, integer normals on1e10 and exact h=n.old_vertex6. Those exact integers, not repeated floating trigonometry, define the accepted nonwinners.

The later15 whole-body projective/shared-affine starts use the exact K30 body, actual homogeneous mass, one affine map and its reciprocal polar. All chart denominators are at least.15 by construction. They preserve the face lattice and can leave the excluded nested corridor. All15 completed without numerical110. The best direct reported count was S2/U2, but some returned bar-count/direct-count discrepancies make these reports unsuitable as exact classifications. There was no rational endpoint audit of the orbit and no orbit-wide exclusion. Every final8-vector is frozen in part3; optimizer convergence is not class success.

## Files and hashes
scout134.py1220B SHA5cbef9f1c09f7e2466548f4f2d4fa4d31bb7370f2f0455c68a531045207994ae
rotate135.py4162B SHA f306b42ccb74b1e503bafc0e7c809c55f54eb097d67515ab2e5639913fb6dc2a
apexchain136.py3459B SHA7a7737d97c3edcd9a269eb914af01ebd31a02824b1778096f4d7a82045120a56
smallcap136.py2231B SHA61d6b8bb21bdd9b32ea4824520a8209cf4f00016f20c9118ceb060d7189ec33f
orbit136.py4643B SHA d5eb6897443cfafedc24c6723ac1f82e84d06b8d11d7456669d0f6c5b6fa7afd

## scout134.py
```python
"""Numerical filled-hull geometry, exact source input and full radial bar lists.
All numerical values are nominations only. No depth threshold establishes class.
"""
from pathlib import Path
import json,itertools,hashlib
import numpy as np
from scipy.spatial import ConvexHull
ROOT=Path(__file__).resolve().parent

def input_points():
 w=np.loadtxt(ROOT/'DETACHED_G6.txt',skiprows=1)
 return w/1000000

def bars(X,edges):
 radii=np.einsum('ij,ij->i',X,X); edges=np.asarray(edges,dtype=int)
 dx=X[edges[:,1]]-X[edges[:,0]]
 z=np.clip(-np.einsum('ij,ij->i',X[edges[:,0]],dx)/np.einsum('ij,ij->i',dx,dx),0,1)
 foot=X[edges[:,0]]+z[:,None]*dx
 level=np.einsum('ij,ij->i',foot,foot)
 par=np.arange(len(X)); peak=radii.copy(); root_id=np.arange(len(X)); out=[]
 def find(i):
  while par[i]!=i:par[i]=par[par[i]];i=par[i]
  return i
 for k in sorted(range(len(edges)),key=lambda k:(level[k],int(edges[k,0]),int(edges[k,1])),reverse=True):
  a,b=map(find,edges[k])
  if a==b:continue
  if peak[a]<peak[b]:a,b=b,a
  dep=1-level[k]/peak[b]
  if dep>0:out.append(dict(root=int(root_id[b]),edge=edges[k].tolist(),birth=float(peak[b]),death=float(level[k]),depth=float(dep)))
  par[b]=a
 return sorted(out,key=lambda z:-z['depth'])

```

## rotate135.py
```python
"""Flexible polygon-plane finite homogeneous deformation. Numerical search, exact freeze separate.
All maximal face cycles are fixed; polygon normal directions may change. Actual
filled volume and centroid are reintegrated from the entire oriented boundary.
The patch chart eliminates exact linear planarity equations, not mesh diagonals.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
from pathlib import Path
from fractions import Fraction as F
import json,time,argparse,itertools,hashlib
import numpy as np
from scipy.linalg import null_space
from scipy.optimize import minimize
import torch
from torch.func import jacfwd
from scout134 import bars
ROOT=Path(__file__).resolve().parent
torch.set_num_threads(1);torch.set_default_dtype(torch.float64)

def encode(x):
 if isinstance(x,np.ndarray): return x.tolist()
 if isinstance(x,np.generic):return x.item()
 if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [encode(v) for v in x]
 return x

def load(name):
 r=json.loads(Path(name).read_text());X=np.array([[float(F(v)) for v in row]for row in r['points']]);return X,[tuple(t)for t in r['faces']]

def chart_basis(X,fs):
 rows=[];patches=[]
 for i,t in enumerate(fs):
  if len(t)<=3:continue
  triples=list(itertools.combinations(t,3));a,b,c=max(triples,key=lambda t:np.linalg.norm(np.cross(X[t[1]]-X[t[0]],X[t[2]]-X[t[0]])))
  n=np.cross(X[b]-X[a],X[c]-X[a]);n/=np.linalg.norm(n)
  patches.append(dict(face=i,vertices=list(t),normal=n.tolist()))
  for j in t[1:]:
   r=np.zeros(3*len(X));r[3*j:3*j+3]=n;r[3*t[0]:3*t[0]+3]=-n;rows.append(r)
 A=np.array(rows);B=null_space(A,rcond=1e-12) if len(rows) else np.eye(3*len(X))
 assert np.max(abs(A@B),initial=0)<1e-12
 return B,patches

def spec(X,fs):
 tri=np.array([(t[0],t[k],t[k+1])for t in fs for k in range(1,len(t)-1)],int)
 picks=[];edges={};turns=[]
 for f,t in enumerate(fs):
  triples=list(itertools.combinations(t,3));best=max(triples,key=lambda z:np.linalg.norm(np.cross(X[z[1]]-X[z[0]],X[z[2]]-X[z[0]])))
  # combinations keep the face's cyclic order, even when labels are not ordered.
  picks.append(best)
  for k,v in enumerate(t):
   edges.setdefault(tuple(sorted((v,t[(k+1)%len(t)]))),[]).append(f)
   turns.append((f,t[k-1],v,t[(k+1)%len(t)]))
 assert all(len(v)==2 for v in edges.values())
 edges=dict(sorted(edges.items()));local=set()
 for edge,(f,g)in edges.items():
  for v in fs[g]:
   if v not in fs[f]:local.add((f,v))
  for v in fs[f]:
   if v not in fs[g]:local.add((g,v))
 plan=np.array([(f,v)for f,t in enumerate(fs)for v in t if v not in picks[f]],int)
 return dict(plan=plan,tri=tri,picks=np.array(picks,int),edges=np.array(list(edges),int),de=np.array(list(edges.values()),int),local=np.array(sorted(local),int),turns=np.array(turns,int))

def geom(X,fs,sp=None):
 if sp is None:sp=spec(X,fs)
 a,b,c=(X[sp['tri'][:,j]]for j in range(3));d=np.einsum('ij,ij->i',a,np.cross(b,c));V=d.sum()/6;assert V>0
 M=(d[:,None]*(a+b+c)).sum(0)/24;g=M/V;Y=X-g
 a,b,c=(Y[sp['picks'][:,j]]for j in range(3));n=np.cross(b-a,c-a);ns=np.linalg.norm(n,axis=1);n=n/ns[:,None];h=(n*a).sum(1);assert min(h)>0;Q=n/h[:,None]
 def scores(Z):
  rr=(Z*Z).sum(1);W=(Z@Z.T-rr[:,None])/rr[:,None];np.fill_diagonal(W,-np.inf);return W,W.max(1),W.argmax(1)
 PW,ps,pw=scores(Y);QW,qs,qw=scores(Q)
 gap=h[:,None]-n@Y.T;mask=np.ones(gap.shape,bool)
 plan=[]
 for i,t in enumerate(fs):mask[i,list(t)]=False;plan.extend(gap[i,list(t)])
 turns=sp['turns'];tr=np.einsum('ij,ij->i',n[turns[:,0]],np.cross(X[turns[:,2]]-X[turns[:,1]],X[turns[:,3]]-X[turns[:,2]]))
 return dict(X=X,Y=Y,V=V,M=M,g=g,n=n,h=h,Q=Q,PW=PW,QW=QW,ps=ps,qs=qs,pw=pw,qw=qw,S=np.where(qs<0)[0],U=np.where(ps<0)[0],P=bars(Y,sp['edges']),Qbars=bars(Q,sp['de']),hull=float(gap[mask].min()),planarity=float(abs(np.array(plan)).max()),turn=float(tr.min()),sp=sp)

def report(A):
 return encode(dict(VEF=[len(A['X']),len(A['sp']['edges']),len(A['Q'])],S=A['S'],U=A['U'],volume=A['V'],centroid=A['g'],P=A['P'],Q=A['Qbars'],hull=A['hull'],planarity=A['planarity'],turn=A['turn'],p_second=np.sort(A['ps'])[1],q_third=np.sort(A['qs'])[2]))

```

## apexchain136.py
```python
"""A finite polar chain on the plane dual to the old unstable vertex.
All newly proposed physical supports pass through that exact old material
vertex after rational freezing. Numerical hull/centroid output is nomination
only. This script does not infer own S1/U1 from reference-chain feasibility.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import json,argparse,itertools
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from scipy.spatial import ConvexHull
import rotate135 as r
ROOT=Path(__file__).resolve().parent

def make(A,k,bulge=0.,winding=1,offset=1.,allocation=1.,first_tangent=False):
 p=A['Y'][int(A['U'][0])];u=A['Q'][int(A['S'][np.argmin((A['Q'][A['S']]**2).sum(1))])];z=A['Q'][int(A['S'][np.argmax((A['Q'][A['S']]**2).sum(1))])]
 L=np.linalg.norm(p);v=p/L;up=u-(u@v)*v;zp=z-(z@v)*v;ru=np.linalg.norm(up);rz=np.linalg.norm(zp);e1=up/ru;e2=zp-(zp@e1)*e1;e2/=np.linalg.norm(e2);phi=np.arccos(np.clip(up@zp/ru/rz,-1,1))
 if winding<0:phi=phi-2*np.pi
 if first_tangent:
  ru=((u@u)-(u@v)*offset/L)/np.linalg.norm(up)*(1+1e-6)
 log_min=-np.log(np.cos(phi/k));log_rho=log_min+allocation*(np.log(rz/ru)/k-log_min)
 rows=[]
 for i in range(k):
  t=i/k;rr=ru*np.exp(i*log_rho+bulge*np.sin(np.pi*t));q=offset/L*v+rr*(np.cos(phi*t)*e1+np.sin(phi*t)*e2);rows.append(q)
 chain=np.vstack([u,rows,z]);guards=(chain[:-1]*(chain[1:]-chain[:-1])).sum(1)/(chain[:-1]**2).sum(1)
 return np.array(rows),dict(k=k,bulge=bulge,winding=winding,offset=offset,allocation=allocation,first_tangent=first_tangent,phi=float(phi),perp_ratio=float(rz/ru),guards=guards.tolist(),min_guard=float(guards.min()),U=int(A['U'][0]),S=A['S'].tolist())

def polar_vertices(Q):
 ch=ConvexHull(Q);X=-ch.equations[:,:3]/ch.equations[:,3,None];keep=[]
 for x in X:
  if all(np.linalg.norm(x-y)>1e-8 for y in keep):keep.append(x)
 return np.array(keep)

def maximal_numeric(X):
 ch=ConvexHull(X);groups=[]
 for t,eq in zip(ch.simplices,ch.equations):
  for g in groups:
   if np.linalg.norm(eq-g[0])<1e-7:g[1].update(map(int,t));break
  else:groups.append([eq.copy(),set(map(int,t))])
 faces=[]
 for eq,vs in groups:
  vs=list(vs);n=eq[:3];c=X[vs].mean(0);e1=X[vs[0]]-c;e1/=np.linalg.norm(e1);e2=np.cross(n,e1);ang=np.arctan2((X[vs]-c)@e2,(X[vs]-c)@e1);cy=[vs[i]for i in np.argsort(ang)];j=cy.index(min(cy));faces.append(tuple(cy[j:]+cy[:j]))
 return sorted(faces)

def search(inp,tag):
 X,fs=r.load(inp);A=r.geom(X,fs);out=[]
 for k in [10,12,13,14,15,16,18,20,24,28]:
  for winding in [1,-1]:
   rows,info=make(A,k,winding=winding);Q=np.vstack([A['Q'],rows]);P=polar_vertices(Q);ff=maximal_numeric(P)
   try:
    C=r.geom(P,ff);info.update(actual=r.report(C),submitted_polar=len(Q),new_active_rows=int(len(ConvexHull(Q).vertices)-sum(i<len(A['Q'])for i in ConvexHull(Q).vertices)),relative_volume=float(C['V']/A['V']),centroid_drift=float(np.linalg.norm(C['g'])),exact=False)
   except Exception as er:info['error']=repr(er)
   out.append(info);print('APEX_CHAIN',k,winding,info['min_guard'], 'VEF',info.get('actual',{}).get('VEF'),'SU',len(info.get('actual',{}).get('S',[])),len(info.get('actual',{}).get('U',[])), 'vol',info.get('relative_volume'),flush=True)
 (ROOT/(tag+'_SCOUT.json')).write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--input',default='replayed/FLEX78_G8_EXACT.json');p.add_argument('--tag',default='APEXCHAIN136');a=p.parse_args();search(a.input,a.tag)
```

## smallcap136.py
```python
"""Finite volume-sensitive allocation of a common-apex polar chain.
No optimizer selects the frozen inputs: every nominated parameter is recorded.
All scouts include own mass and all unthresholded numerical P/Q diagnostics.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import argparse,json,time
from pathlib import Path
import numpy as np
import apexchain136 as c
r=c.r;ROOT=Path(__file__).resolve().parent

def run(inp,tag):
 X,fs=r.load(inp);A=r.geom(X,fs);allrows=[];best={};beg=time.time()
 for k in [10,12,14,16,20,24,30,40]:
  for tau in [.947,.96,1.0]:
   for allocation in [.01,.25,.5,1.]:
    rr,info=c.make(A,k,offset=tau,allocation=allocation,first_tangent=True)
    if info['min_guard']<=0:continue
    Q=np.vstack([A['Q'],rr]);P=c.polar_vertices(Q);ff=c.maximal_numeric(P)
    try:
     B=r.geom(P,ff);report=r.report(B)
     def count(Z):
      W=Z@Z.T-(Z*Z).sum(1)[:,None];np.fill_diagonal(W,-np.inf);return int(sum(W.max(1)<0))
     info.update(actual=report,reference=[count(Q),count(P)],volume_fraction=float(B['V']/A['V']),centroid_drift=float(np.linalg.norm(B['g'])),exact=False)
     score=(len(B['S'])+len(B['U']),sum(z['depth']for z in B['P']+B['Qbars']))
     key='feasible' if len(B['sp']['edges'])<=249 else 'overbudget'
     if key not in best or score<best[key][0]:
      best[key]=score,info
      (ROOT/(tag+'_BEST_'+key+'.json')).write_text(json.dumps(dict(points=P.tolist(),faces=ff,polar=Q.tolist(),nomination=info),separators=(',',':'))+'\n')
     print('SMALLCAP',k,tau,allocation,'E',len(B['sp']['edges']),'ref',info['reference'],'own',len(B['S']),len(B['U']),'vol',info['volume_fraction'],'g',info['centroid_drift'],flush=True)
    except Exception as er:info['error']=repr(er);print('SMALLCAP_ERROR',k,tau,allocation,repr(er),flush=True)
    allrows.append(info)
    (ROOT/(tag+'_SCOUT.json')).write_text(json.dumps(dict(input=Path(inp).name,elapsed=time.time()-beg,rows=allrows),separators=(',',':'))+'\n')
 print('SMALLCAP_COMPLETE',len(allrows),'BEST',best,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--input',default='replayed/FLEX78_G8_EXACT.json');p.add_argument('--tag',default='SMALLCAP136');a=p.parse_args();run(a.input,a.tag)
```

## orbit136.py
```python
"""Finite projective/shared-affine orbit search with actual homogeneous mass.
The fixed exact maximal boundary is transported projectively; b is bounded so
all chart denominators remain positive. The affine metric is shared by primal
and reciprocal polar. All non-global-root outgoing guards enter the loss.
Numerical nominations only; no guard or persistence floor is an exact claim.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import json,sys,time,argparse
from fractions import Fraction as F
from pathlib import Path
import numpy as np
import torch
from scipy.optimize import minimize
import rotate135 as r
ROOT=Path(__file__).resolve().parent
torch.set_default_dtype(torch.float64);torch.set_num_threads(1)

def setup(input_name):
 X,fs=r.load(ROOT/input_name);A=r.geom(X,fs);X=X-A['g'];sp=r.spec(X,fs)
 X0=torch.tensor(X);tri=torch.tensor(sp['tri']);I=torch.eye(len(X),dtype=torch.bool);J=torch.eye(len(fs),dtype=torch.bool)
 N=torch.tensor(A['n']);h=torch.tensor(A['h']);beta=.85/np.linalg.norm(X,axis=1).max()
 def points(z):
  u=z[:3];uu=torch.sqrt((u*u).sum()+1e-30);b=beta*torch.tanh(uu)*u/uu
  den=1+X0@b;P=X0/den[:,None]
  a0,a1,a2=(P[tri[:,j]] for j in range(3));dd=(a0*torch.linalg.cross(a1,a2)).sum(1);V=dd.sum()/6
  g=(dd[:,None]*(a0+a1+a2)).sum(0)/(24*V);Y=P-g
  aa=z[3:];A=torch.stack([torch.stack([aa[0].exp(),aa[2],aa[3]]),torch.stack([aa[0]*0,aa[1].exp(),aa[4]]),torch.stack([aa[0]*0,aa[0]*0,(-aa[0]-aa[1]).exp()])])
  np_=N+h[:,None]*b;hp=h-np_@g
  Q=np_/hp[:,None];Q=Q@torch.linalg.inv(A)
  return Y@A.T,Q,P@A.T,b,A,g,V,den
 def scores(Z,mask):
  rr=(Z*Z).sum(1);W=(Z@Z.T-rr[:,None])/rr[:,None];W=W.masked_fill(mask,-torch.inf);s=W.max(1).values
  # Exclude just the actual farthest point, not an arbitrary junior root.
  ii=torch.arange(len(Z))!=rr.argmax();return s[ii]
 def objective(z,wp,wq,tau):
  P,Q,raw,b,A,g,V,den=points(z);ps=scores(P,I);qs=scores(Q,J)
  # Linear-negative/near-zero quadratic hinge prevents large deficits being
  # cheap merely because they are distributed among many tiny subsidiaries.
  def cost(s):
   d=(tau-s).clamp(min=0);return (torch.sqrt(d*d+1e-10)-1e-5).sum()
  return wp*cost(ps)+wq*cost(qs)+1e-9*(z*z).sum()
 def full(z):
  with torch.no_grad():P,Q,raw,b,A,g,V,den=points(torch.tensor(z))
  geom=r.geom(raw.numpy(),fs);out=r.report(geom);out.update(b=b.tolist(),A=A.tolist(),parameter=z.tolist(),chart_min=float(den.min()),input=input_name)
  return raw.numpy(),out
 return objective,full,fs

def run(input_name,tag,starts,iterations):
 fun,full,fs=setup(input_name);rng=np.random.default_rng(136090);base=np.zeros(8);rows=[];best=None
 bounds=[(-3,3)]*3+[(-.9,.9)]*2+[(-1,1)]*3
 for k in range(starts):
  wp,wq=[(1.,1.),(2.,1.),(1.,2.),(.2,1.),(1.,.2)][k%5]
  z=base.copy() if k<5 else np.clip(rng.normal(0,.12,8),*[np.array(v)for v in zip(*bounds)])
  if k>=10 and best is not None:z=.9*np.array(best['parameter'])+rng.normal(0,.04,8);z=np.clip(z,*[np.array(v)for v in zip(*bounds)])
  calls=[0]
  def fg(z):
   zz=torch.tensor(z,requires_grad=True);v=fun(zz,wp,wq,1e-6);gg=torch.autograd.grad(v,zz)[0];calls[0]+=1;return float(v.detach()),gg.detach().numpy()
  res=minimize(fg,z,jac=True,method='L-BFGS-B',bounds=bounds,options={'maxiter':iterations,'maxls':35,'maxcor':20,'ftol':1e-14,'gtol':1e-10})
  P,out=full(res.x);out.update(k=k,weights=[wp,wq],nit=int(res.nit),nfev=calls[0],success=bool(res.success),message=str(res.message),fun=float(res.fun))
  loss=sum(x['depth']for x in out['P'])+sum(x['depth']for x in out['Q']);out['all_depth_sum']=loss;rows.append(out)
  if best is None or (len(out['S'])+len(out['U']),loss)<(len(best['S'])+len(best['U']),best['all_depth_sum']):
   best=out;(ROOT/(tag+'_BEST.json')).write_text(json.dumps(dict(points=P.tolist(),faces=fs,report=out),separators=(',',':'))+'\n')
  print('ORBIT136',tag,k,'SU',len(out['S']),len(out['U']),'bars',len(out['P']),len(out['Q']),'sum',loss,'nit',res.nit,'status',res.message,flush=True)
  (ROOT/(tag+'_LEDGER.json')).write_text(json.dumps(dict(config=dict(input=input_name,starts=starts,iterations=iterations,seed=136090,tau=1e-6,bounds=bounds),faces=fs,rows=rows),separators=(',',':'))+'\n')
  if len(out['S'])==len(out['U'])==1:break
 print('ORBIT136_COMPLETE',tag,'bestSU',len(best['S']),len(best['U']),'sum',best['all_depth_sum'],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--tag',required=True);p.add_argument('--starts',type=int,default=15);p.add_argument('--iterations',type=int,default=300);a=p.parse_args();run(a.input,a.tag,a.starts,a.iterations)
```
