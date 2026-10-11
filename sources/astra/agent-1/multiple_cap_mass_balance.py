"""Balance several purposeful escape-ball additions by three larger caps.

The compensation points may see several old facets. Every Newton step uses
the actual new convex hull's first moment and analytic derivative; independent
pyramid moments are used only for an initial guess. Each point is bounded by
an old-vertex escape ball. The same physical hull is then fully reintegrated
and counted. No residual or reference census is accepted as exact evidence.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,pathlib,json,itertools,time,hashlib
import numpy as np
from scipy.spatial import QhullError
from balanced_flower_caps import parent_data
from balanced_cap_optimize import mass
from stable_face_augmentation import halfspaces
from basin_scout import score
from geometry import census,halfspace_mesh,arrows

def run(parent,scout,out,limit=60,per_main=15):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);p=parent_data(parent);P,Q,C,N,A=p['P'],p['Q'],p['C'],p['N'],p['area'];S=np.flatnonzero(arrows(Q).max(1)<0);limits=[]
    for c,n in zip(C,N):
        aa=P@c-c@c;bb=2*c@n-P@n;good=aa>1e-12;roots=2*aa[good]/(bb[good]+np.sqrt(bb[good]**2+4*aa[good]));limits.append(.95*max(roots,default=0))
    limits=np.array(limits);eligible=[i for i in range(len(Q)) if i not in S and limits[i]>1e-5 and len(p['faces'][i])<=7];triples=[];inverse=[];cost=[]
    for tri in itertools.combinations(eligible,3):
        if any(set(p['faces'][i])&set(p['faces'][j]) for i,j in itertools.combinations(tri,2)):continue
        B=(A[list(tri),None]*C[list(tri)]/3).T
        if abs(np.linalg.det(B))<1e-13:continue
        triples.append(tri);inverse.append(np.linalg.inv(B));cost.append(sum(len(p['faces'][i]) for i in tri))
    triples=np.array(triples,int);inverse=np.array(inverse);cost=np.array(cost);rs=json.loads((pathlib.Path(scout)/'history.json').read_text());rs=sorted([r for r in rs if 'E' in r and 17<=r['E']<240],key=lambda r:r['referenceQmax'])[:limit];history=[];best=1.;start=time.time();(out/'definition.json').write_text(json.dumps(dict(parent=str(pathlib.Path(parent).resolve()),parent_audit_sha256=hashlib.sha256((pathlib.Path(parent)/'audit.json').read_bytes()).hexdigest(),scout=str(pathlib.Path(scout).resolve()),main_candidates=[r['sample'] for r in rs],compensation_triples=len(triples),cap_bound='95 percent of the maximal old-vertex escape-ball height; not the one-facet visibility radius',scope='Numerical literal physical additions; exact audit required'),indent=2));print('MULTICAP_COMPENSATION_TRIPLES',len(triples),'MAINS',len(rs),flush=True)
    for rank,r in enumerate(rs):
        # Both parents are the same physical checkpoint to floating accuracy;
        # nominal coordinates are explicitly re-evaluated against this exact
        # parent's centred numerical realization before any use.
        main=np.array(r['added_points']);escape=(main[:,None,:]*(P[None,:,:]-main[:,None,:])).sum(2).max(1)
        if escape.min()<=1e-9:continue
        _,moment,_=mass(np.r_[P,main],[],[]);guess=np.einsum('tij,j->ti',inverse,-moment);avail=(Q@main.T<1-1e-9).all(1);valid=(guess>0).all(1)&(guess<limits[triples]).all(1)&avail[triples].all(1)&(r['E']+cost<253);ids=np.flatnonzero(valid);ids=ids[np.argsort(np.max(guess[ids]/limits[triples[ids]],axis=1))[:per_main]];row=dict(rank=rank,sample=r['sample'],initial_E=r['E'],positive_initial_guesses=len(ids),tested=[])
        for index in ids:
            tri=triples[index];c=C[tri];n=N[tri];d=guess[index].copy();moving=np.arange(len(P)+len(main),len(P)+len(main)+3)
            try:
                for it in range(25):
                    points=np.r_[main,c+d[:,None]*n];X=np.r_[P,points];V,M,J=mass(X,moving,n)
                    if np.linalg.norm(M)/V<1e-13:break
                    step=np.linalg.solve(J,-M);accepted=False
                    for bt in range(15):
                        dd=d+step*2**-bt
                        if not ((dd>0)&(dd<limits[tri])).all():continue
                        VV,MM,_=mass(np.r_[P,main,c+dd[:,None]*n],moving,n)
                        if np.linalg.norm(MM)<np.linalg.norm(M):d=dd;accepted=True;break
                    if not accepted:raise ValueError('full physical first-moment correction stalled')
                if np.linalg.norm(M)/V>1e-12:raise ValueError('actual first moment did not close')
                H=halfspaces(X);body=halfspace_mesh(H);own=census(body,0);ss=score(H);item=dict(triple=int(index),balancing_facets=tri.tolist(),heights=d.tolist(),centroid_norm=float(np.linalg.norm(body['g'])),**ss);item.update(own);row['tested'].append(item)
                if not 17<=own['E']<249:continue
                if own['U']!=1:raise ValueError('balanced reference-escape construction lost actual uniqueU')
                folder=out/f'main{r["sample"]:05d}-triple{int(index):05d}';folder.mkdir();np.savez(folder/'body.npz',X=X,Q=H,added_points=points);(folder/'summary-numerical.json').write_text(json.dumps(item,indent=2));recipe=dict(parent_audit=str((pathlib.Path(parent)/'audit.json').resolve()),parent_audit_sha256=hashlib.sha256((pathlib.Path(parent)/'audit.json').read_bytes()).hexdigest(),parent_frame='raw',added_points=[[str(x) for x in row] for row in points+p['centroid']],scope='New rational literal extension in the exact raw parent frame; full exact audit required');(folder/'construction.json').write_text(json.dumps(recipe,indent=2))
                if own['S']==own['U']==1 and min(own['min_primal_nonroot'],own['min_polar_nonroot'])>1e-9:
                    (out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(construction=str((folder/'construction.json').resolve())),indent=2));history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));return
                value=max(ss['Q'],default=0)
                if own['S']==2 and value<best:best=value;(out/'best-own211.json').write_text(json.dumps(dict(folder=str(folder.resolve()),**item),indent=2));print('MULTICAP_BALANCED_OWN211',best,own['E'],flush=True)
            except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError) as err:row['tested'].append(dict(triple=int(index),error=repr(err)))
        history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));print('MULTICAP_BALANCE_MAIN',rank,r['sample'],'tried',len(ids),'best',best,'seconds',time.time()-start,flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--parent',required=True);p.add_argument('--scout',required=True);p.add_argument('--out',required=True);p.add_argument('--limit',type=int,default=60);p.add_argument('--per-main',type=int,default=15);a=p.parse_args();run(a.parent,a.scout,a.out,a.limit,a.per_main)
