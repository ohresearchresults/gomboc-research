# material-f7c131044e5d

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Complete free-vertex and reference-to-own filled-mass numerical methods

This material preserves three complete runnable source units actually used in the lead's free-coordinate construction experiments. These are numerical scouts, NOT exact accepted own110 constructions. The exact canonical record remains C622. The complete literal retained rational examples and a direct continuation checkpoint are preserved separately; do not infer a new object or class from a mutable output directory name or an optimizer history count.

Dependencies: `scout.py` is included completely in immutable material `[internal-source-reference]` (RADIAL_U_CONE_FILLED_MASS_METHODS.md). The original exact input ORIGINAL_G5.json is reconstructed by `[internal-source-reference]`. No additional old sandbox helper is needed. Actual environment: Python3.13.5, NumPy2.3.5, SciPy1.17.0, Torch2.10.0+cpu, NetworkX3.6.1; OPENBLAS_NUM_THREADS=1,OMP_NUM_THREADS=1. Save each block verbatim with a final newline. Source hashes below were recomputed on the preserved complete units.

## Scientific interpretation and limits

FREE_V_GLOBAL_SLP varies all physical vertex coordinates, rebuilds the convex hull, integrates the ordinary FILLED-volume centroid and recenters every accepted trial. A fixed positive physical U-flow guard is maintained while a cosine-normalized polar minimum-total-defect arborescence is improved. This changes actual geometry, unlike a free center or a density modification. The all-pair flow graph is not the quantitative true-edge bottleneck/cut certificate of GLOBAL_DIAGNOSTIC. A smaller total defect need not reduce the number of stable equilibria. The original radial helper's origin-dependent facet orientation is not used here: this file orients facets with QHull's outward equations, allowing a raw origin outside an arbitrary trial hull.

REFERENCE_MASS_FLOW instead keeps a reference110 point at the origin of the translated physical frame and varies all physical coordinates to reduce the own filled-centroid displacement while retaining positive reference S/U flows. Its input is the unchanged literal C330 translated by `(1/2,1/20,1/2)`, which has an exact reference110/weak000 certificate in the literal C330 material. Reference SU11 does not imply OWN SU11. Its original absolute L1 centroid objective has an unwanted scaling freedom: uniformly shrinking a non-centered body decreases that objective without solving the problem.

NORMALIZED_REFERENCE_MASS corrects that freedom with the differentiated objective `||c||_1/Vol(P)^(1/3)` and rescales every finite trial to the starting positive volume. The reference-flow cosine signs are scale invariant. Guards are explicit fixed inputs, not an adaptive descent toward zero. A deliberate separately stated lower guard starts a different finite continuation, not an inherited stronger-margin result. Atomic small checkpoints preserve complete raw coordinates without repeatedly rewriting growing histories.

All hull nominations, derivatives and trial acceptances in these three sources are FLOATING computations. The word 'exact' in NORMALIZED_REFERENCE_MASS's opening phrase 'exact finite hull recomputation' means recomputing the finite trial rather than using only a derivative; it does NOT mean rational exact arithmetic. Coplanar polar nominations are merged at10 decimal places and weakish thresholds come from scout.diag. The NUMERICAL_SU11 markers check only numerical S/U and are not complete strict/weak H audits. Any prospective record needs the question's independent complete exact maximal-complex audits and separate centered integration. Finite LP failure, tiny trust or an interrupted invocation is not a global geometric exclusion.

## FREE_V_GLOBAL_SLP.py

4935bytes,SHA2568be184bac0ff742b6f4914e24f14c4caba3b6cc8fa145f08b64f3717f351bd58.

