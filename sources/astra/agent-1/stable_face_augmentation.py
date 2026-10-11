"""Literal one-vertex augmentation beyond the junior stable facet.

Proposals are sampled in a physical Thales ball about the existing unstable
vertex. This gives a reference-centre escape witness for the new point; every
body is then independently reintegrated at its actual mass centroid. No witness
or equilibrium assertion is transferred through the centroid shift.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,json,pathlib,time,contextlib
import numpy as np
from scipy.spatial import ConvexHull,QhullError
from geometry import halfspace_mesh,arrows,census
from basin_scout import score
from soft_forest_polish import run as polish
from persistence_search import search

def halfspaces(X):
    hull=ConvexHull(X);equations=[]
    for row in hull.equations:
        if not any(np.max(abs(row-old))<1e-9 for old in equations):equations.append(row)
    H=np.array(equations)
    if np.max(H[:,3])>=-1e-8:raise ValueError('augmentation lost interior origin')
    return -H[:,:3]/H[:,3,None]

def run(input,out,samples=800,repairs=16,seed=82931,witness_set='root'):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);Q=np.load(input)['Q'];m=halfspace_mesh(Q);P=m['X']-m['g'];R=Q/(1-Q@m['g'])[:,None]
    wp=arrows(P);wq=arrows(R);roots=np.flatnonzero(wq.max(1)<0);elder=int(np.argmax((R*R).sum(1)));junior=next(int(i) for i in roots if i!=elder);u=P[np.argmax((P*P).sum(1))]
    assert np.sum(wp.max(1)<0)==1 and len(roots)==2
    n=R[junior]/np.linalg.norm(R[junior]);h=1/np.linalg.norm(R[junior]);a=u-(u@n)*n;a/=np.linalg.norm(a);b=np.cross(n,a);rng=np.random.default_rng(seed);history=[];candidates=[];start=time.time();best=1e9
    if witness_set=='root':witnesses=[int(np.argmax((P*P).sum(1)))]
    elif witness_set=='all':witnesses=np.flatnonzero((P@n+np.linalg.norm(P,axis=1))/2>h+1e-10).tolist()
    else:raise ValueError('unknown explicit reference witness set')
    if not witnesses or max((n@P[i]+np.linalg.norm(P[i]))/2 for i in witnesses)<=h:
        raise ValueError('the chosen reference Thales balls have no cap beyond the unwanted facet')
    (out/'definition.json').write_text(json.dumps(dict(input=str(pathlib.Path(input).resolve()),seed=seed,junior=junior,old_centroid=m['g'].tolist(),normal=n.tolist(),support=h,unstable_vertex=u.tolist(),witness_set=witness_set,witness_indices=witnesses,scope='Physical one-vertex convex hulls, actual own centroid recomputed, numerical screening only'),indent=2));np.savez(out/'original.npz',X=P,Q=R)
    # Every sampled point lies on a plane beyond the old stable facet. The
    # remaining disk is the intersection with the diameter-(0,u) Thales ball.
    for k in range(samples):
        witness=witnesses[0] if witness_set=='root' else int(rng.choice(witnesses));w=P[witness]
        depth=rng.uniform(.0001,1.) if k%5 else 10**rng.uniform(-7,-2)
        top=(n@w+np.linalg.norm(w))/2;vheight=h+depth*(top-h)
        radius2=(w@w)/4-(vheight-(n@w)/2)**2
        if radius2<=0:continue
        angle=rng.uniform(0,2*np.pi);rad=np.sqrt(rng.random())*np.sqrt(radius2)*.999
        v=w/2+n*(vheight-(n@w)/2)+rad*(np.cos(angle)*a+np.sin(angle)*b)
        try:
            q=halfspaces(np.r_[P,v[None]]);s=score(q)
            referenceS=int(np.sum(arrows(q).max(1)<0));referenceU=int(np.sum(arrows(np.r_[P,v[None]]).max(1)<0))
            if referenceU!=1:raise ValueError('floating candidate conflicts with the reference escape-witness construction')
            row=dict(sample=k,added_vertex=v.tolist(),witness_vertex=witness,reference_escape=float(v@(w-v)),referenceS=referenceS,referenceU=referenceU,seconds=time.time()-start,**s)
            if referenceS==1 and 17<=s['E']<249:
                np.savez(out/f'REFERENCE110-sample{k:05d}.npz',Q=q,X=np.r_[P,v[None]],reference=np.zeros(3));print('REFERENCE110_ONLY',json.dumps(row),flush=True)
            if 17<=s['E']<249 and len(q)<=84:
                p=out/f'sample{k:05d}.npz';np.savez(p,Q=q,X=np.r_[P,v[None]]);row['input']=str(p.resolve());candidates.append((s['score'],k,p))
                if s['score']<best:best=s['score'];print('AUGMENTATION_BEST',json.dumps(row),flush=True)
                if s['S']==s['U']==1 and min(s['min_primal_nonroot'],s['min_polar_nonroot'])>1e-9:
                    np.savez(out/'POTENTIAL_OWN110.npz',Q=q);return
        except (ValueError,QhullError,np.linalg.LinAlgError) as err:row=dict(sample=k,error=repr(err))
        history.append(row)
        if k%25==0:(out/'screen.json').write_text(json.dumps(history,indent=2))
    (out/'screen.json').write_text(json.dumps(history,indent=2));results=[]
    for rank,(_,k,p) in enumerate(sorted(candidates)[:repairs]):
        folder=out/f'repair{rank:02d}-sample{k:05d}';folder.mkdir();q=np.load(p)['Q']
        try:
            with (folder/'calculation.log').open('w') as log,contextlib.redirect_stdout(log):
                # Both possible one-extra-equilibrium chambers are legitimate
                # intermediate bodies, and own110 is checked before either.
                search(q,folder/'consolidation',iters=900,apex=False,kind='log')
                q=np.load(folder/'consolidation/best.npz')['Q']
                for nu,ns in [(1,1),(1,2),(2,1)]:
                    qq=polish(q,folder/f'correct-U{nu}S{ns}',nP=nu,nQ=ns,steps=90);s=score(qq)
                    row=dict(rank=rank,sample=k,target=[ns,nu],seconds=time.time()-start,**s);results.append(row);np.savez(folder/f'endpoint-U{nu}S{ns}.npz',Q=qq)
                    if s['S']==s['U']==1 and 17<=s['E']<249 and min(s['min_primal_nonroot'],s['min_polar_nonroot'])>1e-9:
                        np.savez(out/'POTENTIAL_OWN110.npz',Q=qq);(out/'repairs.json').write_text(json.dumps(results,indent=2));return
                    print('REPAIRED_AUGMENTATION',json.dumps(row),flush=True)
            print('AUGMENTATION_REPAIR_COMPLETE',rank,k,flush=True)
        except (ValueError,QhullError,RuntimeError,np.linalg.LinAlgError) as err:results.append(dict(rank=rank,sample=k,error=repr(err)))
        (out/'repairs.json').write_text(json.dumps(results,indent=2))

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--input',required=True);ap.add_argument('--out',required=True);ap.add_argument('--samples',type=int,default=800);ap.add_argument('--repairs',type=int,default=16);ap.add_argument('--seed',type=int,default=82931);ap.add_argument('--witness-set',choices=['root','all'],default='root');a=ap.parse_args();run(a.input,a.out,a.samples,a.repairs,a.seed,a.witness_set)
