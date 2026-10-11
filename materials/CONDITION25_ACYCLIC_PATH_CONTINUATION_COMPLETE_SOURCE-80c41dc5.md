# material-80c41dc5db39

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# Acyclic escape-path continuation — complete numerical source unit

## Scientific purpose and limitations
The exact mutual-witness obstruction is preserved in [internal-source-reference]. A forced arrow out of the sole unwanted unstable vertex can create a two-cycle with a neighbor whose only positive witness points back. This method reroutes a complete physical escape arborescence toward the desired apex, allows only specified initially negative path arrows to remain negative during a finite homotopy, and tightens their floors to a common positive gamma. Every other fixed physical arrow, switching centered-polar escape, protected root and convex-incidence condition is retained. The actual filled volume centroid and its derivatives are recomputed, never an arbitrary recentering.

BRANCH_GRAPH.py is a diagnostic for all-pair angular escapes and widest routes. Its widest-tree tie handling can choose unnecessary negative arrows for other vertices. Do NOT use that whole widest tree blindly. ACYCLIC_PATH_CONTINUATION.py instead keeps the initial positive max-arrow forest and changes only the specified path; it explicitly checks that every nonroot now reaches the desired root without a cycle. Intermediate path arrows may remain negative and additional actual unstable vertices are allowed in transit. No intermediate body is claimed own110. Numerical success requires exact freezing, maximal-complex reconstruction and independent A/B/mass checks before acceptance.

## Complete dependencies and reproducibility
Decode CONDITION25 ALL THREE [internal-source-reference],[internal-source-reference],[internal-source-reference] into source/. Their complete24-file dictionary includes flexible/contact/general_atlas/numeric/qp/REFINE and exact parent generator/auditors. Regenerate exact deletion inputs using MAKE_DELETION_INPUTS.py from [internal-source-reference]. No other sandbox, worker result or hidden helper is required. Expected parent generator11841bytes SHA8b8c74c7995098ff531e5d7652da20c1afa9cbaefaeea42cd78ea54e3e7e86f5; DELETE99 report310157 SHAaf5e1884bf301785a618928bf9ccbd44e965391ee964fd24f7e4cdf0cdaac85d; DELETE117 report309887 SHA3832d35b39b5e70cef5c21cfdd3cc5bb91985ba376324574200ddd287eb48446. delete_generator is checked against literal exact parent H deletion, not approximate coordinates.

Environment CPython3.13.5, NumPy2.3.5, SciPy1.17.0; BLAS/OMP1thread. Floating optimizer trajectories may vary across hardware; a frozen exact generator, not timing or numerical trajectory, defines an eventual object. Full scripts below include final newline: BRANCH_GRAPH.py2834bytes SHA1dbbfe96c06cff3b2ec26502172634c84be1fdf59d6c81845f293a6c78899b49; ACYCLIC_PATH_CONTINUATION.py6396bytes SHA973d97a6d10957fc5aea962870275e172f790f94c4c77b6d275d0209e2ded78c.

Commands for diagnostic inputs:
`python -B BRANCH_GRAPH.py --source source --report del99_exact/A.json --delete 99 --forced 128 --out graph99.json`
`python -B BRANCH_GRAPH.py --source source --report del117_exact/A.json --delete 117 --forced 76 --out graph117.json`
Observed graph99.json39782bytes SHAea7d5c263743487b9fbb56d77740cb96d9aa10f58b348d1457f1162b110107a2; graph117.json40253bytes SHA25887a5acbc7f5cdf0cef7cacf37c0424f5ea3f35d6b8ca6920b84555bd1f014. These are reproducible numerical diagnostics, not exact certificates. Initial forced paths cycle144→128→144 and79→76→79. Selected acyclic routes are144→128→145 and79→76→82 followed by the original positive forest to94/92. Their initially negative path angles are respectively[-.06969227897287897,-.059598073217134014] and[-.08638581362913228,-.06219726180681912].

