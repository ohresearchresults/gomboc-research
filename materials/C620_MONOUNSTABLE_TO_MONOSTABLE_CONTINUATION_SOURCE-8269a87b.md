# material-8269a87bcef8

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# Complete own-centroid polar-restoration methods on two exact C620 monounstable bodies

## Purpose and scope
The exact C620 endpoints COORD_C620_RELAX01_99N128_OWN64_1_63 and COORD_C620_RELAX01_117N76_OWN57_1_56 are independently verified NONWINNERS with U1, many stable equilibria, no weak cases. This method attempts to restore S1 while retaining positive physical escapes, the original apex, stable face3, full contact incidence, positive fans, nonowner convexity slacks, and the actual filled-volume centroid. No numerical stage is an accepted own110 body.

Two schedules are preserved. RESTORE_POLAR_HOMOTOPY raises initially negative polar maxima individually from their respective initial values to gamma; initially positive polar maxima remain positive. UNIFORM_RESTORE_POLAR gives ALL non-root polar maxima the same initially negative floor, then raises that floor to gamma. The latter permits new temporary stable faces, widening the admissible path. Both permit max-witness switching and recompute actual mass/centroid derivatives; they do not use a fictitious reference center or polar body's own centroid.

At this preservation step, the two individual-floor runs had accepted lambda0.758471725; a larger target0.87914195 had failed the finite projector. The uniform-floor99 run accepted lambda0.87914195. These are partial numerical observations only. Complete final endpoints and terminal receipts must be stored separately when observed. No failure here proves geometric infeasibility. Canonical own110 C622 remains unchanged.

## Exact input and source closure
Recover BOTH [internal-source-reference] and [internal-source-reference], materialSHA67956fa6445b79ab807416edc3017de7956d4b003aa6be27467fc4930e886086 and c5c1eb3d8b075f77c926c499ebf90bb93f5d34d289620967d78db09cedb48c17, using their ordered complete13-file dictionary. Recover standalone CONDITION25 ALL THREE [internal-source-reference],[internal-source-reference],[internal-source-reference] into source/. These FIVE source materials contain all exact endpoint coordinates, independent A/B/mass auditors and imported numeric atlas/solver helpers; no contact-chart ancestor or original sandbox is needed to START restoration from the frozen monounstable bodies. The full original phaseA numerical provenance is in those capsules but is not a missing endpoint input.

Run package/REPLAY_RELAXED_SOURCE.py source workspace to recover two exact body directories with GENERATOR.json,RAW.json,A.json. For99N128 expected G11926bytes SHAa15ded9d508f3fc2b91c727c3289370a83e5a61e5fe443ec76e926024b2e0e95;RAW15837SHA8a4aa2272c40497956c0fbbce67c0b29f854a9decdbefb7d7386ff95fe891d65;A316254SHA2cee1e5b607c165a74600e120287372eac54af96fe0a0700de448253333b34e2. For117N76 expected G11932SHA539e27799102c9cfe88b77a4fb505ee5a716df4fb468c6c6f5c918f0fecbb616;RAW15815SHAc59749a964a74360b212c038aef32d02c2af3cb29bfe825c130c86cdd7c10f77;A315111SHAa2e8d4a98640413c25253cae4c48deaf1cd7b4109b4432176dca3db5387cfd6a.

Save RESTORE_POLAR_HOMOTOPY.py below including final newline:5512bytes SHA7ff17eba8762934dc5bb0b7decac24ea34b96530c03881f5c07314de3d8ded2a. Run separately on each exact body: python -u -B RESTORE_POLAR_HOMOTOPY.py --source source --body BODY_DIRECTORY --out FRESH_OUTPUT --stages 35 --inner 30. All other options are their literal code defaults. Expected finite terminal RESTORE_POLAR_FINITE_DONE. Final success or failure is not inferred from this expected marker.

