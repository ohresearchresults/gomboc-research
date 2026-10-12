# material-1b4a7c148e2c

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# ACTUAL_MOMENT_FULLBAR_SEARCH_METHODS_V1

Complete experimental numerical source units used in the RESERVE31/free-geometry direction. These are reusable methods, NOT proofs of own110. Literal rational outputs and a complete independent exact auditor are in [internal-source-reference]. This capsule supplies the producing numerical method promised there. It contains all four complete local Python modules, not isolated derivatives.

## Exact recovery dependencies
The source below plus the two explicitly named already immutable input capsules is the complete recovery package:
- [internal-source-reference] contains RESERVE31_INPUT.json,1339bytes,SHA2564b1bed14b6174e65850f72f54a597e0dc284c3cf65fa3962d75a27c796017d5f, including all56 literal rows.
- [internal-source-reference] contains FREE_FIRST_G8_INPUT.json,979bytes,SHA2565b9b38f861e605bbc6db102e000cdd1325cfb2fde88de70a43542fed385348f3, including all31 literal rows. This is the OLD FREE_FIRST_G8, not FREE_LIVE_FULLBAR_G8.
- [internal-source-reference] contains complete exact_poly.py and the independently frozen FREE_LIVE_FULLBAR_G6/G7/G8 literal outputs with their exact audit manifests.
A worker using the entire replay needs these exact input dependencies explicitly attached. No sandbox/archive lookup is needed.

Runtime actually used Python3.13.5,NumPy2.3.5,SciPy1.17.0,torch2.10.0+cpu; OPENBLAS_NUM_THREADS=1,OMP_NUM_THREADS=1,torch threads1,float64. Floating search is piecewise smooth, changes hull/persistence pairing, has no certified global convergence and may take a different trajectory on another numerical stack. Timing fields are nondeterministic. Solver success is not an equilibrium certificate.

## Commands and observed output
Save the following four files with exactly one trailing LF. Put both recovered input JSON files beside them. Generate the OLD free starting file by:
```python
import json
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
raw=json.loads(Path('FREE_FIRST_G8_INPUT.json').read_text())
P=np.array(raw['points'],float)/raw['denominator']
P=P[sorted(ConvexHull(P).vertices)]
Path('FREE_FIRST_FLOAT_START.json').write_text(json.dumps({'P':P.tolist()}))
```
This generated start intentionally has default json.dumps separators and NO trailing newline:1182bytes,SHA2561e3fa7d80b664f12de017b5e09ef68d8840c923937075f7a91d316ddbc302570.
Run `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MAXITER=200 OUT=FREE_DYNAMIC1.json python dynamic_fullbar.py FREE_FIRST_FLOAT_START.json`.
Observed147 iterations,status0,best objective0.6306144874834172,minconstraint-1.7152165615153744e-10. Its best geometry independently rounded to grids6,7,8 is literally preserved and exactly audited in [internal-source-reference]. G8 is own817/weak000/C168,P0/Q7,exact relativeQdepthsum0.6306144899443885. G6/G7 lose uniqueU. No110 claim. FREE_DYNAMIC1.json contains nondeterministic elapsed seconds; exact frozen inputs and audit output bytes, not a timing-bearing optimizer report, are the acceptance authority.

Other reproducible methods: `MAXITER=100 python fullbar_geometry.py` starts original RESERVE31; `MAXITER=100 OUT=FREE_FULLBAR1.json python fullbar_geometry.py FREE_FIRST_FLOAT_START.json` starts older free checkpoint. `python float_landscape.py FREE_FIRST_G8_INPUT.json` is a floating diagnostic only. Homotopy starts with no HOMOTOPY_STATE.json: `MAXITER=120 python homotopy_geometry.py 0.05`, followed by targets0.15,0.3,0.5,0.75. A continuation must include its exact state file; state-file existence is not a certificate. A local target0.8 with MAXITER50 and radius0.8 was accepted by floating feasibility, not as own110.