```python
"""Own-filled-centroid free V-description global flow SLP.
All coordinates are live; topology is rebuilt and own mass integrated on every trial.
No accepted exact construction is asserted by this numerical scout.
S cosine-normalized arborescence cost avoids vanishing-edge radius-normalized losses.
"""
import argparse,json,pathlib,time
import numpy as np,torch,networkx as nx
from scipy.optimize import linprog
from scout import DT,mass_np,diag
from scipy.spatial import ConvexHull

def topology(v):
 h=ConvexHull(v);f=h.simplices.copy();n=np.cross(v[f[:,1]]-v[f[:,0]],v[f[:,2]]-v[f[:,0]])
 reverse=(n*h.equations[:,:3]).sum(1)<0;f[reverse]=f[reverse][:,[0,2,1]]
 return f

def geom(x,f):
 p=x.reshape(-1,3);a,b,c=p[f[:,0]],p[f[:,1]],p[f[:,2]];d=(a*torch.linalg.cross(b,c)).sum(1)
 ctr=(d[:,None]*(a+b+c)).sum(0)/(4*d.sum());p=p-ctr
 a,b,c=p[f[:,0]],p[f[:,1]],p[f[:,2]];n=torch.linalg.cross(b-a,c-a);q=n/(n*a).sum(1)[:,None]
 return p,q,ctr

def arrows(v,cosine=False):
 dv=v[None,:,:]-v[:,None,:];num=(v[:,None,:]*dv).sum(2)
 den=np.linalg.norm(v,axis=1)[:,None]*np.maximum(np.linalg.norm(dv,axis=2),1e-30) if cosine else (v*v).sum(1)[:,None]
 a=num/den;np.fill_diagonal(a,-1e6);return a

def arbo(v,guard,cosine):
 a=arrows(v,cosine);r=int(np.argmax((v*v).sum(1)));G=nx.DiGraph();G.add_nodes_from(range(len(v)))
 for i in range(len(v)):
  if i==r:continue
  for j in range(len(v)):
   if i!=j:G.add_edge(j,i,weight=max(0,guard-a[i,j])+1e-12/(1+max(a[i,j],0)))
 tr=nx.minimum_spanning_arborescence(G,attr='weight');ed=np.array([(i,j) for j,i in tr.edges()],int)
 return float(sum(max(0,guard-a[i,j]) for i,j in ed)),ed,r

def state(x):
 raw=x.reshape(-1,3);f=topology(raw);p,q,c=geom(torch.tensor(x,dtype=DT),torch.tensor(f));p=p.numpy();q=q.numpy();c=c.numpy()
 ids=np.unique(np.round(q,10),axis=0,return_index=True)[1];ids=np.sort(ids);q=q[ids]
 return dict(V=len(np.unique(f)),F=len(q),S=diag(q),U=diag(p),centroid=c.tolist()),f,ids,p,q

def run(inp,out,steps=100,trust=.01,sguard=1e-4,uguard=1e-6,cosine=True):
 o=json.load(open(inp));raw=np.array(o['points'],float)/o['grid'];raw-=mass_np(raw,topology(raw))[0];x=raw.reshape(-1);dest=pathlib.Path(out);dest.mkdir(parents=True,exist_ok=True)
 if (dest/'checkpoint.json').exists():x=np.array(json.load(open(dest/'checkpoint.json'))['raw']).reshape(-1)
 history=[];start=time.time()
 for it in range(steps):
  st,f,ids,p,q=state(x);oldloss,ed,sroot=arbo(q,sguard,cosine);up=arrows(p,False);ur=int(np.argmax((p*p).sum(1)));ui=np.array([i for i in range(len(p)) if i!=ur]);uj=np.argmax(up[ui],axis=1)
  physical_guard=np.full(len(ui),uguard);assert min(up[ui,uj])>0,st
  ft=torch.tensor(f);sid=torch.tensor(ids);ii=torch.tensor(ed[:,0]);jj=torch.tensor(ed[:,1]);uit=torch.tensor(ui);ujt=torch.tensor(uj)
  def fn(t):
   p,q,c=geom(t,ft);q=q[sid];a=q[ii];b=q[jj];dv=b-a
   den=torch.linalg.norm(a,dim=1)*torch.linalg.norm(dv,dim=1) if cosine else (a*a).sum(1)
   sf=(a*dv).sum(1)/den
   a=p[uit];b=p[ujt];uf=(a*(b-a)).sum(1)/(a*a).sum(1)
   return torch.cat([sf,uf])
  t=torch.tensor(x,dtype=DT,requires_grad=True);val=fn(t).detach().numpy();J=torch.autograd.functional.jacobian(fn,t,vectorize=True).numpy();m=len(ed);n=len(x)
  lp=linprog(np.r_[np.zeros(n),np.ones(m)],A_ub=np.vstack([np.c_[-J[:m],-np.eye(m)],np.c_[-J[m:],np.zeros((len(ui),m))]]),b_ub=np.r_[val[:m]-sguard,val[m:]-physical_guard],bounds=[(-trust,trust)]*n+[(0,None)]*m,method='highs')
  if not lp.success:print('LP_FAIL',lp.message,flush=True);break
  dx=lp.x[:n];accept=False;newloss=oldloss
  for alpha in [1.,.5,.25,.125,.0625,.03125,.015625]:
   xx=x+alpha*dx
   try:st2,f2,ids2,p2,q2=state(xx)
   except Exception:continue
   if st2['U']['count']!=1 or st2['U']['weakish']!=0:continue
   af=arrows(p2);rt=int(np.argmax((p2*p2).sum(1)));keep=np.arange(len(p2))!=rt
   if min(af.max(1)[keep])<.9*uguard:continue
   loss2,ed2,root2=arbo(q2,sguard,cosine)
   if loss2<oldloss-1e-9:
    x=(xx.reshape(-1,3)-np.array(st2['centroid'])).reshape(-1);newloss=loss2;accept=True;break
  rec=dict(iteration=it,loss=oldloss,trial_loss=newloss,accepted=accept,trust=trust,alpha=alpha,seconds=time.time()-start,**(st2 if accept else st));history.append(rec)
  print(json.dumps(rec),flush=True);json.dump(dict(raw=x.reshape(-1,3).tolist(),input=inp,sguard=sguard,uguard=uguard,cosine=cosine,history=history),open(dest/'checkpoint.json','w'),indent=2)
  if accept:trust=min(trust*1.15,.04)
  else:trust*=.5
  if trust<1e-7:break
  if rec['S']['count']==1 and rec['S']['weakish']==0:print('NUMERICAL_SU11_REQUIRES_EXACT_AUDIT',flush=True);break
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--input',default='ORIGINAL_G5.json');a.add_argument('--out',default='freev');a.add_argument('--steps',type=int,default=100);a.add_argument('--trust',type=float,default=.01);a.add_argument('--radius-normalized',action='store_true');p=a.parse_args();run(p.input,p.out,p.steps,p.trust,cosine=not p.radius_normalized)
```

