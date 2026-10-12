# material-8a4d778ae556

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Complete own-centroid H-description and global-tree numerical methods

This material preserves the COMPLETE runnable source nucleus materially used to produce the exact C402 and C378_GLOBAL65 nonwinners, and the later minimum-defect continuation. It is numerical research evidence, NOT an acceptance auditor. Every retained exact geometry is defined by its complete literal rational input and separately checked by independent A/B/mass and exact tree/cut predicates.

## Inputs, dependencies and environment

The exact starting checkpoints are independently recoverable from [internal-source-reference] (C288 and its two C330 dependencies), [internal-source-reference] (C402 and exact auditor dependency), and [internal-source-reference] (C378_GLOBAL65_G9 and its stated auditor/verifier dependencies). Use their actual RAW.json as input; a physical H-description is NOT a point hull. All helpers used by these numerical files are included below. No old sandbox, worker download, hidden archive or unspecified code is required.

Environment actually used: CPython3.13.5, NumPy2.3.5, SciPy1.17.0, Torch2.10.0+cpu, NetworkX3.6.1. OPENBLAS_NUM_THREADS=1, OMP_NUM_THREADS=1, Torch one thread and float64. Every source block includes its final newline. Source identities:
H_NO_SADDLE.py5687bytes SHA256 c9f07e030923d0682dc1527ae2c378c05fdae9ecc54424f68790f95be18ed91f;
GLOBAL_DIAGNOSTIC.py1722bytes SHA256 81edb4dfd58385659139bab3fcf99454e5c3e0a8d6959e0663d11ecea68a1d68;
H_GLOBAL_SLP.py4677bytes SHA256 13dd1f459fd8ae1d79924b26bccf6a09dc1fb1e18ccbb69f91f581a67d3ab2aa;
H_GLOBAL_SLP_FIXED_MARGIN.py4659bytes SHA256 913dcfa482852515bbbbda56a4725dcf5e447a092ba5ffff2dc473c2a4ad273a;
H_GLOBAL_SUM_SLP.py4715bytes SHA256 9014da928ac611068695475487153c3f4b98613d3fef3287115aef3f11241493.

## Producing commands and finite observations

From C288: `python H_NO_SADDLE.py C288/RAW.json h_no0.json --steps 5000 --trust .5 --margin .0001 --uweight 1000 --vfloor .5 --seed 20260919 --jitter 0` completed1104 evaluations, numerical own312. Then `python H_NO_SADDLE.py h_no0.json h_no0_u10.json --steps 5000 --trust .5 --margin .001 --uweight 10 --vfloor .5 --seed 20260919 --jitter 0` completed531 evaluations, own413. A fixed-margin global run from that checkpoint with steps1000,trust.0001,maxtrust.05,trustfloor1e-10,physical-margin1e-6,goal1e-5,backtracks20 was interrupted by the200-second container timeout after at least371 accepted steps; do not call1000 complete or deterministic wall-clock replay. Its69 active vectors, rounded to grid10^9, define the separately preserved C402.

The fully completed and more useful subsequent chain starts from exact C402:
`python H_NO_SADDLE.py C402/RAW.json c402_condition.json --steps 5000 --trust .02 --margin .001 --uweight 1000 --vfloor .5 --seed 20260919 --jitter 0` used5441 evaluations and gave numerical own413, physical beta .0009978539 and polar beta -.5185981515. This deliberately sacrifices polar margin to restore physical room.

Then execute H_GLOBAL_SLP_FIXED_MARGIN.py in FIVE50-step blocks. Every block uses maxtrust.05,trustfloor1e-10,physical-margin.0001,goal1e-5,backtracks20. Inputs/outputs/trust values: c402_condition.json -> slp_condition50.json/.0001; 50 ->100/.001;100->150/.001;150->200/.002;200->250/.0015. Observed polar betas respectively -.348921657,-.249716883,-.199498493,-.173426310,-.158987203; physical betas remain positive. Last numerical own[17,1,16], V126/E189/F65. Its65 active vectors rounded ties-to-even to grid10^9 yield the exact C378_GLOBAL65_G9, whose exact global interval is(-.158988,-.158986) and physical beta>1/20000. The exact input, not rerun floating optimization, defines that body.

