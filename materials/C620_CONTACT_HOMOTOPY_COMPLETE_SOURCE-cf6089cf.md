# material-cf6089cfa6af

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# C620 contact-chart homotopy — complete numerical source

## Purpose and exact input closure
This method deforms each of the four exact strict121/weak000 C620 one-neighbor contact-cut charts in its full313-variable contact atlas. The actual filled volume centroid, centered polar and incidence guards are recomputed after every proposal. It does NOT substitute an arbitrary center. Initial physical max-arrow choices form a forest ending at the desired apex or the extra unstable vertex; the extra vertex is rerouted to its best angular target outside its basin. The resulting complete physical graph is explicitly checked acyclic and rooted at the desired apex. Fixed mode retains this tree; dag mode permits switching to any later vertex in a deterministic topological order; switch mode fixes only the bad vertex's chosen target. Polar witnesses may switch. During the homotopy only the initial bad physical arrow is allowed to remain negative. All other physical and polar escapes and protected-root/convexity guards retain positive floors. Intermediate accepted stages are NOT own110 bodies.

Exact inputs are the six charts reproducible from [internal-source-reference] (CONDITION25_SIX_EXACT_CONTACT_CUT_CHARTS_RECOVERY.md, SHA1464ac98592b509eda8a1b0f64d2a252f18d382e7d01d67b4fd262f94fd0f605), its deletion-input helper in [internal-source-reference] (SHAc3e7fc3cef5a2c1fc3d3d7d20930add743d579643fc221381905ae6834960581), and CONDITION25 ALL THREE standalone source materials:
[internal-source-reference] SHA20469536cc4461b597cd92b9c7420b89ad4f1efd82ef72aa4f934b9bb772067a;
[internal-source-reference] SHAa527d91c2ba70ee5220ca4b6ba30964e804fd4fa52a8619d3ae6567608cc8087;
[internal-source-reference] SHAecb59180686fbea53343e4b78e64b70478df5ede3679acd200c163185c1e29d4.
These FIVE materials plus the complete script below are sufficient without an originating sandbox or worker result. Decode the source dictionary into source/, run MAKE_DELETION_INPUTS.py, then CONTACT_CUT_CHARTS.py as specified in those materials. All actual input hashes, full fixed tree, order and parameters are recorded in each run CONFIG.json.

The four starting chart A reports are delete99_neighbor128:316462bytes SHA290524e82efd07897aab77d1fd71537654b91f99bce3741717481a08c07ebfb0; delete99_neighbor145:313970bytes SHAbb3f50d4924f333086656c483a9264b71e10fd7bb3a5746985fce4d08798d264; delete117_neighbor76:316350bytes SHA962c27537d097f2a07d8572bff33161ad63a29f3e0c6c3efd627cee09f9936c0; delete117_neighbor82:315384bytes SHA88422e3a518cb46817b7c02305393b21a09e262475ab462a52e45061d6492f7a. Each was reconstructed exactly in the producing turn. No B/mass outcome or final homotopy outcome is implied by this source-only material.

## Execution and evidence boundary
Save the complete code block including its final newline as CONTACT_HOMOTOPY.py,7166bytes SHA6a8430bcf7004652dbfd159735c03d70e953c6cc9306ab81c720f5ac5fa96b08. Environment CPython3.13.5,NumPy2.3.5,SciPy1.17.0; BLAS/OMP1thread. For each NAME from the four names above, the producing finite command is:
`python -u -B CONTACT_HOMOTOPY.py --source source --body contact_charts/NAME --out homo_NAME --stages 35 --inner 30`
Mode fixed, fraction.05,gamma1e-8,trust.1,qbound.01 are explicit source defaults. Alternative modes are separate experiments, not silently substituted outcomes. Restart requires the original exact chart and an explicitly preserved previous FINAL_Z/STATUS checkpoint; a restart changes the next step to the specified fraction. The four initial acyclic targets are128→144 with desiredroot94;145→146 withroot94;76→79 withroot93;80→83 withroot93, respectively. Labels belong to each starting chart, not its deletion parent.