## REFERENCE_MASS_FLOW.py

4612bytes,SHA256ba61d4cf300e40a181364be232a176750d1987dba50c91602418f4183badf993.

```python
"""Numerical free-vertex filled-mass closure inside reference S1/U1 flow chambers.
Start from literal C330 and exact rational reference110 (1/2,1/20,1/2).
All geometry is physical; no density change. Complete exact audit is still required.
"""
import argparse,json,pathlib,time
import numpy as np,torch
from scipy.optimize import linprog
from scipy.spatial import ConvexHull
from scout import DT,mass_np,diag
from FREE_V_GLOBAL_SLP import topology,arrows

def geom(x,f):
 p=x.reshape(-1,3);a,b,c=p[f[:,0]],p[f[:,1]],p[f[:,2]];d=(a*torch.linalg.cross(b,c)).sum(1)
 ctr=(d[:,None]*(a+b+c)).sum(0)/(4*d.sum());n=torch.linalg.cross(b-a,c-a);q=n/(n*a).sum(1)[:,None]
 return p,q,ctr

def get(x):
 raw=x.reshape(-1,3);h=ConvexHull(raw)
 if max(h.equations[:,-1])>=-1e-8:raise ValueError('reference not interior')
 f=topology(raw);p,q,c=geom(torch.tensor(x,dtype=DT),torch.tensor(f));p,q,c=p.numpy(),q.numpy(),c.numpy()
 ids=np.sort(np.unique(np.round(q,10),axis=0,return_index=True)[1]);q=q[ids]
 ownp=p-c;a,b,cc=ownp[f[:,0]],ownp[f[:,1]],ownp[f[:,2]];ns=np.cross(b-a,cc-a);ownq=ns/(ns*a).sum(1)[:,None];ownids=np.sort(np.unique(np.round(ownq,10),axis=0,return_index=True)[1])
 st=dict(V=len(np.unique(f)),F=len(q),reference_S=diag(q),reference_U=diag(p),own_S=diag(ownq[ownids]),own_U=diag(ownp),centroid=c.tolist(),center_l1=float(sum(abs(c))))
 return st,f,ids,p,q,c

def pol(v):
 a=arrows(v,True);r=int(np.argmax((v*v).sum(1)));ii=np.array([i for i in range(len(v)) if i!=r]);jj=np.argmax(a[ii],axis=1);return ii,jj,a[ii,jj]

def run(inp,out,steps=200,trust=.01,guardfraction=.05):
 o=json.load(open(inp));raw=np.array(o['points'],float)/o['grid']-np.array([.5,.05,.5]);x=raw.reshape(-1);dest=pathlib.Path(out);dest.mkdir(parents=True,exist_ok=True)
 st,f,ids,p,q,c=get(x);sg=min(1e-3,guardfraction*min(pol(q)[2]));ug=min(1e-3,guardfraction*min(pol(p)[2]));assert min(sg,ug)>0
 history=[]
 if (dest/'checkpoint.json').exists():
  checkpoint=json.load(open(dest/'checkpoint.json'));x=np.array(checkpoint['raw']).reshape(-1);history=checkpoint.get('history',[])
 offset=len(history);start=time.time()
 for it in range(steps):
  st,f,ids,p,q,c=get(x);si,sj,_=pol(q);ui,uj,_=pol(p);ft=torch.tensor(f);sid=torch.tensor(ids);sit=torch.tensor(si);sjt=torch.tensor(sj);uit=torch.tensor(ui);ujt=torch.tensor(uj)
  def fn(t):
   p,q,c=geom(t,ft);q=q[sid]
   def fl(a,b):dv=b-a;return (a*dv).sum(1)/(torch.linalg.norm(a,dim=1)*torch.linalg.norm(dv,dim=1))
   return torch.cat([c,fl(q[sit],q[sjt]),fl(p[uit],p[ujt])])
  t=torch.tensor(x,dtype=DT,requires_grad=True);v=fn(t).detach().numpy();J=torch.autograd.functional.jacobian(fn,t,vectorize=True).numpy();n=len(x);m=len(v)-3;guards=np.r_[np.full(len(si),sg),np.full(len(ui),ug)]
  # dx[n], three absolute centroid residuals, n absolute displacement slacks.
  cost=np.r_[np.zeros(n),np.ones(3),np.full(n,1e-6)]
  Z=np.zeros((m,3+n));A=np.vstack([np.c_[-J[3:],Z],np.c_[J[:3],-np.eye(3),np.zeros((3,n))],np.c_[-J[:3],-np.eye(3),np.zeros((3,n))],np.c_[np.eye(n),np.zeros((n,3)),-np.eye(n)],np.c_[-np.eye(n),np.zeros((n,3)),-np.eye(n)]])
  b=np.r_[v[3:]-guards,-v[:3],v[:3],np.zeros(2*n)]
  lp=linprog(cost,A_ub=A,b_ub=b,bounds=[(-trust,trust)]*n+[(0,None)]*(3+n),method='highs')
  if not lp.success:print('LP_FAIL',lp.message,flush=True);break
  accept=False;dx=lp.x[:n]
  for alpha in [1.,.5,.25,.125,.0625,.03125,.015625,.0078125]:
   xx=x+alpha*dx
   try:st2,f2,ids2,p2,q2,c2=get(xx)
   except Exception:continue
   if min(pol(q2)[2])<.9*sg or min(pol(p2)[2])<.9*ug:continue
   if st2['center_l1']<st['center_l1']-1e-10:x=xx;accept=True;break
  rec=dict(iteration=offset+it,accepted=accept,trust=trust,alpha=alpha,sguard=sg,uguard=ug,seconds=time.time()-start,**(st2 if accept else st));history.append(rec);print(json.dumps(rec),flush=True)
  json.dump(dict(raw=x.reshape(-1,3).tolist(),source_input=inp,reference=[.5,.05,.5],sguard=sg,uguard=ug,guardfraction=guardfraction,history=history),open(dest/'checkpoint.json','w'),indent=2)
  if accept:trust=min(.03,trust*1.12)
  else:trust*=.5
  if trust<1e-8:break
  if rec['own_S']['count']==1 and rec['own_U']['count']==1 and rec['own_S']['weakish']==0 and rec['own_U']['weakish']==0:print('NUMERICAL_OWN_SU11_REQUIRES_EXACT_AUDIT',flush=True);break
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--input',default='ORIGINAL_G5.json');a.add_argument('--out',default='reference_mass');a.add_argument('--steps',type=int,default=200);a.add_argument('--trust',type=float,default=.01);a.add_argument('--guardfraction',type=float,default=.05);p=a.parse_args();run(p.input,p.out,p.steps,p.trust,p.guardfraction)
```