Homotopy centre c(P)+(1-t)(z0-c(P0)) distinguishes virtual and actual centres. Fixed-facet support, area, interior and volume constraints are explicit. FullBar computes the actual centroid at every trial and differentiates the sum of ALL positive polar radial persistence depths through mass, normals and active edge feet. DynamicFull rebuilds the hull before every new trial and replaces fixed-facet constraints by all-point escape witnesses and a strict root test against all other points. This initial U1 witness system may itself restrict the search. Floating diagnostics use positive cutoffs and are not weak-equilibrium audits.

## Source manifest and checks
- homotopy_geometry.py6067bytes,SHA2564f0abecedb8e7f9f247069d0a316a811b34292a90ce696b3070223c46dd12037
- float_landscape.py1494bytes,SHA256d90de863827657927f4ac244ef865f40e028a185a928f7bfee21d643bdd634c2
- fullbar_geometry.py4569bytes,SHA256ef41d56f846f14b45d2cfb7bd8921c5166e7825ee24553fe673b919c86299d66
- dynamic_fullbar.py3310bytes,SHA256da9f1047a7c6c9db70c83c5a323ee6f8e2ba5679b6d7b08750f11e9e5894ce4f
Run `python -m py_compile homotopy_geometry.py float_landscape.py fullbar_geometry.py dynamic_fullbar.py` and `sha256sum *.py`. Numerical progress markers are DYNAMIC_ITER/FULLBAR_ITER then a JSON report; exact construction validation is `python exact_poly.py FREE_LIVE_FULLBAR_G8.json`, expected EXACT_POLY_AUDIT_PASS with817/weak000 as specified by its exact capsule.