Terminal marker CONTACT_HOMOTOPY_FINITE_DONE. Outputs CONFIG.json,STAGES.json, LAST_TRIAL/ACCEPTED/FINAL_{GENERATOR,Z,MEASURE}.json and STATUS.json preserve rounded integer controls and binary64hex coordinates separately from numerical measurements. Final generators use grid1e12,np.rint ties-to-even. Optimizer trajectory may vary with hardware; a frozen exact generator, not numerical timing or trajectory identity, defines any later object. A successful stage only satisfies its current possibly negative bad-arrow floor. Even lambda1 requires exact freezing, exhaustive maximal-complex reconstruction, independent A/B and centered-mass checks before an own110 claim. No new record is claimed here. Actual completed outcomes and output hashes must be preserved separately.

### CONTACT_HOMOTOPY.py
```python
"""Finite own-centroid contact-chart escape homotopy; numerical discovery only.
Input is an exact GENERATOR.json and exhaustive maximal-complex A.json.
The physical witness graph is made acyclic before continuation. In fixed mode
its arrows are retained. In dag mode each vertex may switch to any later vertex
in a topological ordering, including its original chosen successor. Polar
escapes can switch in both modes. No numerical output is an exact certificate.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,copy,hashlib,heapq,json,platform,sys,time
from pathlib import Path
from fractions import Fraction as F
import numpy as np,scipy
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
H=lambda b:hashlib.sha256(b).hexdigest()
def main():
 p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--body',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--mode',choices=['fixed','dag','switch'],default='fixed');p.add_argument('--stages',type=int,default=40);p.add_argument('--inner',type=int,default=35);p.add_argument('--fraction',type=float,default=.05);p.add_argument('--gamma',type=float,default=1e-8);p.add_argument('--trust',type=float,default=.1);p.add_argument('--qbound',type=float,default=.01);p.add_argument('--restart',type=Path);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=False)
 sys.path[:0]=[str(a.source/'methods'),str(a.source/'methods/parent')]
 from flexible import FlexibleAtlas
 from REFINE import lp_l1
 import RECONSTRUCT,qp
 G=json.loads((a.body/'GENERATOR.json').read_text());rep=json.loads((a.body/'A.json').read_text());raw=RECONSTRUCT.recover(G);assert raw==json.loads((a.body/'RAW.json').read_text())
 Q=np.array([[float(F(x,r[-1])) for x in r[:3]] for r in raw['H']]);s=FlexibleAtlas(G,rep,Q);z=np.zeros(s.n);v,J,g=s.evaluate(z);assert rep['counts']==[1,2,1] and rep['weak']==[0,0,0];bad=next(i for i in rep['unstable_vertices'] if i!=s.U)
 X=g['X']-g['g'];d=X[None,:,:]-X[:,None,:];W=np.einsum('ic,ijc->ij',X,d)/np.sqrt(np.maximum(np.sum(X*X,1)[:,None]*np.sum(d*d,2),1e-40));np.fill_diagonal(W,-np.inf);par=W.argmax(1);tree={i:int(par[i]) for i in range(s.nv) if i!=s.U}
 def hits_bad(i):
  seen=set()
  while i!=s.U and i not in seen:
   if i==bad:return True
   seen.add(i);i=tree[i]
  return False
 basin=[i for i in tree if hits_bad(i)];target=next(int(i) for i in np.argsort(-W[bad]) if i not in basin);tree[bad]=target
 for i in tree:
  seen=set();j=i
  while j!=s.U:assert j not in seen,('cycle',i,j);seen.add(j);j=tree[j]
 # A deterministic topological order; initial arrows all go forward.
 indeg=[0]*s.nv
 for j in tree.values():indeg[j]+=1
 todo=[i for i in range(s.nv) if indeg[i]==0];heapq.heapify(todo);order=[]
 while todo:
  i=heapq.heappop(todo);order.append(i)
  if i in tree:
   j=tree[i];indeg[j]-=1
   if indeg[j]==0:heapq.heappush(todo,j)
 assert len(order)==s.nv and order[-1]==s.U
 rank={i:k for k,i in enumerate(order)}
 if a.mode=='fixed':s.forcedp=tree
 elif a.mode=='dag':s.blockedp=[(i,j) for i in tree for j in range(s.nv) if rank[j]<=rank[i]]
 else:s.forcedp={bad:target}
 s.last=None;v,J,g=s.evaluate(z);slot=int(np.where(s.keptp==bad)[0][0]);initial=float(v[slot]);assert initial<0
 s.floor[:s.mechlen-2]=a.gamma;s.floor[s.mechlen-2:s.mechlen]=.25*v[s.mechlen-2:s.mechlen];s.floor[s.mechlen:s.mechlen+s.nq]=1e-9;s.floor[s.mechlen+s.nq:s.mechlen+s.nq+len(s.tris)]=1e-8;s.floor[slot]=initial
 cfg={k:str(v) if isinstance(v,Path) else v for k,v in vars(a).items()};cfg.update(generator_sha256=H(B(G)),raw_sha256=H(B(raw)),report_sha256=H((a.body/'A.json').read_bytes()),versions=[platform.python_version(),np.__version__,scipy.__version__],root=s.U,bad=bad,target=target,tree=tree,order=order,slot=slot,initial_bad_angle=initial,variables=s.n)
 (a.out/'CONFIG.json').write_bytes(B(cfg));hist=[];lam=0.;step=a.fraction;t0=time.monotonic()
 if a.restart:
  z=np.array([float.fromhex(x) for x in json.loads((a.restart/'FINAL_Z.json').read_text())]);lam=json.loads((a.restart/'STATUS.json').read_text())['lambda_reached']
 def measure(zz):
  vv,JJ,gg=s.evaluate(zz);return dict(bad_angle=float(vv[slot]),mechanical_minimum=float(vv[:s.mechlen].min()),other_minimum=float(np.delete(vv[:s.mechlen-2],slot).min()),polar_minimum=float(vv[s.nv-1:s.mechlen-2].min()),slack=float(gg['slack'].min()),v6minimum=float(gg['v6'].min()),volume=float(gg['V']),centroid=gg['g'].tolist())
 def save(zz,stem):
  vv,JJ,gg=s.evaluate(zz);GG=copy.deepcopy(G);GG['grid']=10**12;GG['controls']=np.rint(gg['Y']*GG['grid']).astype(np.int64).tolist();(a.out/(stem+'_GENERATOR.json')).write_bytes(B(GG));(a.out/(stem+'_Z.json')).write_bytes(B([float(x).hex() for x in zz]));(a.out/(stem+'_MEASURE.json')).write_bytes(B(measure(zz)))
 def project(z0,target,old):
  zz=z0.copy();s.floor[slot]=initial+(a.gamma-initial)*target;desired=s.floor+np.maximum(abs(s.floor)*.01,1e-13);desired[slot]=s.floor[slot]+max(min((a.gamma-initial)*(target-old)*.01,1e-8),1e-13);records=[];trust=a.trust;qbound=a.qbound
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
  targetlam=min(1.,lam+step);zz,ok,records=project(z,targetlam,lam);hist.append(dict(stage=k,old_lambda=lam,target=targetlam,step=step,success=ok,inner=records));(a.out/'STAGES.json').write_bytes(B(hist));save(zz,'LAST_TRIAL');print('CONTACT_HOMOTOPY_STAGE',k,lam,targetlam,ok,len(records),records[-1],flush=True)
  if ok:z=zz;lam=targetlam;save(z,'ACCEPTED');step=min(.25,step*1.3)
  else:step*=.5
  if lam==1 or step<1e-7:break
 save(z,'FINAL');status=dict(lambda_reached=lam,stages=len(hist),seconds=time.monotonic()-t0,**measure(z));status['numerical_own11_candidate']=status['mechanical_minimum']>0 and status['slack']>0 and status['v6minimum']>0;(a.out/'STATUS.json').write_bytes(B(status));print('CONTACT_HOMOTOPY_FINITE_DONE',B(status).decode(),flush=True)
if __name__=='__main__':main()
```