Commands for finite numerical search:
`python -u ACYCLIC_PATH_CONTINUATION.py --source source --report del99_exact/A.json --delete 99 --path 144,128,145 --out acyclic99 --stages 35 --inner 40`
`python -u ACYCLIC_PATH_CONTINUATION.py --source source --report del117_exact/A.json --delete 117 --path 79,76,82 --out acyclic117 --stages 35 --inner 40`
All other parameters are defaults in source: lambda-step.05, gamma1e-8, trust.1, qbound.01, endpoint grid1e12 with np.rint ties-to-even. The script also supports a direct route144,145 or79,82. Such a route is not the previous one-shot full-target LP: finite nonlinear homotopy may follow a curved path even when a full linear proposal is infeasible.

Expected terminal ACYCLIC_PATH_CONTINUATION_FINITE_DONE. Output CONFIG.json contains complete fixed tree, path/slots, initial angles, versions, all arguments and input hashes. INPUT_GENERATOR.json, STAGES.json, LAST_TRIAL/ACCEPTED/FINAL_{GENERATOR,Z,MEASURE}.json and STATUS.json preserve exact integer controls and binary64 hex coordinates separately from numerical measurements. Accepted-stage success does not mean final lambda1 or own110. No not-yet-completed continuation outcome is claimed in this source material; results must be preserved separately.

### BRANCH_GRAPH.py
```python
"""Analyze forced-arrow cycles and widest acyclic escape routes; diagnostic, not exclusion."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import sys,json,argparse,heapq
from pathlib import Path
from fractions import Fraction as F
import numpy as np
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def main():
 p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--report',type=Path,required=True);p.add_argument('--delete',type=int,required=True);p.add_argument('--forced',type=int,required=True);p.add_argument('--checkpoint',type=Path);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 sys.path[:0]=[str(a.source/'methods'),str(a.source/'methods/parent')]
 from flexible import FlexibleAtlas,delete_generator
 import RECONSTRUCT
 G0=json.loads((a.source/'GENERATOR.json').read_text());raw=RECONSTRUCT.recover(G0);Q=np.array([[float(F(x,r[-1])) for x in r[:3]] for r in raw['H']]);G,_=delete_generator(G0,a.delete,Q);r=json.loads(a.report.read_text());s=FlexibleAtlas(G,r,np.delete(Q,a.delete,0));z=np.zeros(s.n) if a.checkpoint is None else np.array([float.fromhex(x) for x in json.loads(a.checkpoint.read_text())]);v,J,g=s.evaluate(z);X=g['X']-g['g'];d=X[None,:,:]-X[:,None,:];A=np.sum(X*X,axis=1);D=np.sum(d*d,axis=2);C=np.einsum('ic,ijc->ij',X,d);W=C/np.sqrt(np.maximum(A[:,None]*D,1e-40));np.fill_diagonal(W,-np.inf);mx=W.argmax(1);root=s.U;bad=next(i for i in r['unstable_vertices'] if i!=root)
 def route(par,start):
  seen=set();p=[];i=start
  while i!=root and i not in seen:seen.add(i);p.append(int(i));i=int(par[i])
  p.append(i);return p
 forced=mx.copy();forced[bad]=a.forced
 vals=np.full(s.nv,-np.inf);vals[root]=np.inf;par=np.full(s.nv,-1,int);done=np.zeros(s.nv,bool);queue=[(-np.inf,root)]
 while queue:
  neg,j=heapq.heappop(queue)
  if done[j]:continue
  done[j]=True
  for i in range(s.nv):
   if done[i]:continue
   c=min(vals[j],W[i,j])
   if c>vals[i]:vals[i]=c;par[i]=j;heapq.heappush(queue,(-c,i))
 path=route(par,bad);basin=[i for i in range(s.nv) if bad in route(mx,i)]
 rows=[dict(vertex=int(i),max_target=int(mx[i]),max_angle=float(W[i,mx[i]]),widest_target=int(par[i]),widest_angle=float(W[i,par[i]]),widest_value=float(vals[i])) for i in range(s.nv) if i!=root]
 res=dict(delete=a.delete,root=root,bad=bad,forced_target=a.forced,forced_cycle_or_path=route(forced,bad),widest_bad_path=path,widest_bad_arrows=[dict(source=i,target=j,angle=float(W[i,j])) for i,j in zip(path,path[1:])],bad_basin=basin,changed_negative_arrows=[r for r in rows if r['widest_angle']<=0],rows=rows,centroid=g['g'].tolist(),current_min_nonroot=float(np.min(np.delete(W.max(1),root))))
 a.out.write_bytes(B(res));print(B({k:x for k,x in res.items() if k!='rows'}).decode())
if __name__=='__main__':main()
```

