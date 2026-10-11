"""A second exact geometric regime for literal point augmentation.

If a reference-centred body has one unstable vertex u, adding a new point v with
u.(v-u)>0 preserves escape for every old nonmaximum and gives u an escape too.
The new point is therefore the unique reference maximum (it is farther than u).
This reference argument does NOT put the new uniform centroid at that origin.
Every actual centroid and complete own census is recomputed and recorded.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,pathlib,json,time
import numpy as np
from scipy.spatial import QhullError
from stable_face_augmentation import halfspaces
from geometry import halfspace_mesh,census,arrows
from basin_scout import score

def run(input,out,samples=1600,seed=91571):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);q=np.load(input)['Q'];m=halfspace_mesh(q);P=m['X']-m['g'];R=q/(1-q@m['g'])[:,None];u=P[np.argmax((P*P).sum(1))];assert np.sum(arrows(P).max(1)<0)==1
    S=np.flatnonzero(arrows(R).max(1)<0);elder=int(np.argmax((R*R).sum(1)));junior=next(int(i) for i in S if i!=elder);n=R[junior]/np.linalg.norm(R[junior]);rng=np.random.default_rng(seed);history=[];start=time.time();count=0
    np.savez(out/'source.npz',X=P,Q=R);(out/'definition.json').write_text(json.dumps(dict(input=str(pathlib.Path(input).resolve()),seed=seed,source_centroid=m['g'].tolist(),old_root=u.tolist(),junior=junior,scope='Literal convex-hull additions, reference and actual centres explicitly distinguished'),indent=2))
    for k in range(samples):
        direction=rng.normal(size=3)
        if k%3==0:direction=n+rng.normal(size=3)*.35
        # Enforce the strict old-root escape analytically, with a free tangent
        # component, rather than conditioning on a floating post hoc census.
        tangent=direction-u*(direction@u)/(u@u);v=(1+10**rng.uniform(-5,1))*u+tangent*np.linalg.norm(u)*10**rng.uniform(-2,.7)
        try:
            Q=halfspaces(np.r_[P,v[None]]);mm=halfspace_mesh(Q);own=census(mm,0);ref=dict(mm);ref['g']=np.zeros(3);cc=census(ref,0)
            row=dict(sample=k,vertex=v.tolist(),reference_S=cc['S'],reference_U=cc['U'],reference_margin=min(cc['min_primal_nonroot'],cc['min_polar_nonroot']),old_root_escape=float(u@(v-u)),actual=own,seconds=time.time()-start)
            if cc['U']!=1:raise ValueError('numerical geometry conflicts with strict reference escape construction')
            if 17<=own['E']<249 and (cc['S']==1 or own['S']==own['U']==1):
                count+=1;p=out/f'candidate{k:05d}.npz';np.savez(p,Q=Q,X=np.r_[P,v[None]],reference=np.zeros(3));row['input']=str(p.resolve());s=score(Q);row['own_Pmax']=max(s['P'],default=0);row['own_Qmax']=max(s['Q'],default=0);print('REFERENCE110_AUGMENTATION',json.dumps(row),flush=True)
            if 17<=own['E']<249 and own['S']==own['U']==1 and min(own['min_primal_nonroot'],own['min_polar_nonroot'])>1e-9:
                np.savez(out/'POTENTIAL_OWN110.npz',Q=Q,X=np.r_[P,v[None]]);history.append(row);(out/'screen.json').write_text(json.dumps(history,indent=2));return
        except (ValueError,QhullError,np.linalg.LinAlgError) as err:row=dict(sample=k,error=repr(err),vertex=v.tolist())
        history.append(row)
        if k%25==0:(out/'screen.json').write_text(json.dumps(history,indent=2))
    (out/'screen.json').write_text(json.dumps(history,indent=2));print('FINITE_REFERENCE_SCREEN_COMPLETE',len(history),count,flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--input',required=True);ap.add_argument('--out',required=True);ap.add_argument('--samples',type=int,default=1600);ap.add_argument('--seed',type=int,default=91571);a=ap.parse_args();run(a.input,a.out,a.samples,a.seed)
