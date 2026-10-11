"""Simultaneous physical additions in the old-vertex escape-ball union.

Two to four new points can remove an entire polar basin differently from a
single cut. Every new point has an explicit old escape witness. Reference U=1
is a conditional geometric invariant; it is NOT an own-centroid claim. All
own-centroid counts, moments, and genuine numerical hull counts are separate.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,pathlib,json,time
import numpy as np
from scipy.spatial import QhullError
from stable_face_augmentation import halfspaces
from geometry import halfspace_mesh,arrows,census
from persistence_search import pairs,polar_edges

def depths(A,edges):
    pp,h=pairs(A,edges);return (1-h[pp[:,1]]/(A[pp[:,0]]**2).sum(1)).tolist()

def run(input,out,samples=1500,seed=992912):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);Q=np.load(input)['Q'];m=halfspace_mesh(Q);P=m['X']-m['g'];Q=Q[m['active']];Q=Q/(1-Q@m['g'])[:,None];S=np.flatnonzero(arrows(Q).max(1)<0);u=int(np.argmax((P*P).sum(1)));assert len(S)==2 and np.sum(arrows(P).max(1)<0)==1;elder=int(np.argmax((Q*Q).sum(1)));junior=next(int(i) for i in S if i!=elder);n=Q[junior]/np.linalg.norm(Q[junior]);h=1/np.linalg.norm(Q[junior]);a=P[u]-(P[u]@n)*n;a/=np.linalg.norm(a);b=np.cross(n,a);eligible=np.flatnonzero((P@n+np.linalg.norm(P,axis=1))/2>h+1e-10);rng=np.random.default_rng(seed);history=[];best=1.;start=time.time();np.savez(out/'parent.npz',X=P,Q=Q);(out/'definition.json').write_text(json.dumps(dict(input=str(pathlib.Path(input).resolve()),seed=seed,junior=junior,eligible_witnesses=eligible.tolist(),scope='Numerical literal multi-point hulls with explicitly distinct reference and volume-centroid equilibrium counts'),indent=2))
    for it in range(samples):
        count=2+it%3;pts=[];witness=[];phase=rng.uniform(0,2*np.pi)
        for k in range(count):
            j=int(rng.choice(eligible));w=P[j];top=(n@w+np.linalg.norm(w))/2;depth=rng.uniform(.05,.999) if it%4 else 10**rng.uniform(-5,-.3);height=h+depth*(top-h);radius=np.sqrt(max(0,w@w/4-(height-n@w/2)**2));angle=phase+2*np.pi*k/count+rng.normal(scale=.25) if it%2 else rng.uniform(0,2*np.pi);rad=radius*np.sqrt(rng.uniform(.1,.999))*.999;v=w/2+n*(height-n@w/2)+rad*(np.cos(angle)*a+np.sin(angle)*b);assert v@(w-v)>0;pts.append(v);witness.append(j)
        try:
            X=np.r_[P,pts];H=halfspaces(X);body=halfspace_mesh(H);edges=len(body['edges']);refU=int(np.sum(arrows(body['X']).max(1)<0));refS=int(np.sum(arrows(H[body['active']]).max(1)<0));assert refU==1
            eq=polar_edges(body);rq=depths(H,eq);own=census(body,0);p=depths(body['X']-body['g'],body['edges']);q=depths(H/(1-H@body['g'])[:,None],eq);value=max(rq,default=0);row=dict(sample=it,added_points=np.array(pts).tolist(),witnesses=witness,referenceS=refS,referenceU=refU,referenceQ=rq,referenceQmax=value,ownP=p,ownQ=q,**own)
            if 17<=edges<249 and (value<best or refS==1):
                folder=out/f'sample{it:05d}';folder.mkdir();np.savez(folder/'body.npz',X=body['X'],Q=H,added_points=pts);proposal=dict(scope='Numerical multi-point physical body proposal; exact audit required',source=str((out/'parent.npz').resolve()),V=len(body['X']),E=edges,F=len(body['active']),faces=body['faces'],edges=body['edges'].tolist(),active=list(range(len(body['active']))),raw_vertices=[[str(x) for x in p] for p in body['X']],raw_halfspaces=[[str(x) for x in p]+['1'] for p in H[body['active']]]);(folder/'proposal.json').write_text(json.dumps(proposal,indent=2));(folder/'summary.json').write_text(json.dumps(row,indent=2));row['folder']=str(folder.resolve())
                if value<best:best=value;(out/'best-reference.json').write_text(json.dumps(row,indent=2));print('MULTIPOINT_REFERENCE_BEST',json.dumps({k:row[k] for k in ['sample','referenceS','referenceU','referenceQ','S','U','E','folder']}),flush=True)
                if refS==1:print('REFERENCE110_MULTI_POINT_NOT_OWN_CENTROID',it,flush=True)
            if 17<=edges<249 and own['S']==own['U']==1 and min(own['min_primal_nonroot'],own['min_polar_nonroot'])>1e-9:
                np.savez(out/'POTENTIAL_OWN110.npz',X=body['X'],Q=H,added_points=pts);history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));return
        except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError) as err:row=dict(sample=it,error=repr(err),added_points=np.array(pts).tolist(),witnesses=witness)
        history.append(row)
        if it%25==0:(out/'history.json').write_text(json.dumps(history,indent=2))
    (out/'history.json').write_text(json.dumps(history,indent=2));print('MULTIPOINT_FINITE_SCREEN_COMPLETE',len(history),best,time.time()-start,flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--out',required=True);p.add_argument('--samples',type=int,default=1500);p.add_argument('--seed',type=int,default=992912);a=p.parse_args();run(a.input,a.out,a.samples,a.seed)