Save MAKE_UNIFORM_RESTORE.py below:1174bytes SHAdafb0da550d9f16f144c7e188fb2adc632d80da8a6d4de41ff14ca8a282c1fc5. Run python -B -S MAKE_UNIFORM_RESTORE.py RESTORE_POLAR_HOMOTOPY.py UNIFORM_RESTORE_POLAR.py. This source patch completed with UNIFORM_RESTORE_SOURCE_READY; generated5618bytes SHA f4f76a4bea9b01bc8c13a05ad838c1c6a5291ca7ad886055165786d23d314333. Run python -u -B UNIFORM_RESTORE_POLAR.py --source source --body BODY_DIRECTORY --out FRESH_OUTPUT --stages 35 --inner 30. Default --polar-relax .01; expected finite terminal UNIFORM_RESTORE_FINITE_DONE. Numerical environment CPython3.13.5,NumPy2.3.5,SciPy1.17.0,OPENBLAS_NUM_THREADS=1,OMP_NUM_THREADS=1. Complete CONFIG,STAGES,hexadecimal coordinate vectors and grid1e12 ties-to-even frozen generators are written by each run. Exact frozen generators, not platform-dependent numeric trajectories, define later bodies.

### RESTORE_POLAR_HOMOTOPY.py
```python
"""Restore mono-stability from an exact relaxed-polar, own-monounstable body.
Keep all physical escapes, own filled-volume mass and convexity guards active.
Initially negative polar escapes are raised together through finite homotopy.
No numerical stage is an exact record; freeze and audit the final generator.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,copy,hashlib,json,platform,sys,time
from fractions import Fraction as F
from pathlib import Path
import numpy as np,scipy
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
H=lambda b:hashlib.sha256(b).hexdigest()
def main():
 p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--body',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--stages',type=int,default=35);p.add_argument('--inner',type=int,default=30);p.add_argument('--fraction',type=float,default=.05);p.add_argument('--gamma',type=float,default=1e-8);p.add_argument('--trust',type=float,default=.1);p.add_argument('--qbound',type=float,default=.01);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=False)
 sys.path[:0]=[str(a.source/'methods'),str(a.source/'methods/parent')];from flexible import FlexibleAtlas
 from REFINE import lp_l1
 import qp,RECONSTRUCT
 G=json.loads((a.body/'GENERATOR.json').read_text());rep=json.loads((a.body/'A.json').read_text());raw=RECONSTRUCT.recover(G);assert raw==json.loads((a.body/'RAW.json').read_text());assert rep['counts'][1]==1 and rep['weak']==[0,0,0] and 3 in rep['stable_face_ids']
 Q=np.array([[float(F(x,r[-1])) for x in r[:3]] for r in raw['H']]);s=FlexibleAtlas(G,rep,Q);z=np.zeros(s.n);v,J,g=s.evaluate(z);assert min(v[:s.nv-1])>0
 s.floor[:s.mechlen-2]=a.gamma;s.floor[s.mechlen-2:s.mechlen]=.25*v[s.mechlen-2:s.mechlen];s.floor[s.mechlen:s.mechlen+s.nq]=1e-9;s.floor[s.mechlen+s.nq:s.mechlen+s.nq+len(s.tris)]=1e-8
 ix=np.where(v[s.nv-1:s.mechlen-2]<a.gamma)[0]+s.nv-1;assert len(ix)>0;initial=v[ix].copy();s.floor[ix]=initial
 cfg={k:str(x) if isinstance(x,Path) else x for k,x in vars(a).items()};cfg.update(method_sha256=H(Path(__file__).read_bytes()),generator_sha256=H((a.body/'GENERATOR.json').read_bytes()),raw_sha256=H(B(raw)),report_sha256=H((a.body/'A.json').read_bytes()),versions=[platform.python_version(),np.__version__,scipy.__version__],root=s.U,stable=3,variables=s.n,raised_slots=ix.tolist(),initial_raised_values=initial.tolist());(a.out/'CONFIG.json').write_bytes(B(cfg));hist=[];lam=0.;step=a.fraction;t0=time.monotonic()
 def measure(zz):
  vv,JJ,gg=s.evaluate(zz);return dict(physical_minimum=float(vv[:s.nv-1].min()),polar_minimum=float(vv[s.nv-1:s.mechlen-2].min()),mechanical_minimum=float(vv[:s.mechlen].min()),negative_polar_count=int(sum(vv[s.nv-1:s.mechlen-2]<0)),slack=float(gg['slack'].min()),v6minimum=float(gg['v6'].min()),volume=float(gg['V']),centroid=gg['g'].tolist())
 def save(zz,stem):
  vv,JJ,gg=s.evaluate(zz);GG=copy.deepcopy(G);GG['grid']=10**12;GG['controls']=np.rint(gg['Y']*GG['grid']).astype(np.int64).tolist();(a.out/(stem+'_GENERATOR.json')).write_bytes(B(GG));(a.out/(stem+'_Z.json')).write_bytes(B([float(x).hex() for x in zz]));(a.out/(stem+'_MEASURE.json')).write_bytes(B(measure(zz)))
 def project(z0,target):
  zz=z0.copy();s.floor[ix]=initial+(a.gamma-initial)*target;desired=s.floor+np.maximum(abs(s.floor)*.01,1e-13);desired[ix]=s.floor[ix];records=[];trust=a.trust;qbound=a.qbound
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
     val=float(np.linalg.norm(s.residual(zz+alpha*dz)))
     if np.isfinite(val) and (val<merit*(1-1e-5*alpha) or val<1e-10):zz+=alpha*dz;ok=True;break
    except (ValueError,np.linalg.LinAlgError,FloatingPointError):pass
   row.update(alpha=alpha,accepted=ok,proposal_norm=float(np.linalg.norm(dz)))
   if not ok:trust*=.5;qbound*=.5
   if trust<1e-8:break
  return zz,False,records
 for k in range(a.stages):
  target=min(1.,lam+step);zz,ok,records=project(z,target);hist.append(dict(stage=k,old_lambda=lam,target=target,step=step,success=ok,inner=records));(a.out/'STAGES.json').write_bytes(B(hist));save(zz,'LAST_TRIAL');print('RESTORE_POLAR_STAGE',k,lam,target,ok,len(records),records[-1],flush=True)
  if ok:z=zz;lam=target;save(z,'ACCEPTED');step=min(.25,step*1.3)
  else:step*=.5
  if lam==1 or step<1e-7:break
 save(z,'FINAL');status=dict(lambda_reached=lam,stages=len(hist),seconds=time.monotonic()-t0,**measure(z));status['numerical_own11_candidate']=status['mechanical_minimum']>0 and status['slack']>0 and status['v6minimum']>0;(a.out/'STATUS.json').write_bytes(B(status));print('RESTORE_POLAR_FINITE_DONE',B(status).decode(),flush=True)
if __name__=='__main__':main()
```