The total-defect alternative uses H_GLOBAL_SUM_SLP.py, margin1e-5,maxtrust.01,trustfloor1e-10,allowed-drop.01,backtracks20. From slp_condition250 use three25-step blocks, each trust.001 and physical-margin.0001. They reduce numerical S from17 to13,10,6 while worsening polar beta to about-.30953. A fourth25-step block with trust.0001,physical-margin1e-5 yields only microscopic changes. Active-support pruning and grid10^7 rounding of that checkpoint, followed by two25-step blocks with physical-margin1e-5 and trust.0001 then.0003, yield numerical own514 then413, the latter V124/E186/F64, physical beta about3.055e-6, polar beta about-.297765. These later endpoints are NOT exactified in this material. They remain numerical observations, not durable exact successors or own110 claims.

The JSON reports include full options, input SHA, accepted-step history and actual argument strings. Their elapsed-time/path fields preclude an environment-independent byte-identical transcript guarantee. Exact geometry capsules pin all accepted coordinate bytes and generated audit hashes separately.

## Limitations that change interpretation

Floating geometry deduplicates vertices at9 decimal places and nominates support owners by nearest reconstructed plane. Thin or almost-coplanar contacts may alter numerical topology; the exact maximal-complex auditors decide final V/E/F. No local loss or reported E is an acceptance certificate. Root identities are recomputed from the current filled centroid rather than frozen to the old apex.

The original SLP adapts its physical floor downward and can converge toward zero physical reserve; that version was not accepted as robust progress. The exact two-line fixed-margin patch below corrects this acceptance policy. A remaining numerical limitation is restoration infeasibility: accepted beta may be below the LP target floor, and very small trust can make the next LP infeasible. Its unsuccessful-LP `continue` bypasses the later trustfloor check, so a finite run can spend its remaining iterations shrinking trust; this is not a geometric exclusion. No scheduler or source revision is silently inferred from those messages.

The minimum-total-defect arborescence reduces the sum of negative arrows, not the maximum bottleneck. Its combinatorial cost can jump when near-coincident facets become adjacent after tiny rounding; it is not a continuous geometric distance to own110. The permitted .01 beta drop is per accepted step, not a global limit. All finite failures leave the support family open.