### ACYCLIC_PATH_CONTINUATION.py
```python
"""Homotopy of a complete acyclic physical escape tree across a root basin.
Only the chosen path's initially negative arrows may stay negative in transit.
All physical arrows use fixed acyclic targets; polar escapes can switch freely.
Actual filled centroid and all convex-incidence guards are recomputed at each step.
Numerical producer only. Freeze exact controls and run independent auditors later.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,copy,hashlib,json,sys,time,platform
from pathlib import Path
from fractions import Fraction as F
import numpy as np,scipy
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
H=lambda b:hashlib.sha256(b).hexdigest()
def main():
 p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--report',type=Path,required=True);p.add_argument('--delete',type=int,required=True);p.add_argument('--path',required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--stages',type=int,default=35);p.add_argument('--inner',type=int,default=40);p.add_argument('--fraction',type=float,default=.05);p.add_argument('--gamma',type=float,default=1e-8);p.add_argument('--trust',type=float,default=.1);p.add_argument('--qbound',type=float,default=.01);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=False)
 sys.path[:0]=[str(a.source/'methods'),str(a.source/'methods/parent')]
 from flexible import FlexibleAtlas,delete_generator
 from REFINE import lp_l1
 import RECONSTRUCT,qp
 G0=json.load(open(a.source/'GENERATOR.json'));raw=RECONSTRUCT.recover(G0);Q=np.array([[float(F(x,r[-1])) for x in r[:3]] for r in raw['H']]);G,mapping=delete_generator(G0,a.delete,Q);assert RECONSTRUCT.recover(G)=={'H':[r for i,r in enumerate(raw['H']) if i!=a.delete]}
 rep=json.load(open(a.report));s=FlexibleAtlas(G,rep,np.delete(Q,a.delete,0));z=np.zeros(s.n);v,J,g=s.evaluate(z);bad=next(i for i in rep['unstable_vertices'] if i!=s.U);path=list(map(int,a.path.split(',')));assert path[0]==bad and len(set(path))==len(path)
 X=g['X']-g['g'];d=X[None,:,:]-X[:,None,:];W=np.einsum('ic,ijc->ij',X,d)/np.sqrt(np.maximum(np.sum(X*X,1)[:,None]*np.sum(d*d,2),1e-40));np.fill_diagonal(W,-np.inf);par=W.argmax(1);tree={i:int(par[i]) for i in range(s.nv) if i!=s.U}
 for i,j in zip(path,path[1:]):assert i!=s.U;tree[i]=j
 for i in tree:
  seen=set();j=i
  while j!=s.U:assert j not in seen,('cycle',i,j);seen.add(j);j=tree[j]
 s.forcedp=tree;s.last=None;v,J,g=s.evaluate(z);slots=np.array([int(np.where(s.keptp==i)[0][0]) for i in path[:-1]]);initial=v[slots].copy();assert np.all(initial<0)
 s.floor[:s.mechlen-2]=a.gamma;s.floor[s.mechlen-2:s.mechlen]=.25*v[s.mechlen-2:s.mechlen];s.floor[s.mechlen:s.mechlen+s.nq]=1e-9;s.floor[s.mechlen+s.nq:s.mechlen+s.nq+len(s.tris)]=1e-8;s.floor[slots]=initial
 cfg={k:str(v) if isinstance(v,Path) else v for k,v in vars(a).items()};cfg.update(parent_generator_sha256=H(B(G0)),input_generator_sha256=H(B(G)),report_sha256=H(a.report.read_bytes()),versions=[platform.python_version(),np.__version__,scipy.__version__],path=path,tree=tree,slots=slots.tolist(),initial_path_angles=initial.tolist(),variables=s.n);(a.out/'CONFIG.json').write_bytes(B(cfg));(a.out/'INPUT_GENERATOR.json').write_bytes(B(G));hist=[];lam=0.;step=a.fraction;t0=time.monotonic()
 def measure(zz):
  vv,JJ,gg=s.evaluate(zz);return dict(path_angles=vv[slots].tolist(),mechanical_minimum=float(vv[:s.mechlen].min()),other_minimum=float(np.delete(vv[:s.mechlen-2],slots).min()),polar_minimum=float(vv[s.nv-1:s.mechlen-2].min()),slack=float(gg['slack'].min()),v6minimum=float(gg['v6'].min()),volume=float(gg['V']),centroid=gg['g'].tolist())
 def save(zz,stem):
  vv,JJ,gg=s.evaluate(zz);GG=copy.deepcopy(G);GG['grid']=10**12;GG['controls']=np.rint(gg['Y']*GG['grid']).astype(np.int64).tolist();(a.out/(stem+'_GENERATOR.json')).write_bytes(B(GG));(a.out/(stem+'_Z.json')).write_bytes(B([float(x).hex() for x in zz]));(a.out/(stem+'_MEASURE.json')).write_bytes(B(measure(zz)))
 def project(z0,target,old):
  zz=z0.copy();s.floor[slots]=initial+(a.gamma-initial)*target;desired=s.floor+np.maximum(abs(s.floor)*.01,1e-13);desired[slots]=s.floor[slots]+np.maximum(np.minimum((a.gamma-initial)*(target-old)*.01,1e-8),1e-13);records=[];trust=a.trust;qbound=a.qbound
  for it in range(a.inner):
   vv,JJ,gg=s.evaluate(zz);merit=float(np.linalg.norm(s.residual(zz)));row=dict(it=it,merit=merit,min_guard=float(np.min(vv-s.floor)),**measure(zz));records.append(row)
   if row['min_guard']>-1e-12:return zz,True,records
   JQ=gg['DY'][:s.nq].reshape(-1,s.n);AA=np.vstack((JJ/s.rescale[:,None],JQ));lo=np.r_[(desired-vv)/s.rescale,np.full(3*s.nq,-qbound)];hi=np.r_[np.full(len(vv),np.inf),np.full(3*s.nq,qbound)]
   dz,err=qp.solve(AA,lo,hi,np.full(s.n,-trust),np.full(s.n,trust),np.ones(s.n),tol=1e-10)
   if dz is None:dz,err=lp_l1(AA,lo,hi,np.full(s.n,-trust),np.full(s.n,trust),np.ones(s.n))
   if dz is None:
    row['failure']=err;trust=min(.5,trust*1.5);qbound=min(.05,qbound*1.5)
    if it>2 and all('failure' in r for r in records[-3:]):break
    continue
   ok=False
   for j in range(16):
    alpha=2.**-j
    try:
     value=float(np.linalg.norm(s.residual(zz+alpha*dz)))
     if np.isfinite(value) and (value<merit*(1-1e-5*alpha) or value<1e-10):zz+=alpha*dz;ok=True;break
    except (ValueError,np.linalg.LinAlgError,FloatingPointError):pass
   row.update(alpha=alpha,accepted=ok,proposal_norm=float(np.linalg.norm(dz)))
   if not ok:trust*=.5;qbound*=.5
   if trust<1e-8:break
  return zz,False,records
 for k in range(a.stages):
  target=min(1.,lam+step);print('ACYCLIC_TARGET',k,lam,target,flush=True);zz,ok,records=project(z,target,lam);hist.append(dict(stage=k,old_lambda=lam,target=target,step=step,success=ok,inner=records));(a.out/'STAGES.json').write_bytes(B(hist));save(zz,'LAST_TRIAL');print('ACYCLIC_STAGE',k,ok,len(records),records[-1],flush=True)
  if ok:z=zz;lam=target;save(z,'ACCEPTED');step=min(.25,step*1.3)
  else:step*=.5
  if lam==1 or step<1e-7:break
 save(z,'FINAL');status=dict(lambda_reached=lam,stages=len(hist),seconds=time.monotonic()-t0,**measure(z));status['numerical_own11_candidate']=status['mechanical_minimum']>0 and status['slack']>0 and status['v6minimum']>0;(a.out/'STATUS.json').write_bytes(B(status));print('ACYCLIC_PATH_CONTINUATION_FINITE_DONE',B(status).decode(),flush=True)
if __name__=='__main__':main()
```
