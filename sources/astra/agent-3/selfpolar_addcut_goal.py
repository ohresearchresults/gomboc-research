"""Independent rational Jensen add-and-cut construction and physical search.

The tetrahedron is an unscored construction scaffold. Search begins at N>=10.
N vertices = N maximal facets, E=2N-2; N<=125 gives both complexities <500.
Every O(4) Cayley section change defines a new uniformly filled physical body.
The numerical origin-centroid residual is NOT a certificate; exact final mass
and complete native contact census on the rational construction decide success.
"""
from pathlib import Path
import argparse, json, time
from collections import Counter
import numpy as np
from support_geometry import escape
from dual_shadow_goal import bars


def topology(X,D):
    n=len(X);faces=[];owners={}
    if D.shape!=(n,n) or not np.array_equal(D,D.T) or np.any(np.diag(D)):
        raise ValueError('invalid self-polar contact matrix')
    for f in range(n):
        ids=np.flatnonzero(D[f]);p=X[ids]
        if len(ids)<3:raise ValueError('facet has fewer than three vertices')
        normal=-X[f]/np.linalg.norm(X[f]);e=np.eye(3)[np.argmin(abs(normal))];e-=normal*(e@normal);e/=np.linalg.norm(e);t=np.cross(normal,e);c=p.mean(0);a=np.arctan2((p-c)@t,(p-c)@e);cy=ids[np.argsort(a)].tolist();faces.append(cy)
        for i,j in zip(cy,cy[1:]+cy[:1]):owners.setdefault(tuple(sorted((i,j))),[]).append(f)
    if len(owners)!=2*n-2 or any(len(v)!=2 for v in owners.values()):
        raise ValueError('nonmanifold or non-self-dual incidence')
    edges=np.array(sorted(owners));tris=np.array([(cy[0],cy[j],cy[j+1])for cy in faces for j in range(1,len(cy)-1)])
    return dict(faces=faces,edges=edges,tris=tris)


def mass(X,T):
    a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];v6=np.einsum('ij,ij->i',a,np.cross(b,c));V=v6.sum()/6;s=a+b+c
    if V<=0:raise ValueError('nonpositive oriented volume')
    g=(v6[:,None]*s).sum(0)/(24*V)
    M=(np.einsum('i,ij,ik->jk',v6,a,a)+np.einsum('i,ij,ik->jk',v6,b,b)+np.einsum('i,ij,ik->jk',v6,c,c)+np.einsum('i,ij,ik->jk',v6,s,s))/(120*V)
    return V,g,M


def cayley(X,b):
    b2=b@b;xb=X@b;den=1-b2-2*xb
    if min(den)<=0:raise ValueError('nonpositive O4 section denominator')
    return ((1+b2)*X+2*b-2*xb[:,None]*b)/den[:,None]


def center(X,T):
    X=X.copy();history=[]
    for _ in range(35):
        V,g,M=mass(X,T);res=np.linalg.norm(g)
        if res<3e-14:return X,history
        J=2*(np.eye(3)+5*M-4*np.outer(g,g));b=np.linalg.solve(J,-g);ok=False
        for k in range(24):
            step=2.**-k*b
            try:Y=cayley(X,step)
            except ValueError:continue
            if np.linalg.norm(mass(Y,T)[1])<res*(1-1e-5):
                X=Y;history.append(dict(kind='cayley',b=step.tolist()));ok=True;break
        if not ok:raise ValueError('O4 physical centroid closure failed to descend')
    raise ValueError('O4 physical centroid closure exceeded iteration limit')