### MAKE_UNIFORM_RESTORE.py
```python
"""Exact patch: allow every non-root polar witness to change sign temporarily."""
from pathlib import Path
import hashlib,sys
assert len(sys.argv)==3
s=Path(sys.argv[1]).read_text();assert hashlib.sha256(s.encode()).hexdigest()=='7ff17eba8762934dc5bb0b7decac24ea34b96530c03881f5c07314de3d8ded2a'
s=s.replace("p.add_argument('--stages',type=int,default=35);","p.add_argument('--polar-relax',type=float,default=.01);p.add_argument('--stages',type=int,default=35);")
s=s.replace("ix=np.where(v[s.nv-1:s.mechlen-2]<a.gamma)[0]+s.nv-1;assert len(ix)>0;initial=v[ix].copy();s.floor[ix]=initial","ix=np.arange(s.nv-1,s.mechlen-2);assert a.polar_relax>0;initial=np.full(len(ix),-a.polar_relax);assert np.all(v[ix]>=initial);s.floor[ix]=initial")
s=s.replace('Initially negative polar escapes are raised together through finite homotopy.','ALL non-root polar escapes share one rising floor, permitting new temporary stable faces.')
s=s.replace('RESTORE_POLAR_STAGE','UNIFORM_RESTORE_STAGE').replace('RESTORE_POLAR_FINITE_DONE','UNIFORM_RESTORE_FINITE_DONE')
Path(sys.argv[2]).write_text(s);print('UNIFORM_RESTORE_SOURCE_READY',len(s.encode()),hashlib.sha256(s.encode()).hexdigest())
```
