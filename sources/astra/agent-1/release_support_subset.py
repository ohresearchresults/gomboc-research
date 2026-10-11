"""Retire literal supports to84, then free all surviving support coordinates.
The final family has a universal genuine-edge bound E<=246, without pretending
that a parent's nonsimple vertices survive arbitrary normal movement. All
intermediate hulls and own-centroid equilibria are recomputed.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,pathlib,json,time,contextlib
from fractions import Fraction
import numpy as np
from scipy.spatial import QhullError
from basin_scout import score
from soft_forest_polish import run as polish
from geometry import halfspace_mesh,census

def run(parent,out,width=3,target=84,repairs=3):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);H=json.loads(pathlib.Path(parent).read_text())['H'];Q=np.array([[float(Fraction(x,row[3])) for x in row[:3]] for row in H]);m=halfspace_mesh(Q);Q=Q[m['active']]/(1-Q[m['active']]@m['g'])[:,None];N=len(Q);assert 6<=target<=84 and N>target;beam=[(score(Q)['score'],tuple(range(N)),Q)];history=[];start=time.time();np.savez(out/'parent.npz',Q=Q)
    for stage in range(N-target):
        folder=out/f'delete{stage:02d}';folder.mkdir();candidates={};records=[]
        for rank,(_,ids,q) in enumerate(beam):
            for j in range(len(q)):
                remain=ids[:j]+ids[j+1:]
                if remain in candidates:continue
                trial=np.delete(q,j,axis=0)
                try:
                    s=score(trial);row=dict(parent_rank=rank,removed=ids[j],remaining=remain,**s);records.append(row);candidates[remain]=(s['score'],remain,trial,row)
                    if s['S']==s['U']==1 and 17<=s['E']<249 and min(s['min_primal_nonroot'],s['min_polar_nonroot'])>1e-9:
                        np.savez(out/'POTENTIAL_OWN110.npz',Q=trial);(folder/'screen.json').write_text(json.dumps(records,indent=2));return
                except (ValueError,QhullError,np.linalg.LinAlgError) as error:records.append(dict(parent_rank=rank,removed=ids[j],error=repr(error)))
        chosen=sorted(candidates.values(),key=lambda x:x[0])[:width]
        if not chosen:raise ValueError('No bounded physical support retirement admitted')
        beam=[r[:3] for r in chosen];(folder/'screen.json').write_text(json.dumps(records,indent=2));row=dict(stage=stage,facets_supplied=N-stage-1,selected=[r[3] for r in chosen],seconds=time.time()-start);history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));print('SUPPORT_SUBSET_STAGE',stage,'N',N-stage-1,[(r[3]['S'],r[3]['U'],r[3]['E'],r[0]) for r in chosen],flush=True)
        for rank,r in enumerate(chosen):np.savez(folder/f'candidate{rank}.npz',Q=r[2],retained_ids=np.array(r[1]))
    results=[]
    for rank,(_,ids,q) in enumerate(beam[:repairs]):
        p=out/f'repair{rank:02d}';p.mkdir();np.savez(p/'input.npz',Q=q,retained_ids=np.array(ids))
        for nU,nS in [(1,1),(1,2)]:
            try:
                with (p/f'class-U{nU}S{nS}.log').open('w') as log,contextlib.redirect_stdout(log):qq=polish(q,p/f'class-U{nU}S{nS}',nP=nU,nQ=nS,steps=180,apex=False)
                s=score(qq);s.update(census(halfspace_mesh(qq),0));r=dict(rank=rank,target=[nS,nU],seconds=time.time()-start,**s);np.savez(p/f'endpoint-U{nU}S{nS}.npz',Q=qq);results.append(r);(out/'repairs.json').write_text(json.dumps(results,indent=2));print('SUPPORT_SUBSET_REPAIR',json.dumps({k:r[k] for k in ['rank','target','S','U','E','Q','P']}),flush=True)
                if s['S']==s['U']==1 and 17<=s['E']<249 and min(s['min_primal_nonroot'],s['min_polar_nonroot'])>1e-9:np.savez(out/'POTENTIAL_OWN110.npz',Q=qq);return
            except (ValueError,QhullError,RuntimeError,AssertionError,np.linalg.LinAlgError) as error:results.append(dict(rank=rank,target=[nS,nU],error=repr(error)));(out/'repairs.json').write_text(json.dumps(results,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--parent',required=True);p.add_argument('--out',required=True);p.add_argument('--width',type=int,default=3);p.add_argument('--target',type=int,default=84);p.add_argument('--repairs',type=int,default=3);a=p.parse_args();run(a.parent,a.out,a.width,a.target,a.repairs)
