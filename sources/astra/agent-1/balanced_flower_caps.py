"""Uniform-mass-balanced literal convex-hull additions inside escape balls.

For a reference-centred mono-unstable polytope, a new point inside a diameter
ball B(w/2,|w|/2), w an old vertex, has a strict escape to w. All old escape
witnesses remain in the enlarged hull, and the old farthest vertex stays the
unique reference maximum. Three disjoint small facet pyramids are used to
cancel the first moment added by a purposeful point beyond the unwanted stable
face. This reference lemma is never substituted for the actual-centroid audit.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,json,pathlib,time,itertools,hashlib
from fractions import Fraction
import numpy as np
from scipy.spatial import QhullError
from geometry import halfspace_mesh,arrows,census
from stable_face_augmentation import halfspaces
from basin_scout import score

def parent_data(folder,cap_fraction=.2):
    folder=pathlib.Path(folder);a=json.loads((folder/'audit.json').read_text());H=json.loads((folder/'H.json').read_text())['H'];Q=np.array([[float(Fraction(int(v),int(row[3]))) for v in row[:3]] for row in H]);m=halfspace_mesh(Q);P=m['X']-m['g'];Q=Q[m['active']];Q=Q/(1-Q@m['g'])[:,None];faces=m['faces'];norm=np.linalg.norm(Q,axis=1);N=Q/norm[:,None];C=[];area=[]
    for cy in faces:
        x=P[cy];cross=np.cross(x[1:-1]-x[0],x[2:]-x[0]);areas=np.linalg.norm(cross,axis=1)/2;C.append((areas[:,None]*(x[0]+x[1:-1]+x[2:])/3).sum(0)/areas.sum());area.append(areas.sum())
    C=np.array(C);area=np.array(area);limits=[]
    for f,c in enumerate(C):
        delta=Q@N[f];gap=1-Q@c;mask=(delta>1e-12);mask[f]=False;geometric=np.min(gap[mask]/delta[mask])
        A=P@c-c@c;B=2*c@N[f]-P@N[f];allowed=np.where(A>0,2*np.maximum(A,0)/(B+np.sqrt(B*B+4*np.maximum(A,0))),0);flower=float(allowed.max());limits.append(cap_fraction*min(geometric,flower))
    return dict(folder=folder,audit=a,P=P,Q=Q,faces=faces,edges=len(m['edges']),N=N,C=C,area=area,limits=np.array(limits),centroid=m['g'])

def run(parent,out,samples=600,seed=97619):
    p=parent_data(parent);P,Q,C,N,A=p['P'],p['Q'],p['C'],p['N'],p['area'];out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);rng=np.random.default_rng(seed);S=np.flatnonzero(arrows(Q).max(1)<0);U=np.flatnonzero(arrows(P).max(1)<0);assert len(U)==1 and len(S)==2
    elder=int(np.argmax((Q*Q).sum(1)));junior=next(int(i) for i in S if i!=elder);n=N[junior];height=1/np.linalg.norm(Q[junior]);u=P[U[0]];basis=u-n*(n@u);basis/=np.linalg.norm(basis);other=np.cross(n,basis);witnesses=np.flatnonzero((P@n+np.linalg.norm(P,axis=1))/2>height+1e-10);eligible=[f for f in range(len(Q)) if f not in S and p['limits'][f]>1e-7 and len(p['faces'][f])<=6];triples=[];inverse=[];cost=[]
    for tri in itertools.combinations(eligible,3):
        total=sum(len(p['faces'][i]) for i in tri)
        if total>248-p['edges']-3:continue
        if any(set(p['faces'][i])&set(p['faces'][j]) for i,j in itertools.combinations(tri,2)):continue
        B=(A[list(tri),None]*C[list(tri)]/3).T
        if abs(np.linalg.det(B))<1e-14:continue
        triples.append(tri);inverse.append(np.linalg.inv(B));cost.append(total)
    triples=np.array(triples,int);inverse=np.array(inverse);cost=np.array(cost);history=[];start=time.time();best=1.
    (out/'definition.json').write_text(json.dumps(dict(parent=str(pathlib.Path(parent).resolve()),parent_audit_sha256=hashlib.sha256((pathlib.Path(parent)/'audit.json').read_bytes()).hexdigest(),seed=seed,eligible_facets=eligible,balancing_triples=len(triples),junior=junior,scope='Numerical first-moment-balanced physical hull additions; every candidate requires an exact audit'),indent=2));np.savez(out/'parent.npz',X=P,Q=Q,centroid=p['centroid']);print('BALANCE_TRIPLES',len(triples),'FACETS',len(eligible),flush=True)
    if not len(triples):return
    for k in range(samples):
        w=P[int(rng.choice(witnesses))];top=(n@w+np.linalg.norm(w))/2;depth=10**rng.uniform(-6,-.3);h=height+depth*(top-height);radius=np.sqrt(max(0,(w@w)/4-(h-n@w/2)**2));angle=rng.uniform(0,2*np.pi);rad=radius*np.sqrt(rng.random())*.999;v=w/2+n*(h-n@w/2)+rad*(np.cos(angle)*basis+np.sin(angle)*other)
        try:
            mainQ=halfspaces(np.r_[P,v[None]]);main=halfspace_mesh(mainQ);E=len(main['edges']);moment=main['g']*main['volume'];delta=np.einsum('tij,j->ti',inverse,-moment);available=(Q@v<=1-1e-8);valid=(delta>0).all(1)&(delta<p['limits'][triples]).all(1)&available[triples].all(1)&(E+cost<249)
            ids=np.flatnonzero(valid);row=dict(sample=k,main_E=E,main_moment=moment.tolist(),linear_balance_options=len(ids),seconds=time.time()-start)
            if not len(ids):history.append(row);continue
            # Small caps minimize interaction and preserve a sizeable interior
            # margin in their analytic one-facet visibility domains.
            rank=ids[np.argsort(np.max(delta[ids]/p['limits'][triples[ids]],axis=1))[:5]]
            for t in rank:
                tri=triples[t];d=delta[t].copy();c=C[tri];nn=N[tri];aa=A[tri]
                for _ in range(10):
                    residual=moment+np.sum((aa*d/3)[:,None]*(c+d[:,None]*nn/4),axis=0)
                    if np.linalg.norm(residual)<1e-15:break
                    J=((aa/3)[:,None]*(c+d[:,None]*nn/2)).T;d-=np.linalg.solve(J,residual)
                if not ((d>0)&(d<p['limits'][tri])).all():continue
                caps=c+d[:,None]*nn;points=np.r_[v[None],caps];newX=np.r_[P,points];newQ=halfspaces(newX);body=halfspace_mesh(newQ);cc=census(body,0);error=float(np.linalg.norm(body['g']))
                if error>1e-10:continue # The individual pyramids did not add independently.
                if not 17<=cc['E']<249:continue
                r=score(newQ);value=max(r['Q'],default=0);record=dict(sample=k,balancing_facets=tri.tolist(),heights=d.tolist(),centroid_norm=error,point_escapes=arrows(np.r_[P,points])[-4:,:len(P)].max(1).tolist(),**r);row.setdefault('balanced_bodies',[]).append(record)
                if cc['U']!=1:raise ValueError('actual-centre census failed the balanced escape construction')
                folder=out/f'candidate{k:05d}-triple{int(t):05d}';folder.mkdir();np.savez(folder/'body.npz',Q=newQ,X=newX,added_points=points);(folder/'construction.json').write_text(json.dumps(dict(parent_audit=str((p['folder']/'audit.json').resolve()),parent_audit_sha256=hashlib.sha256((p['folder']/'audit.json').read_bytes()).hexdigest(),parent_translation='Subtract the exact audited volume centroid from every exact raw parent vertex',added_points=[[str(x) for x in r] for r in points],scope='Literal rational point additions to the exact centred parent; this recipe defines a body for subsequent exact auditing'),indent=2));(folder/'summary-numerical.json').write_text(json.dumps(record,indent=2))
                if cc['S']==1 and min(cc['min_primal_nonroot'],cc['min_polar_nonroot'])>1e-9:
                    (out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(construction=str((folder/'construction.json').resolve()),input=str((folder/'body.npz').resolve())),indent=2));history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));print('POTENTIAL_BALANCED_OWN110_REQUIRES_EXACT',record,flush=True);return
                if cc['S']==2 and value<best:
                    best=value;(out/'best.json').write_text(json.dumps(dict(folder=str(folder.resolve()),**record),indent=2));print('BALANCED_CAP_BEST',json.dumps(record),flush=True)
        except (ValueError,AssertionError,QhullError,np.linalg.LinAlgError) as err:row=dict(sample=k,error=repr(err))
        history.append(row)
        if k%10==0:(out/'history.json').write_text(json.dumps(history,indent=2));print('BALANCED_CAP_SCREEN',k,'best_Q',best,flush=True)
    (out/'history.json').write_text(json.dumps(history,indent=2));print('FINITE_BALANCED_CAP_SCREEN_COMPLETE',len(history),best,flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--parent',required=True);ap.add_argument('--out',required=True);ap.add_argument('--samples',type=int,default=600);ap.add_argument('--seed',type=int,default=97619);a=ap.parse_args();run(a.parent,a.out,a.samples,a.seed)