## homotopy_geometry.py
```python
"""Experimental homogeneous geometry homotopy. Floating only until exact freeze.
Reference z_t = actual_volume_centroid(P)+(1-t)*(z0-centroid(P0)).
At t=1 every equilibrium inequality is at the actual volume centroid.
"""
import json,os,sys,time
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import minimize
import torch
from torch.func import jacfwd
torch.set_num_threads(1);torch.set_default_dtype(torch.float64)

def hull(P):
 hu=ConvexHull(P);fs=hu.simplices.copy()
 for i,f in enumerate(fs):
  if np.dot(np.cross(P[f[1]]-P[f[0]],P[f[2]]-P[f[0]]),hu.equations[i,:3])<0:fs[i,[1,2]]=fs[i,[2,1]]
 fs=np.array(sorted(fs.tolist(),key=lambda f:sorted(f)))
 return fs

def physics(P,fs):
 a,b,c=P[fs[:,0]],P[fs[:,1]],P[fs[:,2]];d=np.einsum('ij,ij->i',a,np.cross(b,c));v=d.sum()/6;cent=(d[:,None]*(a+b+c)).sum(axis=0)/(4*d.sum())
 return v,cent

def census(P,fs,z):
 nb=[set() for p in P];edge={}
 for i,f in enumerate(fs):
  for a,b in zip(f,np.roll(f,-1)):nb[a].add(b);nb[b].add(a);edge.setdefault(tuple(sorted((int(a),int(b)))),[]).append(i)
 S=[];U=[];sv=[];uv=[]
 for i,p in enumerate(P):
  g=max((p-z)@(P[j]-p) for j in nb[i]);uv.append(g)
  if g<0:U.append(i)
 for i,f in enumerate(fs):
  n=np.cross(P[f[1]]-P[f[0]],P[f[2]]-P[f[0]])
  g=min(np.dot(np.cross(n,P[b]-P[a]),z-P[a]) for a,b in zip(f,np.roll(f,-1)));sv.append(g)
  if g>0:S.append(i)
 return dict(S=S,U=U,SU=[len(S),len(U)],minU=min(abs(np.array(uv))),minS=min(abs(np.array(sv))))

class Model:
 def __init__(self,P,fs,z0,sroot=None,escape_override=None):
  self.N=len(P);self.fs_np=fs;self.fs=torch.tensor(fs,dtype=torch.long);self.V0,self.c0=physics(P,fs);self.offset=torch.tensor(z0-self.c0);self.P0=P.copy();self.nb=[set() for p in P]
  for f in fs:
   for a,b in zip(f,np.roll(f,-1)):self.nb[a].add(int(b));self.nb[b].add(int(a))
  cs=census(P,fs,z0);assert cs['SU'][1]==1;self.Uroot=cs['U'][0];self.Sroot=cs['S'][0] if sroot is None else sroot
  pu=[];pv=[];ps=[]
  for i in range(self.N):
   if i==self.Uroot:
    for j in sorted(self.nb[i]):pu.append(i);pv.append(j);ps.append(-1.)
   else:
    js=sorted(self.nb[i]);j=max(js,key=lambda j:(P[i]-z0)@(P[j]-P[i])/np.linalg.norm(P[j]-P[i]));pu.append(i);pv.append(j);ps.append(1.)
  self.pu=torch.tensor(pu);self.pv=torch.tensor(pv);self.ps=torch.tensor(ps)
  sf=[];sk=[];ss=[]
  for i,f in enumerate(fs):
   n=np.cross(P[f[1]]-P[f[0]],P[f[2]]-P[f[0]])
   if i==self.Sroot:
    for k in range(3):sf.append(i);sk.append(k);ss.append(1.)
   else:
    side=[np.dot(np.cross(n,P[f[(k+1)%3]]-P[f[k]]),z0-P[f[k]])/np.linalg.norm(np.cross(n,P[f[(k+1)%3]]-P[f[k]])) for k in range(3)]
    k=int(np.argmin(side)) if escape_override is None or i not in escape_override else escape_override[i];sf.append(i);sk.append(k);ss.append(-1.)
  self.sf=torch.tensor(sf);self.sk=torch.tensor(sk);self.ss=torch.tensor(ss)
  self.off=np.array([(i,j) for i,f in enumerate(fs) for j in range(self.N) if j not in f]);self.oi=torch.tensor(self.off[:,0]);self.oj=torch.tensor(self.off[:,1])
  norm=np.linalg.norm(np.cross(P[fs[:,1]]-P[fs[:,0]],P[fs[:,2]]-P[fs[:,0]]),axis=1);self.area_min=torch.tensor(norm*.02)
  self.t=0.;self.eps=1e-6;self.lastx=None;self.jf=jacfwd(self.constraints_torch)
 def constraints_torch(self,x):
  P=x.reshape(self.N,3);a=P[self.fs[:,0]];b=P[self.fs[:,1]];c=P[self.fs[:,2]];n=torch.linalg.cross(b-a,c-a);nr=torch.linalg.vector_norm(n,dim=1);nu=n/torch.clamp(nr[:,None],min=1e-15)
  d=(a*torch.linalg.cross(b,c)).sum(dim=1);v6=d.sum();cent=(d[:,None]*(a+b+c)).sum(dim=0)/(4*v6);z=cent+(1-self.t)*self.offset
  convex=(nu[self.oi]*(a[self.oi]-P[self.oj])).sum(dim=1)-1e-10
  inside=(nu*(a-z)).sum(dim=1)-1e-6
  pe=P[self.pv]-P[self.pu];rad=P[self.pu]-z
  pg=self.ps*(rad*pe).sum(dim=1)/torch.clamp(torch.linalg.vector_norm(rad,dim=1)*torch.linalg.vector_norm(pe,dim=1),min=1e-15)-self.eps
  u=self.fs[self.sf,self.sk];w=self.fs[self.sf,(self.sk+1)%3];side=torch.linalg.cross(nu[self.sf],P[w]-P[u]);sg=self.ss*(side*(z-P[u])).sum(dim=1)/torch.clamp(torch.linalg.vector_norm(side,dim=1),min=1e-15)-self.eps
  return torch.cat([pg,sg,convex,inside,nr-self.area_min,(v6/6-self.V0*.2).reshape(1)])
 def val(self,x):return self.constraints_torch(torch.tensor(x)).detach().numpy()
 def jac(self,x):return self.jf(torch.tensor(x)).detach().numpy()

def main():
 root=Path(__file__).parent;raw=json.loads((root/'RESERVE31_INPUT.json').read_text());P=np.array(sorted(set(map(tuple,raw['points']))),float)/raw['denominator'];P=P[sorted(ConvexHull(P).vertices)];fs=hull(P);z0=np.array([-.6,.08,-.32]);model=Model(P,fs,z0)
 outpath=root/'HOMOTOPY_STATE.json'
 state=json.loads(outpath.read_text()) if outpath.exists() else dict(t=0.,P=P.tolist(),steps=[],fs=fs.tolist())
 x=np.array(state['P']).ravel();old_t=float(state['t']);target=float(sys.argv[1]) if len(sys.argv)>1 else old_t+.05;model.t=target
 base=x.copy();radius=float(sys.argv[2]) if len(sys.argv)>2 else .5
 start=time.monotonic()
 r=minimize(lambda q:((q-base)**2).sum()/2,x,jac=lambda q:q-base,method='SLSQP',constraints={'type':'ineq','fun':model.val,'jac':model.jac},bounds=list(zip(P.ravel()-radius,P.ravel()+radius)),options={'maxiter':int(os.environ.get('MAXITER','50')),'ftol':1e-10,'disp':False})
 vals=model.val(r.x);Q=r.x.reshape(-1,3);vol,cen=physics(Q,fs)
 entry=dict(from_t=old_t,target=target,success=bool(r.success),status=int(r.status),message=str(r.message),iterations=int(r.nit),minconstraint=float(vals.min()),objective=float(r.fun),seconds=time.monotonic()-start,centroid=cen.tolist(),virtual=census(Q,fs,cen+(1-target)*model.offset.numpy()),actual=census(Q,fs,cen),volume=vol,P=Q.tolist())
 print(json.dumps({k:v for k,v in entry.items() if k!='P'},indent=2),flush=True)
 trial=root/('HOMOTOPY_TRIAL_'+str(target).replace('.','_')+'.json');trial.write_text(json.dumps(entry,separators=(',',':'))+'\n')
 if vals.min()>-1e-8:
  state.update(t=target,P=Q.tolist());state['steps'].append({k:v for k,v in entry.items() if k!='P'});outpath.write_text(json.dumps(state,separators=(',',':'))+'\n')
if __name__=='__main__':main()
```

