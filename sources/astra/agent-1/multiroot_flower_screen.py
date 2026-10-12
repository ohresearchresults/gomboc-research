"""Geometric covering additions for the shallow multi-stable own-U1 body.
Coverage means an old stable facet is removed, not that its equilibrium has
vanished. Reference and freshly integrated own-centroid counts are separate.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import pathlib,json,hashlib,time
import numpy as np
from scipy.spatial import QhullError
from contact_forest import ContactModel
from stable_face_augmentation import halfspaces
from geometry import halfspace_mesh,arrows,census
from persistence_search import pairs,polar_edges


def bars(A,edges):
    pp,h=pairs(A,edges)
    return (1-h[pp[:,1]]/(A[pp[:,0]]**2).sum(1)).tolist()


def run(pool,out,trials=600,seed=210940):
    pool=pathlib.Path(pool);data=json.loads(pool.read_text());out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False)
    c=ContactModel(data['source'],1,1,'local');e=c.evaluate(np.load(data['input'])['z'],False)
    assert e['U']==1;P=e['P'];Q=e['Q'];rows=data['rows'];points=np.array([r['point'] for r in rows])
    S=np.flatnonzero(arrows(Q).max(1)<0);elder=int(np.argmax((Q*Q).sum(1)));S=S[S!=elder]
    cover=Q[S]@points.T>1+1e-9;rng=np.random.default_rng(seed);history=[];best=(999,999.);start=time.time()
    np.savez(out/'physical_parent.npz',X=P,Q=Q)
    (out/'definition.json').write_text(json.dumps(dict(pool=str(pool.resolve()),pool_sha256=hashlib.sha256(pool.read_bytes()).hexdigest(),
        trials=trials,seed=seed,scope='Literal flower additions; stable-facet coverage is a heuristic, actual reference and own-centroid equilibria all recomputed'),indent=2))
    for it in range(trials):
        count=1+it%5;remaining=np.ones(len(S),bool);chosen=[]
        for k in range(count):
            gain=cover[remaining].sum(0).astype(float)
            noise=rng.uniform(0,[.2,2.,6.][it%3],len(points))
            objective=gain+noise
            if chosen:objective[chosen]=-np.inf
            idx=int(np.argmax(objective));chosen.append(idx);remaining&=~cover[:,idx]
        pts=points[chosen]
        try:
            for i,v in zip(chosen,pts):
                if v@(P[rows[i]['witness']]-v)<=0:raise ValueError('Reference escape witness not strict')
            H=halfspaces(np.r_[P,pts]);m=halfspace_mesh(H);own=census(m,0);X=m['X'];H=H[m['active']]
            refU=int(np.sum(arrows(X).max(1)<0));refS=int(np.sum(arrows(H).max(1)<0))
            if refU!=1:raise ValueError('Reference escape invariant failed numerical reconstruction')
            dual_edges=polar_edges(m);rq=bars(H,dual_edges)
            op=bars(X-m['g'],m['edges']);oq=bars(H/(1-H@m['g'])[:,None],dual_edges)
            row=dict(trial=it,point_indices=chosen,old_stable_facets_cut=int((~remaining).sum()),referenceS=refS,referenceU=refU,
                referenceQ=rq,referenceQmax=max(rq,default=0),ownP=op,ownQ=oq,seconds=time.time()-start,**own)
            rank=(refS,max(rq,default=0))
            if 17<=own['E']<249 and (rank<best or refS==1):
                p=out/f'trial{it:04d}';p.mkdir();np.savez(p/'body.npz',X=X,Q=H,added_points=pts)
                proposal=dict(scope='Numerical literal hull proposal; rational reconstruction required',V=len(X),E=own['E'],F=len(H),
                    faces=m['faces'],edges=m['edges'].tolist(),active=list(range(len(H))),
                    raw_vertices=[[str(v) for v in x] for x in X],raw_halfspaces=[[str(v) for v in q]+['1'] for q in H])
                (p/'proposal.json').write_text(json.dumps(proposal,indent=2));row['folder']=str(p.resolve())
                (p/'summary.json').write_text(json.dumps(row,indent=2));best=min(best,rank)
                (out/'best-reference.json').write_text(json.dumps(row,indent=2))
                print('MULTIROOT_FLOWER_BEST',json.dumps({k:v for k,v in row.items() if k not in ('referenceQ','ownP','ownQ')}),flush=True)
            if 17<=own['E']<249 and own['S']==own['U']==1:
                np.savez(out/'POTENTIAL_OWN110.npz',X=X,Q=H,added_points=pts)
                history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));return
        except (ValueError,RuntimeError,AssertionError,QhullError,np.linalg.LinAlgError) as error:
            row=dict(trial=it,point_indices=chosen,error=repr(error))
        history.append(row)
        if it%20==0:(out/'history.json').write_text(json.dumps(history,indent=2))
    (out/'history.json').write_text(json.dumps(history,indent=2))