<!-- FILE H_NO_SADDLE.py -->
```python
"""Root-free own-centroid shape optimization in a complete H-description.
All supports move independently; only actual inter-facet edges enter the saddle
objective. Interior/redundant supports and contact transitions are permitted.
Numerical only: floating contacts are never an acceptance certificate.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,sys,json,time,hashlib
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import minimize
import torch
torch.set_num_threads(1);torch.set_default_dtype(torch.float64)

def geometry(Y):
 q=ConvexHull(Y)
 if q.equations[:,3].max()>=-1e-8:raise ValueError('unbounded')
 P=-q.equations[:,:3]/q.equations[:,3,None];_,unique=np.unique(np.round(P,9),axis=0,return_index=True);P=P[unique];td=q.simplices[unique]
 h=ConvexHull(P);tr=h.simplices.copy();flip=np.einsum('ij,ij->i',np.cross(P[tr[:,1]]-P[tr[:,0]],P[tr[:,2]]-P[tr[:,0]]),h.equations[:,:3])<0;tr[flip]=tr[flip][:,[0,2,1]]
 nom=-h.equations[:,:3]/h.equations[:,3,None];dist=((nom[:,None,:]-Y[None,:,:])**2).sum(2);labels=dist.argmin(1)
 edge={}
 for k,(i,j,l) in enumerate(tr):
  for a,b in ((i,j),(j,l),(l,i)):edge.setdefault(tuple(sorted((int(a),int(b)))),[]).append((int(labels[k]),int(a),int(b)))
 E=[]
 for (i,j),pair in sorted(edge.items()):
  assert len(pair)==2 and pair[0][1:]==pair[1][1:][::-1]
  if pair[0][0]!=pair[1][0]:E.append([i,j,pair[0][0],pair[1][0],pair[0][1],pair[0][2]])
 return td,tr,np.asarray(E),h.vertices,np.unique(labels)

def evaluate(Y):
 td,tr,e,active,facets=geometry(Y.detach().numpy());P=torch.linalg.solve(Y[td],torch.ones((len(td),3)));base=P.mean(0);t=P[tr]-base;v6=(t[:,0]*torch.linalg.cross(t[:,1],t[:,2])).sum(1);vol=v6.sum()/6;g=base+(v6[:,None]*t.sum(1)).sum(0)/(4*v6.sum());X=P-g
 i,j,f,h,a,b=[e[:,k] for k in range(6)];n=Y/torch.linalg.vector_norm(Y,dim=1)[:,None];r=torch.linalg.vector_norm(X,dim=1);d=X[j]-X[i];dl=torch.linalg.vector_norm(d,dim=1);da=X[b]-X[a];dal=torch.linalg.vector_norm(da,dim=1)
 forms=torch.stack((-(X[i]*d).sum(1)/(r[i]*dl),(X[j]*d).sum(1)/(r[j]*dl),(n[f]*torch.linalg.cross(X[a],da)).sum(1)/(r[a]*dal),(n[h]*torch.linalg.cross(X[b],-da)).sum(1)/(r[b]*dal)),1)
 targets=torch.tensor(np.concatenate((e[:,0],e[:,1])),dtype=torch.long);vals=torch.cat((forms[:,0],forms[:,1]));u=torch.full((len(X),),100.).scatter_reduce(0,targets,vals,reduce='amin',include_self=True)
 return forms,u,g,vol,X,Y[facets]/(1-Y[facets]@g)[:,None],active,e

def report(y):
 with torch.no_grad():
  forms,u,g,V,X,Z,active,e=evaluate(torch.tensor(y));rr=Z.square().sum(1);D=Z@Z.T-rr[:,None];D-=torch.eye(len(Z))*1e6
  s=int((D.max(1).values<0).sum());v=int((u[active]>0).sum());hh=int((forms.min(1).values>0).sum())
 return dict(VEF=[len(active),len(e),len(Z)],SUH=[s,v,hh],centroid=g.tolist(),volume=V.item(),worst_saddle=forms.min(1).values.max().item(),points=(X+g).tolist())

def run(a):
 inp=Path(a.input);cfg=json.loads(inp.read_text())
 if 'H' in cfg:
  h=np.asarray(cfg['H'],float);initial=h[:,:3]/h[:,3,None]
 else:initial=np.asarray(cfg['polar_points'],float)
 if a.jitter:initial+=np.random.default_rng(a.seed).normal(0,a.jitter,initial.shape)
 # all raw support vectors are bounded locally; convex-hull failure receives a large finite penalty
 shape=initial.shape;calls=0;best=None;history=[];start=time.time()
 def fun(flat):
  nonlocal calls,best
  yy=flat.reshape(shape);z=torch.tensor(yy,requires_grad=True)
  try:ff,u,g,V,X,Z,act,e=evaluate(z)
  except (ValueError,RuntimeError,AssertionError):return 1e5+float(((yy-initial)**2).sum()),(2*(yy-initial)).ravel()
  root=int(X.detach().square().sum(1).argmax());ix=[int(i) for i in act if i!=root]
  lh=torch.relu(ff.min(1).values+a.margin).square().sum();lu=torch.relu(u[ix]+a.margin).square().sum()
  # Volume/RMS bounds oppose flattening; no old stable or unstable carrier is fixed.
  size=X.square().sum(1).mean();lv=torch.relu(a.vfloor-V/size**1.5).square()
  obj=lh+a.uweight*lu+lv;obj.backward();val=obj.item();calls+=1
  if best is None or val<best[0]:
   best=(val,yy.copy())
   if calls%100==0 or val<1e-18:
    r=report(yy);history.append(dict(call=calls,loss=val,**{k:v for k,v in r.items() if k!='points'}));save(yy,r);print(calls,val,r['VEF'],r['SUH'],flush=True)
  return val,z.grad.numpy().ravel()
 def save(yy,r):Path(a.output).write_text(json.dumps(dict(polar_points=yy.tolist(),grid=1,numerical_only=True,summary={k:v for k,v in r.items() if k!='points'},points=r['points']),sort_keys=True,separators=(',',':')))
 opts=dict(maxiter=a.steps,maxfun=20*a.steps,ftol=1e-23,gtol=1e-12,maxls=40,maxcor=30);res=minimize(fun,initial.ravel(),jac=True,method='L-BFGS-B',bounds=list(zip((initial-a.trust).ravel(),(initial+a.trust).ravel())),options=opts)
 r=report(best[1]);save(best[1],r);Path(a.output+'.report.json').write_text(json.dumps(dict(arguments=vars(a),input_sha256=hashlib.sha256(inp.read_bytes()).hexdigest(),calls=calls,best_loss=best[0],history=history,options=opts,status=int(res.status),message=str(res.message),elapsed=time.time()-start),sort_keys=True,separators=(',',':')));print('H_NO_SADDLE_NUMERICAL_ONLY',calls,best[0],{k:v for k,v in r.items() if k!='points'},flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('output');p.add_argument('--steps',type=int,default=5000);p.add_argument('--trust',type=float,default=.5);p.add_argument('--margin',type=float,default=1e-4);p.add_argument('--uweight',type=float,default=1000);p.add_argument('--vfloor',type=float,default=.5);p.add_argument('--seed',type=int,default=20260919);p.add_argument('--jitter',type=float,default=0);run(p.parse_args())
```