## NORMALIZED_REFERENCE_MASS.py

4300bytes,SHA256db5961030e1c17986b1e1333af38878f070edc6136195a35e8205a92cd4eaa03.

```python
"""Actual filled-mass continuation in positive reference S/U flow chambers.
Volume-normalized objective and exact finite hull recomputation at every trial.
Numerical only: a SU11 marker needs complete independent exact own-centroid audits.
This file resumes a literal raw-point checkpoint and saves atomic small checkpoints.
"""
import argparse,json,pathlib,time
import numpy as np,torch
from scipy.optimize import linprog
from REFERENCE_MASS_FLOW import get,pol,geom
from FREE_V_GLOBAL_SLP import topology
from scout import DT,mass_np

def run(input_path,out,steps=300,trust=.01,sguard=.001,uguard=.001):
 dest=pathlib.Path(out);dest.mkdir(parents=True,exist_ok=True)
 source=json.load(open(input_path));raw=np.asarray(source['raw'],dtype=float);x=raw.reshape(-1)
 vtarget=float(mass_np(raw,topology(raw))[1]);assert vtarget>0
 step_offset=0
 if (dest/'checkpoint.json').exists():
  o=json.load(open(dest/'checkpoint.json'));x=np.asarray(o['raw'],float).reshape(-1);vtarget=o['volume_target'];step_offset=o['completed_steps']
 st,f,ids,p,q,c=get(x);scale0=vtarget**(1/3);start=time.time()
 for it in range(steps):
  st,f,ids,p,q,c=get(x);si,sj,_=pol(q);ui,uj,_=pol(p)
  ft=torch.tensor(f);sid=torch.tensor(ids);sit=torch.tensor(si);sjt=torch.tensor(sj);uit=torch.tensor(ui);ujt=torch.tensor(uj)
  def fn(t):
   p,q,c=geom(t,ft);q=q[sid];a,b,z=p[ft[:,0]],p[ft[:,1]],p[ft[:,2]];volume=(a*torch.linalg.cross(b,z)).sum()/6
   def fl(a,b):dv=b-a;return (a*dv).sum(1)/(torch.linalg.norm(a,dim=1)*torch.linalg.norm(dv,dim=1))
   return torch.cat([c/volume.pow(1/3),fl(q[sit],q[sjt]),fl(p[uit],p[ujt])])
  t=torch.tensor(x,dtype=DT,requires_grad=True);val=fn(t).detach().numpy();J=torch.autograd.functional.jacobian(fn,t,vectorize=True).numpy()
  n=len(x);m=len(val)-3;guards=np.r_[np.full(len(si),sguard),np.full(len(ui),uguard)]
  obj=np.r_[np.zeros(n),np.ones(3),np.full(n,1e-6/scale0)]
  A=np.vstack([np.c_[-J[3:],np.zeros((m,3+n))],np.c_[J[:3],-np.eye(3),np.zeros((3,n))],np.c_[-J[:3],-np.eye(3),np.zeros((3,n))],np.c_[np.eye(n),np.zeros((n,3)),-np.eye(n)],np.c_[-np.eye(n),np.zeros((n,3)),-np.eye(n)]])
  b=np.r_[val[3:]-guards,-val[:3],val[:3],np.zeros(2*n)]
  lp=linprog(obj,A_ub=A,b_ub=b,bounds=[(-trust*scale0,trust*scale0)]*n+[(0,None)]*(3+n),method='highs')
  if not lp.success:print('NORMALIZED_LP_FAIL',lp.message,flush=True);break
  oldscore=float(abs(val[:3]).sum());accepted=False;dx=lp.x[:n]
  for alpha in [1.,.5,.25,.125,.0625,.03125,.015625,.0078125,.00390625]:
   xx=x+alpha*dx
   try:
    trial=xx.reshape(-1,3);ctr,vol=mass_np(trial,topology(trial));assert vol>0
    xx*= (vtarget/vol)**(1/3)
    st2,f2,ids2,p2,q2,c2=get(xx)
    smin=float(min(pol(q2)[2]));umin=float(min(pol(p2)[2]))
   except Exception:continue
   if smin<.9*sguard or umin<.9*uguard:continue
   score2=float(abs(c2).sum()/scale0)
   if score2<oldscore-1e-10:x=xx;accepted=True;break
  rec=dict(step=step_offset+it,accepted=accepted,trust=trust,alpha=alpha,normalized_center_l1=score2 if accepted else oldscore,reference_s_min_cos=smin if accepted else float(min(pol(q)[2])),reference_u_min_cos=umin if accepted else float(min(pol(p)[2])),seconds=time.time()-start,**(st2 if accepted else st))
  print(json.dumps(rec),flush=True)
  with open(dest/'history.jsonl','a') as fh:fh.write(json.dumps(rec)+'\n')
  payload=dict(raw=x.reshape(-1,3).tolist(),volume_target=vtarget,sguard=sguard,uguard=uguard,completed_steps=step_offset+it+1,last_record=rec,source_input=input_path)
  tmp=dest/'checkpoint.tmp';tmp.write_text(json.dumps(payload,separators=(',',':')));tmp.replace(dest/'checkpoint.json')
  if accepted:trust=min(.03,trust*1.12)
  else:trust*=.5
  if trust<1e-8:break
  if rec['own_S']['count']==1 and rec['own_U']['count']==1 and rec['own_S']['weakish']==0 and rec['own_U']['weakish']==0:
   print('NUMERICAL_OWN_SU11_REQUIRES_EXACT_AUDIT',flush=True);break
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--input',default='REFERENCE_MASS_POST2427_RAW.json');ap.add_argument('--out',default='normalized_mass');ap.add_argument('--steps',type=int,default=300);ap.add_argument('--trust',type=float,default=.01);ap.add_argument('--sguard',type=float,default=.001);ap.add_argument('--uguard',type=float,default=.001);a=ap.parse_args();run(a.input,a.out,a.steps,a.trust,a.sguard,a.uguard)
```

## Finite replay and continuation commands

Recover ORIGINAL_G5.json from [internal-source-reference], save scout.py from [internal-source-reference] and the three blocks here. In distinct clean output directories:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python FREE_V_GLOBAL_SLP.py --input ORIGINAL_G5.json --out freev_fresh --steps 100 --trust .01
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python REFERENCE_MASS_FLOW.py --input ORIGINAL_G5.json --out reference_mass_fresh --steps 200 --trust .01 --guardfraction .05
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python NORMALIZED_REFERENCE_MASS.py --input MASS_CHAMBER46_CD5E.json --out mass_continuation_fresh --steps 100 --trust .01 --sguard .0001 --uguard .0001
```

The last command uses the entire explicit46-point continuation checkpoint preserved in the companion literal material, NOT a similarly named historical directory. These commands specify finite research searches, not promises of bit-identical optimizer trajectories on other library/platform versions. Source/source-input hashes identify the exact starting evidence. The companion literal rational G6/G8 geometries are independently reconstructible without rerunning any optimizer. Geometry candidates remain numerical until exact auditing; ordinary successful termination is not an own110 certificate.