def audit_numeric(X,D,top=None):
    top=topology(X,D)if top is None else top;V,g,M=mass(X,top['tris']);contact=1+X@X.T
    resid=float(max(abs(contact[D])));slack=float(min(contact[~D]));turns=[]
    for f,cy in enumerate(top['faces']):
        P=X[cy];ed=np.roll(P,-1,axis=0)-P;turns.extend(np.cross(ed,np.roll(ed,-1,axis=0))@(-X[f]))
    turn=float(min(turns))
    if resid>3e-9 or slack<=1e-12 or turn<=1e-15:
        raise ValueError(f'numerical contact cell unresolved: residual={resid}, slack={slack}, turn={turn}')
    Z=X-g;H=-X/(1+X@g)[:,None];vp,_=escape(Z);vq,_=escape(H);P=bars(dict(Z=Z,edges=top['edges']),False)[0]
    # The dual edge graph is the negative-polar image of this same graph.
    Q=bars(dict(Z=H,edges=top['edges']),False)[0]
    r=int(np.argmax(np.sum(Z*Z,axis=1)));s=int(np.argmax(np.sum(H*H,axis=1)))
    return dict(N=len(X),V=len(X),F=len(X),E=len(top['edges']),S=int(sum(vq<0)),U=int(sum(vp<0)),Pmax=float(max(P,default=0)),Qmax=float(max(Q,default=0)),Psum=float(sum(P)),Qsum=float(sum(Q)),positive_P=len(P),positive_Q=len(Q),centroid=g.tolist(),centroid_norm=float(np.linalg.norm(g)),min_noncontact=slack,contact_residual=resid,min_turn=turn,min_nonroot_escape=float(min(np.delete(vp,r))),min_nonstable_escape=float(min(np.delete(vq,s))),root=r,unstable_ids=np.flatnonzero(vp<0).tolist(),volume=float(V)),top


def addcut(X,D,top,k,weights,fraction,score=True):
    face=np.flatnonzero(D[k]);w=np.asarray(weights);y=w@X[face]/sum(w);dots=X@y;mask=(np.arange(len(X))!=k)&(dots<0)
    tmax=float(min(-1/dots[mask]-1))if np.any(mask)else float('inf')
    t=fraction*tmax if np.isfinite(tmax)else fraction/(1-fraction)
    if not(0<t<tmax)or t<1e-10:raise ValueError('add-cut interval collapsed')
    x=(1+t)*y;s=X@x
    if s[k]>=-1 or min(np.delete(s,k))<=-1:raise ValueError('apex violates Jensen Corollary7.5 hypotheses')
    nbr=list(map(int,sorted(set(top['edges'][np.any(top['edges']==k,axis=1)].ravel())-{k})));old=np.array([i for i in range(len(X))if i!=k]);z=np.array([X[k]+((-1-s[k])/(s[j]-s[k]))*(X[j]-X[k])for j in nbr]);Y=np.vstack((X[old],x,z));n=len(X);N=len(Y);DD=np.zeros((N,N),bool);DD[:n-1,:n-1]=D[np.ix_(old,old)];DD[n-1,n:]=True;DD[n:,n-1]=True
    for h,j in enumerate(nbr):
        contacts=D[k,old]&D[j,old];DD[n+h,:n-1]=contacts;DD[:n-1,n+h]=contacts
    tt=topology(Y,DD);Y,h=center(Y,tt['tris']);row=audit_numeric(Y,DD,tt)[0]if score else None
    op=dict(kind='addcut',vertex=int(k),face=face.tolist(),weights=w.tolist(),t=float(t),fraction=float(fraction),interval='finite'if np.isfinite(tmax)else 'unbounded',edge_neighbors=nbr)
    return Y,DD,tt,[op]+h,row


def scaffold(rng):
    X=np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],float);D=~np.eye(4,dtype=bool);top=topology(X,D);hist=[]
    # No equilibrium objective is evaluated below the permitted search bound.
    while len(X)<10:
        k=int(rng.integers(len(X)));w=rng.uniform(.2,1,len(np.flatnonzero(D[k])))
        X,D,top,h,row=addcut(X,D,top,k,w,.4,score=False);hist+=h
    row,top=audit_numeric(X,D,top)
    return dict(X=X,D=D,top=top,history=hist,row=row)