<!-- FILE GLOBAL_DIAGNOSTIC.py -->
```python
"""Numerical true-edge maximum-bottleneck trees; no exact certificate is asserted."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import json,sys,heapq
from pathlib import Path
import numpy as np
import torch
from H_NO_SADDLE import geometry,evaluate

def bottleneck(X,edges):
 root=int((X*X).sum(1).argmax());adj=[[] for _ in X]
 for i,j in edges:
  if i==j:continue
  d=X[j]-X[i];norm=np.linalg.norm(d)
  if norm<1e-13:continue
  adj[i].append((j,float(X[i]@d/(np.linalg.norm(X[i])*norm))));adj[j].append((i,float(-X[j]@d/(np.linalg.norm(X[j])*norm))))
 b=np.full(len(X),-np.inf);b[root]=np.inf;parent=np.full(len(X),-1);parent[root]=root;heap=[(-np.inf,root)]
 while heap:
  v,j=heapq.heappop(heap);v=-v
  if v<b[j]:continue
  for i,_ in adj[j]:
   w=next(w for k,w in adj[i] if k==j);c=min(v,w)
   if c>b[i]:b[i]=c;parent[i]=j;heapq.heappush(heap,(-c,i))
 return dict(beta=float(np.delete(b,root).min()),root=root,parent=parent.tolist())

def get(cfg):
 if 'H' in cfg:
  H=np.asarray(cfg['H'],float);Y=H[:,:3]/H[:,3,None]
 else:Y=np.array(cfg['polar_points'])
 td,tr,e,act,fac=geometry(Y)
 with torch.no_grad():ff,u,g,vol,X,Z,act,e=evaluate(torch.tensor(Y));X=X.numpy();Z=Z.numpy()
 fm={int(j):i for i,j in enumerate(fac)};de=[(fm[f],fm[h]) for f,h in e[:,2:4]]
 return dict(physical=bottleneck(X,e[:,:2]),polar=bottleneck(Z,de),VEF=[len(act),len(e),len(fac)],centroid=g.tolist())
if __name__=='__main__':
 cfg=json.loads(Path(sys.argv[1]).read_text());r=get(cfg);print(json.dumps({k:{a:b for a,b in v.items() if a!='parent'} if isinstance(v,dict) else v for k,v in r.items()}))
 if len(sys.argv)>2:Path(sys.argv[2]).write_text(json.dumps(r,sort_keys=True,separators=(',',':')))
```

