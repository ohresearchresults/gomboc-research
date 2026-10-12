"""Whole physical support continuation permitting every equilibrium class.
Eta schedule motivated by peer3's pinned free-vertex continuation source; this
experiment uses a bounded-facet physical H family with actual volume integration.
No reference centre or intermediate class repair is imposed.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,pathlib,json,time
import numpy as np
from persistence_search import search
from geometry import halfspace_mesh,census
from basin_scout import score

def run(input,out,steps=2500,seed=0,perturb=0.):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);Q=np.load(input)['Q'];assert len(Q)<=84
    if perturb:
        rng=np.random.default_rng(seed);Q+=rng.normal(size=Q.shape)*perturb*np.sqrt(np.mean(Q*Q))
    np.savez(out/'initial.npz',Q=Q);history=[];start=time.time()
    (out/'definition.json').write_text(json.dumps(dict(input=str(pathlib.Path(input).resolve()),seed=seed,perturb=perturb,mass='uniform volume at actual centroid',class_constraints='none until separate endpoint correction',submitted_supports=len(Q),universal_edge_bound=3*len(Q)-6),indent=2))
    for stage,eta in enumerate([1.,.3,.1,.03,.01,.003,.001,.0001,.00001]):
        folder=out/f'stage{stage:02d}'
        try:search(Q,folder,iters=steps,apex=False,kind='log',seed=seed,eta=eta)
        except (ValueError,RuntimeError,np.linalg.LinAlgError) as err:
            folder.mkdir(exist_ok=True);(folder/'ERROR.json').write_text(json.dumps(dict(error=repr(err)),indent=2));print('UNRESTRICTED_STAGE_FAILED',stage,repr(err),flush=True)
            return
        if (folder/'NOMINATION.npz').exists():
            q=np.load(folder/'NOMINATION.npz')['Q'];e=census(halfspace_mesh(q),0)
            if e['S']==e['U']==1:
                np.savez(out/'POTENTIAL_OWN110.npz',Q=q);print('POTENTIAL_OWN110_REQUIRES_COMPLETE_EXACT',flush=True);return
        Q=np.load(folder/'best.npz')['Q'];s=score(Q);row=dict(stage=stage,eta=eta,seconds=time.time()-start,**s);history.append(row);(out/'stages.json').write_text(json.dumps(history,indent=2));np.savez(out/'latest.npz',Q=Q);print('UNRESTRICTED_SUPPORT_STAGE',{k:row[k] for k in ['stage','eta','S','U','E','P','Q','seconds']},flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--input',required=True);ap.add_argument('--out',required=True);ap.add_argument('--steps',type=int,default=2500);ap.add_argument('--seed',type=int,default=0);ap.add_argument('--perturb',type=float,default=0.);a=ap.parse_args();run(a.input,a.out,a.steps,a.seed,a.perturb)
