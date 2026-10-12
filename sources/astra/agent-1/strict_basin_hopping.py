"""Nonmonotone physical-shape exploration between strict equilibrium chambers.

Seeded finite perturbations and complete actual-centroid correction. An uphill
remaining-basin step may be retained by an explicit temperature rule. The goal
is still own110 and weak000 after a complete rational audit of the same body.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,pathlib,json,time,contextlib
import numpy as np
from persistence_search import search
from soft_forest_polish import run as polish
from geometry import halfspace_mesh,census
from basin_scout import score

def qualifies(Q):
    m=halfspace_mesh(Q);c=census(m,0)
    return 17<=c['E']<250 and c['S']==c['U']==1 and min(c['min_primal_nonroot'],c['min_polar_nonroot'])>1e-9

def run(input,out,side='Q',seed=83197,steps=80):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);rng=np.random.default_rng(seed);Q=np.load(input)['Q'];assert len(Q)<=84
    targetU,targetS=(2,1) if side=='P' else (1,2);state=score(Q);value=max(state[side],default=0);best=value;history=[];start=time.time()
    (out/'definition.json').write_text(json.dumps(dict(input=str(pathlib.Path(input).resolve()),side=side,seed=seed,rule='Explicit Metropolis acceptance on sole remaining relative basin depth after strict actual-centroid correction',maximum_submitted_supports=len(Q)),indent=2));np.savez(out/'initial.npz',Q=Q)
    for k in range(steps):
        folder=out/f'trial{k:04d}';folder.mkdir();before=Q.copy();amplitude=[.0005,.002,.008,.02][k%4];temperature=.025*(.99**k)+.003
        # Include projective and affine physical maps, plus genuinely local
        # support perturbations. Every resulting body is fully re-integrated.
        if k%3==0:
            M=np.eye(3)+rng.normal(size=(3,3))*amplitude
            trial=Q@np.linalg.inv(M)
        elif k%3==1:trial=Q+rng.normal(size=3)*amplitude*np.sqrt(np.mean(Q*Q))
        else:
            perturb=rng.normal(size=Q.shape);mask=rng.random(len(Q))<.3;perturb[~mask]=0;trial=Q+amplitude*np.sqrt(np.mean(Q*Q))*perturb
        np.savez(folder/'proposal.npz',Q=trial)
        try:
            with (folder/'calculation.log').open('w') as log,contextlib.redirect_stdout(log):
                fixed=polish(trial,folder/'initial-repair',nP=targetU,nQ=targetS,steps=45)
                if qualifies(fixed):
                    np.savez(out/'POTENTIAL_OWN110.npz',Q=fixed);return
                s=score(fixed)
                if s['S']!=targetS or s['U']!=targetU:raise ValueError('no strict requested chamber reached after finite correction')
                search(fixed,folder/'descent',iters=450,apex=False,kind='log')
                if (folder/'descent/NOMINATION.npz').exists():
                    candidate=np.load(folder/'descent/NOMINATION.npz')['Q']
                    if qualifies(candidate):np.savez(out/'POTENTIAL_OWN110.npz',Q=candidate);return
                candidate=np.load(folder/'descent/best.npz')['Q'];repaired=polish(candidate,folder/'final-repair',nP=targetU,nQ=targetS,steps=70)
                if qualifies(repaired):np.savez(out/'POTENTIAL_OWN110.npz',Q=repaired);return
            s=score(repaired)
            if s['S']!=targetS or s['U']!=targetU:raise ValueError('final strict chamber correction failed')
            after=max(s[side],default=0);probability=1. if after<=value else float(np.exp((value-after)/temperature));draw=float(rng.random());accepted=draw<probability
            row=dict(trial=k,amplitude=amplitude,temperature=temperature,before=value,after=after,accepted=accepted,probability=probability,draw=draw,S=s['S'],U=s['U'],E=s['E'],seconds=time.time()-start)
            np.savez(folder/'strict-endpoint.npz',Q=repaired)
            if accepted:Q=repaired;value=after;np.savez(out/'current.npz',Q=Q)
            if after<best:best=after;np.savez(out/'best.npz',Q=repaired);(out/'best.json').write_text(json.dumps(row,indent=2))
        except (ValueError,RuntimeError,np.linalg.LinAlgError) as err:row=dict(trial=k,amplitude=amplitude,rejected_error=repr(err),seconds=time.time()-start)
        history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));print('STRICT_BASIN_HOP',row,flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--input',required=True);ap.add_argument('--out',required=True);ap.add_argument('--side',choices=['P','Q'],default='Q');ap.add_argument('--seed',type=int,default=83197);ap.add_argument('--steps',type=int,default=80);a=ap.parse_args();run(a.input,a.out,a.side,a.seed,a.steps)