<!-- FILE H_GLOBAL_SLP.py -->
```python
"""Sequential linear optimization of the global dual tree with a positive physical tree.
Every accepted step rebuilds the true hull and recomputes the ordinary filled centroid.
Numerical only. A failed finite run is not an exclusion of the support family.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,json,sys,hashlib,time
from pathlib import Path
import numpy as np
import torch
from scipy.optimize import linprog
from H_NO_SADDLE import geometry,evaluate,report
from GLOBAL_DIAGNOSTIC import bottleneck

def structure(y):
 td,tr,e,active,fac=geometry(y);fm={int(j):i for i,j in enumerate(fac)};de=[(fm[f],fm[h]) for f,h in e[:,2:4]]
 with torch.no_grad():ff,u,g,V,X,Z,active,e=evaluate(torch.tensor(y))
 p=bottleneck(X.numpy(),e[:,:2]);q=bottleneck(Z.numpy(),de)
 return (td,tr,e,active,fac),p,q

def arrows_fixed(Y,struct,p,q):
 td,tr,e,active,fac=struct;P=torch.linalg.solve(Y[td],torch.ones((len(td),3)));base=P.mean(0);t=P[tr]-base;v6=(t[:,0]*torch.linalg.cross(t[:,1],t[:,2])).sum(1);g=base+(v6[:,None]*t.sum(1)).sum(0)/(4*v6.sum());X=P-g;Z=Y[fac]/(1-Y[fac]@g)[:,None]
 def ar(X,parent):
  ix=[i for i in range(len(X)) if i!=parent['root']];jx=[parent['parent'][i] for i in ix];d=X[jx]-X[ix]
  return (X[ix]*d).sum(1)/(torch.linalg.vector_norm(X[ix],dim=1)*torch.linalg.vector_norm(d,dim=1))
 return torch.cat((ar(X,p),ar(Z,q)))

def run(a):
 inp=Path(a.input);cfg=json.loads(inp.read_text())
 if 'H' in cfg:
  H=np.asarray(cfg['H'],float);y=H[:,:3]/H[:,3,None]
 else:y=np.asarray(cfg['polar_points'],float)
 trust=a.trust;hist=[];accepted=0;start=time.time();initial=y.copy();bestbeta=-np.inf
 def save(st,p,q):
  rr=report(y);Path(a.output).write_text(json.dumps(dict(polar_points=y.tolist(),grid=1,numerical_only=True,summary={k:v for k,v in rr.items() if k!='points'},points=rr['points'],trees=dict(physical=p,polar=q)),sort_keys=True,separators=(',',':')))
 for k in range(a.steps):
  st,p,q=structure(y);nphys=len(p['parent'])-1;npole=len(q['parent'])-1
  if q['beta']>bestbeta:bestbeta=q['beta'];save(st,p,q)
  if p['beta']<=0:raise ValueError('initial/current physical tree is not positive')
  if q['beta']>a.goal:print('NUMERICAL_POSITIVE_BOTH_TREES',flush=True);break
  Y=torch.tensor(y,requires_grad=True);fn=lambda x:arrows_fixed(x,st,p,q);vals=fn(Y).detach().numpy();jac=torch.autograd.functional.jacobian(fn,Y,vectorize=True).detach().numpy().reshape(len(vals),-1);jp,jq=jac[:nphys],jac[nphys:];vp,vq=vals[:nphys],vals[nphys:];D=y.size
  floor=np.minimum(vp*.5,a.physical_margin);Ap=np.column_stack((-jp,np.zeros(nphys)));Aq=np.column_stack((-jq,np.ones(npole)));A=np.vstack((Ap,Aq));b=np.concatenate((vp-floor,vq));cost=np.zeros(D+1);cost[-1]=-1
  sol=linprog(cost,A_ub=A,b_ub=b,bounds=[(-trust,trust)]*D+[(q['beta'],1.)],method='highs')
  if not sol.success:trust*=.5;hist.append(dict(iteration=k,trust=trust,lp_status=int(sol.status),physical=p['beta'],polar=q['beta']));continue
  step=sol.x[:D].reshape(y.shape);accepted_step=False;candidate=None
  for j in range(a.backtracks):
   yy=y+(2.**(-j))*step
   try:sts,ps,qs=structure(yy)
   except (ValueError,RuntimeError,AssertionError):continue
   if ps['beta']>=min(a.physical_margin/4,p['beta']/4) and qs['beta']>q['beta']+1e-12:
    candidate=(yy,sts,ps,qs,j);accepted_step=True;break
  if accepted_step:
   y,sts,ps,qs,j=candidate;accepted+=1;trust=min(a.maxtrust,trust*(1.15 if j==0 else .9));r=dict(iteration=k,accepted=accepted,trust=trust,backtrack=j,physical=ps['beta'],polar=qs['beta'],lp_prediction=float(sol.x[-1]));hist.append(r)
   if k%10==0:save(sts,ps,qs);print(r,flush=True)
  else:trust*=.5;hist.append(dict(iteration=k,trust=trust,rejected=True,physical=p['beta'],polar=q['beta']))
  if trust<a.trustfloor:print('TRUST_FLOOR',flush=True);break
 st,p,q=structure(y);save(st,p,q);rr=report(y);Path(a.output+'.report.json').write_text(json.dumps(dict(arguments=vars(a),input_sha256=hashlib.sha256(inp.read_bytes()).hexdigest(),accepted=accepted,history=hist,elapsed=time.time()-start),sort_keys=True,separators=(',',':')));print('H_GLOBAL_SLP_FINITE_END',accepted,p['beta'],q['beta'],{k:v for k,v in rr.items() if k!='points'},flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('output');p.add_argument('--steps',type=int,default=600);p.add_argument('--trust',type=float,default=.001);p.add_argument('--maxtrust',type=float,default=.05);p.add_argument('--trustfloor',type=float,default=1e-10);p.add_argument('--physical-margin',type=float,default=1e-6);p.add_argument('--goal',type=float,default=1e-5);p.add_argument('--backtracks',type=int,default=20);run(p.parse_args())
```