## float_landscape.py
```python
import numpy as np
from homotopy_geometry import hull,physics,census

def radial(X,E):
 R=(X*X).sum(axis=1);events=[]
 for a,b in E:
  d=X[b]-X[a];t=np.clip(-X[a]@d/(d@d),0,1);h=np.sum((X[a]+t*d)**2);events.append((h,a,b))
 pa=list(range(len(X)));peak=list(range(len(X)));members=[{i} for i in pa];bars=[]
 def find(a):
  while pa[a]!=a:pa[a]=pa[pa[a]];a=pa[a]
  return a
 for h,a,b in sorted(events,reverse=True):
  u,v=find(a),find(b)
  if u==v:continue
  if R[peak[u]]<R[peak[v]]:u,v=v,u
  dep=(R[peak[v]]-h)/R[peak[v]]
  if dep>1e-13:bars.append(dict(peak=peak[v],elder=peak[u],depth=float(dep),component=sorted(members[v]),edge=[int(a),int(b)]))
  pa[v]=u;members[u]|=members[v]
 return bars

def landscape(P):
 fs=hull(P);V,c=physics(P,fs);E={}
 for k,f in enumerate(fs):
  for a,b in zip(f,np.roll(f,-1)):E.setdefault(tuple(sorted((int(a),int(b)))),[]).append(k)
 n=np.cross(P[fs[:,1]]-P[fs[:,0]],P[fs[:,2]]-P[fs[:,0]]);Q=n/np.einsum('ij,ij->i',n,P[fs[:,0]]-c)[:,None]
 pb=radial(P-c,E);qb=radial(Q,E.values());return dict(V=len(P),E=len(E),C=2*len(E),census=census(P,fs,c),Pbars=pb,Qbars=qb,Psum=sum(b['depth'] for b in pb),Qsum=sum(b['depth'] for b in qb),Qmax=max([b['depth'] for b in qb]+[0.]))
if __name__=='__main__':
 import json,sys
 from scipy.spatial import ConvexHull
 x=json.load(open(sys.argv[1]));P=np.array(x['P'] if 'P' in x else x['points'],float)
 if 'denominator' in x:P/=x['denominator']
 P=P[sorted(ConvexHull(P).vertices)]
 print(json.dumps(landscape(P),indent=2))
```

