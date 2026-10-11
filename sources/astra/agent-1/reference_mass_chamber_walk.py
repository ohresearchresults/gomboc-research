"""Finite shape excursions inside a genuine reference110 contact chamber.
Linear predictors hold the normalized centroid to first order while exploring
other physical shape directions. Nonlinear own mass and reference equilibria
are rechecked. Each excursion is followed by a new actual-centroid closure.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import pathlib,json,time,contextlib
import numpy as np
from scipy.optimize import linprog
from reference_mass_curved_flow import ReferenceBody,repair_reference,run as descend
from contact_centroid_flow import normalized,metric
from contact_retraction import retract


def run(source,input,out,tries=12,walk_steps=24,descent_steps=160,seed=971219):
    source=pathlib.Path(source).resolve();input=pathlib.Path(input).resolve();out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False)
    c=ReferenceBody(source);initial=np.load(input)['z'];base=c.evaluate(initial);base_mass=float(np.linalg.norm(normalized(base)[0]))
    floor=.2*normalized(base)[2];eps=1e-9;rng=np.random.default_rng(seed);history=[];start=time.time()
    (out/'definition.json').write_text(json.dumps(dict(source=str(source),input=str(input),tries=tries,walk_steps=walk_steps,
        descent_steps=descent_steps,seed=seed,allowed_mass_factor=1.05,normalized_volume_floor=floor,
        scope='Finite physical reference110 excursions followed by actual uniform mass closure; only own110 is a nomination'),indent=2))
    (out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes())
    for trial in range(tries):
        p=out/f'trial{trial:02d}';p.mkdir();z=initial.copy();trust=.015;walk=[]
        force=rng.normal(size=base['A'].shape)
        # Smooth the random field along genuine boundary edges; preserve the
        # distinction between physical vertices and dual support vectors.
        for _ in range(3):
            new=force.copy();degree=np.ones(c.n)
            for edges,offset in [(c.eu,c.F),(c.es,0)]:
                for a,b in edges:
                    a+=offset;b+=offset;new[a]+=force[b];new[b]+=force[a];degree[a]+=1;degree[b]+=1
            force=new/degree[:,None]
        with (p/'calculation.log').open('w') as log,contextlib.redirect_stdout(log):
            for it in range(walk_steps):
                e=c.evaluate(z);m,M,nv,DV=normalized(e);W=metric(e);d=c.free;bound=trust/np.sqrt(d)
                row=dict(it=it,mass_distance=float(np.linalg.norm(m)),referenceS=e['S'],referenceU=e['U'],ownS=e['ownS'],ownU=e['ownU'],trust=trust)
                walk.append(row);np.savez(p/'walk-latest.npz',z=z,X=e['X'],Q=e['Y']);(p/'walk.json').write_text(json.dumps(walk,indent=2))
                if e['ownS']==e['ownU']==1:
                    np.savez(out/'POTENTIAL_OWN110.npz',z=z,X=e['X'],Q=e['Y']);(out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(chart=str(source),input=str((out/'POTENTIAL_OWN110.npz').resolve())),indent=2));return
                root=e['roots'][0][0];axis=e['X'][root]/np.linalg.norm(e['X'][root]);anchor=int(np.argmax(np.linalg.norm(np.cross(e['Y'],axis),axis=1)))
                roll=np.cross(axis,e['Y'][anchor]);roll/=np.linalg.norm(roll)
                eq=np.vstack([M@W,e['DX'][root]@W,roll@e['DY'][anchor]@W]);es=np.maximum(np.linalg.norm(eq,axis=1),1e-12);eq/=es[:,None]
                A=np.vstack([-e['J']@W,-e['gapJ']@W,-DV@W]);b=np.r_[e['mechanical']-eps,.8*e['gapv'],nv-floor]
                keep=b<=bound*np.abs(A).sum(1)+1e-10;A=A[keep];b=b[keep];sc=np.maximum(bound*np.abs(A).sum(1),1e-12);A/=sc[:,None];b/=sc
                gradient=-np.einsum('ic,icp->p',force,e['DA'])@W;gradient/=max(float(abs(gradient).max()),1e-30)
                lp=linprog(gradient,A_ub=A,b_ub=b,A_eq=eq,b_eq=np.zeros(len(eq)),bounds=[(-bound,bound)]*d,method='highs',
                    options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
                if not lp.success:trust*=.5;continue
                dz=W@lp.x;accepted=False
                for level in range(7):
                    try:
                        zz,ee,receipt=retract(c,e,dz,2**-level)
                        if ee['S']!=1 or ee['U']!=1 or ee['mechanical'].min()<.8*eps:
                            zz,ee,ok=repair_reference(c,zz,p/f'guard-repair-{it:03d}-{level}',eps=eps,steps=18)
                            if ee['ownS']==ee['ownU']==1:
                                np.savez(out/'POTENTIAL_OWN110.npz',z=zz,X=ee['X'],Q=ee['Y']);(out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(chart=str(source),input=str((out/'POTENTIAL_OWN110.npz').resolve())),indent=2));return
                            if not ok:continue
                        radius=np.max(np.linalg.norm(ee['X'],axis=1))
                        if ee['volume']/radius**3>floor and np.linalg.norm(ee['g'])/radius<=1.05*base_mass:
                            z=zz;accepted=True;row.update(alpha=2**-level,physical_step=receipt['physical_step']);break
                    except (ValueError,RuntimeError,AssertionError,np.linalg.LinAlgError):continue
                if accepted and level==0:trust=min(.08,trust*1.2)
                elif not accepted:trust*=.4
                if trust<1e-8:break
            e=c.evaluate(z,False);np.savez(p/'excursion.npz',z=z,X=e['X'],Q=e['Y'])
            descend(source,p/'excursion.npz',p/'mass-closure',steps=descent_steps,eps=eps)
        if (p/'mass-closure/POTENTIAL_OWN110.json').exists():
            (out/'POTENTIAL_OWN110.json').write_bytes((p/'mass-closure/POTENTIAL_OWN110.json').read_bytes());return
        result=json.loads((p/'mass-closure/history.json').read_text())[-1];result.pop('retraction',None);result.update(trial=trial,chart=str(source),input=str((p/'mass-closure/latest.npz').resolve()),total_seconds=time.time()-start)
        history.append(result);(out/'history.json').write_text(json.dumps(history,indent=2));print('CHAMBER_WALK_MASS_ENDPOINT',json.dumps(result),flush=True)