### Exact patch producing H_GLOBAL_SLP_FIXED_MARGIN.py
```python
from pathlib import Path
import hashlib
p=Path('H_GLOBAL_SLP.py').read_bytes();assert hashlib.sha256(p).hexdigest()=='13dd1f459fd8ae1d79924b26bccf6a09dc1fb1e18ccbb69f91f581a67d3ab2aa'
s=p.decode();old='floor=np.minimum(vp*.5,a.physical_margin)';assert s.count(old)==1;s=s.replace(old,'floor=np.full_like(vp,a.physical_margin)');old="ps['beta']>=min(a.physical_margin/4,p['beta']/4)";assert s.count(old)==1;s=s.replace(old,"ps['beta']>=a.physical_margin/4");b=s.encode();assert len(b)==4659 and hashlib.sha256(b).hexdigest()=='913dcfa482852515bbbbda56a4725dcf5e447a092ba5ffff2dc473c2a4ad273a';Path('H_GLOBAL_SLP_FIXED_MARGIN.py').write_bytes(b)
```

<!-- FILE H_GLOBAL_SUM_SLP.py -->
```python
"""Whole-support own-centroid sequential LP using minimum-defect arborescences.
Rootward trees minimize the SUM of negative polar arrow deficits, rather than
only the worst bottleneck. Every accepted step recomputes true hull and mass.
Finite numerical method, not an exact certificate or a family exclusion.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,json,sys,time,hashlib
from pathlib import Path
import numpy as np
import torch
import networkx as nx
from scipy.optimize import linprog
from H_NO_SADDLE import geometry,evaluate,report
from GLOBAL_DIAGNOSTIC import bottleneck
from H_GLOBAL_SLP import arrows_fixed

def state(y,margin):
 st=geometry(y);td,tr,e,active,fac=st;fm={int(j):i for i,j in enumerate(fac)};de={tuple(sorted((fm[f],fm[h]))) for f,h in e[:,2:4]}
 with torch.no_grad():ff,u,g,V,X,Z,act,ee=evaluate(torch.tensor(y));X=X.numpy();Z=Z.numpy()
 p=bottleneck(X,e[:,:2]);globalq=bottleneck(Z,de);root=globalq['root'];G=nx.DiGraph();G.add_nodes_from(range(len(Z)))
 for i,j in de:
  for v,w in [(i,j),(j,i)]:
   if v==root:continue
   d=Z[w]-Z[v];weight=float(Z[v]@d/(np.linalg.norm(Z[v])*np.linalg.norm(d)));G.add_edge(w,v,weight=max(0.,margin-weight)+1e-14)
 ar=nx.minimum_spanning_arborescence(G);parent=[-1]*len(Z);parent[root]=root;loss=0.
 for j,i in ar.edges():
  parent[i]=j;d=Z[j]-Z[i];w=float(Z[i]@d/(np.linalg.norm(Z[i])*np.linalg.norm(d)));loss+=max(0.,margin-w)
 assert all(i>=0 for i in parent)
 return st,p,dict(root=root,parent=parent,beta=globalq['beta'],deficit_sum=loss)

def run(a):
 inp=Path(a.input);cfg=json.loads(inp.read_text())
 if 'H' in cfg:
  H=np.asarray(cfg['H'],float);y=H[:,:3]/H[:,3,None]
 else:y=np.array(cfg['polar_points'])
 trust=a.trust;history=[];accepted=0;start=time.time()
 def save(st,p,q):
  r=report(y);Path(a.output).write_text(json.dumps(dict(polar_points=y.tolist(),points=r.pop('points'),grid=1,numerical_only=True,summary=r,physical_tree=p,polar_min_defect_tree=q),sort_keys=True,separators=(',',':')))
 for iteration in range(a.steps):
  st,p,q=state(y,a.margin);assert p['beta']>0
  if q['deficit_sum']<1e-14:print('NUMERICAL_ZERO_POLAR_DEFICIT_TREE',flush=True);break
  Y=torch.tensor(y,requires_grad=True);fn=lambda z:arrows_fixed(z,st,p,q);v=fn(Y).detach().numpy();jac=torch.autograd.functional.jacobian(fn,Y,vectorize=True).detach().numpy().reshape(len(v),-1);np_=len(p['parent'])-1;nq=len(q['parent'])-1;D=y.size;vp,vq=v[:np_],v[np_:];jp,jq=jac[:np_],jac[np_:]
  Ap=np.column_stack((-jp,np.zeros((np_,nq))));Aq=np.column_stack((-jq,-np.eye(nq)));b=np.concatenate((vp-a.physical_margin,vq-a.margin));cost=np.concatenate((np.zeros(D),np.ones(nq)));sol=linprog(cost,A_ub=np.vstack((Ap,Aq)),b_ub=b,bounds=[(-trust,trust)]*D+[(0,None)]*nq,method='highs')
  if not sol.success:
   trust*=.5;history.append(dict(iteration=iteration,lp_status=int(sol.status),trust=trust))
   if trust<a.trustfloor:break
   continue
  step=sol.x[:D].reshape(y.shape);candidate=None
  for k in range(a.backtracks):
   yy=y+2.**(-k)*step
   try:sts,ps,qs=state(yy,a.margin)
   except (ValueError,RuntimeError,AssertionError,nx.NetworkXException):continue
   if ps['beta']>=a.physical_margin/4 and qs['deficit_sum']<q['deficit_sum']-1e-12 and qs['beta']>=q['beta']-a.allowed_drop:candidate=(yy,sts,ps,qs,k);break
  if candidate:
   y,sts,ps,qs,k=candidate;accepted+=1;trust=min(a.maxtrust,trust*(1.15 if k==0 else .9));r=dict(iteration=iteration,accepted=accepted,backtrack=k,trust=trust,physical=ps['beta'],polar=qs['beta'],deficit_sum=qs['deficit_sum']);history.append(r)
   if iteration%5==0:save(sts,ps,qs);print(r,flush=True)
  else:trust*=.5;history.append(dict(iteration=iteration,rejected=True,trust=trust))
  if trust<a.trustfloor:break
 st,p,q=state(y,a.margin);save(st,p,q);rr=report(y);Path(a.output+'.report.json').write_text(json.dumps(dict(arguments=vars(a),input_sha256=hashlib.sha256(inp.read_bytes()).hexdigest(),accepted=accepted,history=history,elapsed=time.time()-start),sort_keys=True,separators=(',',':')));print('MIN_DEFECT_SLP_FINITE_END',accepted,p['beta'],q['beta'],q['deficit_sum'],{k:v for k,v in rr.items() if k!='points'},flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('output');p.add_argument('--steps',type=int,default=50);p.add_argument('--trust',type=float,default=.001);p.add_argument('--maxtrust',type=float,default=.01);p.add_argument('--trustfloor',type=float,default=1e-10);p.add_argument('--margin',type=float,default=1e-5);p.add_argument('--physical-margin',type=float,default=1e-4);p.add_argument('--allowed-drop',type=float,default=.01);p.add_argument('--backtracks',type=int,default=20);run(p.parse_args())
```