def save(state,out):
    out=Path(out);out.mkdir(parents=True,exist_ok=True);np.savez(out/'body.npz',X=state['X'],D=state['D']);(out/'construction.json').write_text(json.dumps(dict(scaffold=[[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],operations=state['history'],definition='Every stored binary64 control is its exact dyadic rational; normalize each weights array by its exact sum. Jensen add-cut then rational O4 Cayley section changes. Uniform mass belongs to the final physical 3D body.'),indent=2));(out/'numeric.json').write_text(json.dumps(state['row'],indent=2));(out/'incidence.json').write_text(json.dumps(dict(faces=state['top']['faces'],edges=state['top']['edges'].tolist()),indent=2))


def run(out,seed=91731,width=5,trials=120):
    out=Path(out);out.mkdir(exist_ok=False,parents=True);rng=np.random.default_rng(seed);beam=[scaffold(rng)for _ in range(width)];start=time.time();trace=[];counter=0;errors=Counter();best=None
    (out/'definition.json').write_text(json.dumps(dict(seed=seed,width=width,trials=trials,source='https://arxiv.org/html/1902.00784',theorem='Corollary7.5',maximum_vertices=125,minimum_search_vertices=10,maximum_edges=248),indent=2))
    for level in range(42):
        candidates=[]
        for bi,st in enumerate(beam):
            X,D,top=st['X'],st['D'],st['top'];row=st['row'];root=row['root'];u=[i for i in row['unstable_ids']if i!=root]
            degrees=np.bincount(top['edges'].ravel(),minlength=len(X));valid=np.flatnonzero(len(X)+degrees<=125)
            if not len(valid):continue
            for trial in range(trials):
                counter+=1
                choice=[k for k in u if k in valid] if trial%5 else valid
                if not len(choice):choice=valid
                k=int(rng.choice(choice));nf=int(sum(D[k]));conc=[.25,.6,1.,2.,5.][trial%5];w=rng.dirichlet(np.full(nf,conc));frac=float(rng.choice([.03,.15,.35,.6,.85,.97,.997,.9999])) if trial%3 else float(rng.uniform(.05,.999))
                try:Y,DD,tt,h,rr=addcut(X,D,top,k,w,frac)
                except(ValueError,np.linalg.LinAlgError)as e:errors[str(e).split(':')[0]]+=1;continue
                state=dict(X=Y,D=DD,top=tt,history=st['history']+h,row=rr);rr.update(level=level,parent=bi,trial=trial,call=counter,seed=seed);candidates.append(state)
                if rr['S']==rr['U']==1:
                    save(state,out/f'potential_{counter:07d}');raise RuntimeError('Physical numerical110 nomination saved; exact rational replay required before any success claim')
                key=(rr['S']+rr['U'],rr['Pmax']+rr['Qmax'],rr['Psum']+rr['Qsum'])
                if best is None or key<best:
                    best=key;save(state,out/'best');print('SELFPOLAR_NEW_BEST',rr,flush=True)
        if not candidates:break
        keys=[lambda s:(s['row']['U']+s['row']['S'],s['row']['Pmax']+s['row']['Qmax'],s['row']['Psum']+s['row']['Qsum']),lambda s:(s['row']['Pmax']+s['row']['Qmax'],s['row']['U']+s['row']['S']),lambda s:(s['row']['Psum']+s['row']['Qsum'],s['row']['U']+s['row']['S'])]
        chosen=[]
        for key in keys:
            for c in sorted(candidates,key=key):
                if all(c['row']['call']!=z['row']['call']for z in chosen):chosen.append(c);break
        for c in sorted(candidates,key=keys[0]):
            if len(chosen)>=width:break
            if all(c['row']['call']!=z['row']['call']for z in chosen):chosen.append(c)
        beam=chosen[:width]
        for j,c in enumerate(beam):save(c,out/f'level{level:02d}'/f'beam{j}')
        rr=dict(level=level,calls=counter,seconds=time.time()-start,beam=[c['row']for c in beam],errors=dict(errors));trace.append(rr);(out/'trace.json').write_text(json.dumps(trace,indent=2));print('SELFPOLAR_LEVEL',level,counter,[(r['row']['N'],r['row']['S'],r['row']['U'],r['row']['Pmax'])for r in beam],time.time()-start,flush=True)
    print('SELFPOLAR_FINITE_BATCH_END',counter,best,dict(errors),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('out');p.add_argument('--seed',type=int,default=91731);p.add_argument('--width',type=int,default=5);p.add_argument('--trials',type=int,default=120);a=p.parse_args();run(a.out,a.seed,a.width,a.trials)