## fullbar_geometry.py
```python
"""Actual-volume-centred free geometry, complete Q-persistence objective.
Piecewise-smooth all-bar sum; full reconstruction/certification remains required.
No optimization convergence flag is treated as a physical result.
"""
from homotopy_geometry import *
from float_landscape import landscape

class FullBar(Model):
 def __init__(self,P,fs):
  V,c=physics(P,fs);super().__init__(P,fs,c)
  pu=[];pv=[];sg=[]
  for i in range(len(P)):
   js=[j for j in range(len(P)) if j!=i]
   if i==self.Uroot:
    for j in sorted(self.nb[i]):pu.append(i);pv.append(j);sg.append(-1.)
   else:
    j=max(js,key=lambda j:(P[i]-c)@(P[j]-P[i])/np.linalg.norm(P[j]-P[i]));pu.append(i);pv.append(j);sg.append(1.)
  self.pu=torch.tensor(pu);self.pv=torch.tensor(pv);self.ps=torch.tensor(sg)
  edges={}
  for f,tri in enumerate(fs):
   for a,b in zip(tri,np.roll(tri,-1)):edges.setdefault(tuple(sorted((int(a),int(b)))),[]).append(f)
  self.qedges=np.array(list(edges.values()));self.jf=jacfwd(self.constraints_torch);self.eps=1e-7;self.cache_x=None;self.reg=1e-7
 def geometry(self,x):
  P=x.reshape(self.N,3);a=P[self.fs[:,0]];b=P[self.fs[:,1]];cc=P[self.fs[:,2]];n=torch.linalg.cross(b-a,cc-a);nr=torch.linalg.vector_norm(n,dim=1);nu=n/torch.clamp(nr[:,None],min=1e-15)
  d=(a*torch.linalg.cross(b,cc)).sum(dim=1);v6=d.sum();c=(d[:,None]*(a+b+cc)).sum(dim=0)/(4*v6);h=(nu*(a-c)).sum(dim=1);Q=nu/torch.clamp(h[:,None],min=1e-12)
  return P,a,nu,nr,v6,c,h,Q
 def constraints_torch(self,x):
  P,a,nu,nr,v6,c,h,Q=self.geometry(x)
  edge=P[self.pv]-P[self.pu];rad=P[self.pu]-c;pg=self.ps*(edge*rad).sum(dim=1)/torch.clamp(torch.linalg.vector_norm(rad,dim=1)*torch.linalg.vector_norm(edge,dim=1),min=1e-15)-self.eps
  convex=(nu[self.oi]*(a[self.oi]-P[self.oj])).sum(dim=1)-1e-10
  return torch.cat([pg,convex,h-1e-6,nr-self.area_min,(v6/6-self.V0*.2).reshape(1)])
 def pairs(self,Q):
  R=(Q*Q).sum(axis=1);E=self.qedges;a=Q[E[:,0]];d=Q[E[:,1]]-a;t=np.clip(-np.sum(a*d,axis=1)/np.maximum(np.sum(d*d,axis=1),1e-30),0,1);lev=((a+t[:,None]*d)**2).sum(axis=1)
  pa=list(range(len(Q)));peak=pa.copy();pairs=[]
  def find(i):
   while pa[i]!=i:pa[i]=pa[pa[i]];i=pa[i]
   return i
  for k in sorted(range(len(E)),key=lambda k:(-lev[k],tuple(E[k]))):
   aa,bb=E[k];u,v=find(aa),find(bb)
   if u==v:continue
   if (R[peak[u]],peak[u])<(R[peak[v]],peak[v]):u,v=v,u
   if R[peak[v]]-lev[k]>1e-14*R[peak[v]]:pairs.append((peak[v],int(aa),int(bb)))
   pa[v]=u
  return pairs
 def update_objective(self,x):
  if self.cache_x is not None and np.array_equal(x,self.cache_x):return
  q=torch.tensor(x,requires_grad=True);Q=self.geometry(q)[-1];pairs=self.pairs(Q.detach().numpy())
  loss=((q-torch.tensor(self.P0.ravel()))**2).sum()*self.reg/2
  for r,a,b in pairs:
   d=Q[b]-Q[a];t=torch.clamp(-(Q[a]*d).sum()/torch.clamp((d*d).sum(),min=1e-30),0.,1.);z=Q[a]+t*d;birth=(Q[r]*Q[r]).sum();loss=loss+(birth-(z*z).sum())/birth
  self.cache_x=x.copy();self.obj=float(loss.detach());self.grad=torch.autograd.grad(loss,q)[0].detach().numpy();self.active_pairs=pairs
 def objective(self,x):self.update_objective(x);return self.obj
 def gradient(self,x):self.update_objective(x);return self.grad

def main():
 root=Path(__file__).parent;raw=json.loads((root/'RESERVE31_INPUT.json').read_text());P=np.array(sorted(set(map(tuple,raw['points']))),float)/raw['denominator'];P=P[sorted(ConvexHull(P).vertices)]
 if len(sys.argv)>1:P=np.array(json.loads((root/sys.argv[1]).read_text())['P'],float)
 fs=hull(P);m=FullBar(P,fs);base=P.ravel();best=[base.copy(),m.objective(base)];history=[];start=time.monotonic()
 def callback(x):
  v=m.val(x);o=m.objective(x);entry=[len(history),float(o),float(v.min())];history.append(entry)
  if v.min()>-1e-8 and o<best[1]:best[:]=[x.copy(),o]
  if len(history)%20==0:print('FULLBAR_ITER',*entry,'best',best[1],flush=True)
 r=minimize(m.objective,base,jac=m.gradient,method='SLSQP',constraints={'type':'ineq','fun':m.val,'jac':m.jac},bounds=list(zip(base-2.,base+2.)),callback=callback,options={'maxiter':int(os.environ.get('MAXITER','100')),'ftol':1e-10,'disp':False})
 Q=best[0].reshape(-1,3);report=landscape(Q);entry=dict(success=bool(r.success),status=int(r.status),iterations=int(r.nit),best_objective=best[1],minconstraint=float(m.val(best[0]).min()),seconds=time.monotonic()-start,landscape=report,P=Q.tolist(),history=history)
 name=os.environ.get('OUT','FULLBAR_CHECKPOINT.json');(root/name).write_text(json.dumps(entry,separators=(',',':'))+'\n');print(json.dumps({k:v for k,v in entry.items() if k not in ('P','history')},indent=2),flush=True)
if __name__=='__main__':main()
```

