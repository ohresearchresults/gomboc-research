"""Independent generic starts in the fully asymmetric positive-shadow family.

Each perturbation is a new explicitly saved candidate. Three actual uniform
mass equations are restored before any refinement. Rejected constructions
remain recorded; no tolerance deletes positive equilibrium bars.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from shadow_free_base_family import Family
from shadow_mass_retracted_goal import restore,bars,census,run as refine

def run(sources,out,trials,seed):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);rng=np.random.default_rng(seed);history=[];start=time.time()
    for case in range(trials):
        source=sources[case%len(sources)];F=Family(np.load(source));q=F.q.copy();sigma=[.003,.015,.05,.1][(case//len(sources))%4]
        q[:F.ad]+=rng.normal(0,sigma,F.ad);q[F.ad:F.cost_end]=np.maximum(q[F.ad:F.cost_end]+rng.normal(0,sigma*.02,F.n),1e-8);q[F.cost_end:F.cost_end+2]+=rng.normal(0,sigma*2,2)
        q=np.array([np.clip(v,lo+1e-10,hi-1e-10)for v,(lo,hi)in zip(q,F.bounds)]);d=out/f'case{case:03d}';d.mkdir();np.save(d/'trial_parameters.npy',q);row=dict(case=case,source=source,sigma=sigma)
        try:
            if min(F.domain(q)[0])<=0:raise ValueError('base angular domain rejected')
            q,g,corr=restore(F,q);row['mass_correction']=corr
            if q is None:raise ValueError('actual mass correction did not converge')
            cc=census(g)
            if cc['U']!=1 or not cc['base_valid']:raise ValueError('restored trial is not actualU1 with a base')
            values,_,_=bars(g,False);row.update(initial_Q=float(max(values,default=0.)),initial_census=cc);np.save(d/'physical.npy',g['X']);np.save(d/'parameters.npy',q);(d/'construction.json').write_text(json.dumps(row,indent=2))
            refine(d/'physical.npy',d/'parameters.npy',d/'goal_refinement',1200,True);result=json.loads((d/'goal_refinement/latest.json').read_text());row.update(endpoint=result)
        except(ValueError,np.linalg.LinAlgError)as err:
            row['rejected']=repr(err);(d/'REJECTED.json').write_text(json.dumps(row,indent=2))
        history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));print('SHADOW_TILTED_BASIN',dict(case=case,seconds=time.time()-start,**{k:v for k,v in row.items()if k not in ['case','mass_correction']}),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('out');p.add_argument('sources',nargs='+');p.add_argument('--trials',type=int,default=24);p.add_argument('--seed',type=int,default=945312);a=p.parse_args();run(a.sources,a.out,a.trials,a.seed)