## dynamic_fullbar.py
```python
"""Live-hull / exact-moment-formula automatic-differentiation Q full-bar search.
Every floating evaluation rebuilds the hull. No fixed-face convexity chart.
Each nonroot input point has a strict all-point escape witness at actual mass.
Root has strict negative directional derivatives to every other input point.
"""
from fullbar_geometry import *

class DynamicFull(FullBar):
 def __init__(self,P):
  super().__init__(P,hull(P));self.prepared=None;self.eps=1e-7
  self.pu=torch.tensor(list(self.pu.numpy()[:0])+[i for i in range(len(P)) if i!=self.Uroot]+[self.Uroot]*(len(P)-1))
  V,c=physics(P,hull(P));parents=[]
  for i in range(len(P)):
   if i==self.Uroot:continue
   parents.append(max([j for j in range(len(P)) if j!=i],key=lambda j:(P[i]-c)@(P[j]-P[i])/np.linalg.norm(P[j]-P[i])))
  self.pv=torch.tensor(parents+[j for j in range(len(P)) if j!=self.Uroot]);self.ps=torch.tensor([1.]*(len(P)-1)+[-1.]*(len(P)-1));self.jf=jacfwd(self.constraints_torch)
 def prepare(self,x):
  if self.prepared is not None and np.array_equal(x,self.prepared):return
  fs=hull(np.asarray(x).reshape(-1,3));self.fs=torch.tensor(fs);self.fs_np=fs;edges={}
  for f,tri in enumerate(fs):
   for a,b in zip(tri,np.roll(tri,-1)):edges.setdefault(tuple(sorted((int(a),int(b)))),[]).append(f)
  self.qedges=np.array(list(edges.values()));self.prepared=x.copy()
 def constraints_torch(self,x):
  P,a,nu,nr,v6,c,h,Q=self.geometry(x)
  e=P[self.pv]-P[self.pu];r=P[self.pu]-c
  pg=self.ps*(e*r).sum(dim=1)/torch.clamp(torch.linalg.vector_norm(e,dim=1)*torch.linalg.vector_norm(r,dim=1),min=1e-15)-self.eps
  return torch.cat([pg,(v6/6-self.V0*.2).reshape(1)])
 def val(self,x):self.prepare(x);return self.constraints_torch(torch.tensor(x)).detach().numpy()
 def jac(self,x):self.prepare(x);return self.jf(torch.tensor(x)).detach().numpy()
 def update_objective(self,x):self.prepare(x);return super().update_objective(x)

def main():
 root=Path(__file__).parent;raw=json.loads((root/'RESERVE31_INPUT.json').read_text());P=np.array(sorted(set(map(tuple,raw['points']))),float)/raw['denominator'];P=P[sorted(ConvexHull(P).vertices)]
 if len(sys.argv)>1:P=np.array(json.loads((root/sys.argv[1]).read_text())['P'],float)
 m=DynamicFull(P);base=P.ravel();best=[base.copy(),m.objective(base)];history=[];start=time.monotonic()
 def callback(x):
  v=m.val(x);o=m.objective(x);entry=[len(history),float(o),float(v.min())];history.append(entry)
  if v.min()>-1e-9 and o<best[1]:best[:]=[x.copy(),o]
  if len(history)%20==0:print('DYNAMIC_ITER',*entry,'best',best[1],flush=True)
 r=minimize(m.objective,base,jac=m.gradient,method='SLSQP',constraints={'type':'ineq','fun':m.val,'jac':m.jac},bounds=list(zip(base-2.,base+2.)),callback=callback,options={'maxiter':int(os.environ.get('MAXITER','200')),'ftol':1e-10,'disp':False})
 Q=best[0].reshape(-1,3);report=landscape(Q);entry=dict(success=bool(r.success),status=int(r.status),iterations=int(r.nit),best_objective=best[1],minconstraint=float(m.val(best[0]).min()),seconds=time.monotonic()-start,landscape=report,P=Q.tolist(),history=history)
 name=os.environ.get('OUT','DYNAMIC_CHECKPOINT.json');(root/name).write_text(json.dumps(entry,separators=(',',':'))+'\n');print(json.dumps({k:v for k,v in entry.items() if k not in ('P','history')},indent=2),flush=True)
if __name__=='__main__':main()
```
