"""Physical support flow through changing hull incidences with numerical211 guards.
All supplied supports are actual halfspaces; every accepted state reconstructs
their full intersection, integrates uniform mass and centres its polar normals.
The source must be a simple body. N<=84 bounds genuine E<=246 regardless of
future hull changes. Strict/weak acceptance is reserved for the exact auditor.
"""
import sys,json,time,hashlib
from pathlib import Path
import numpy as np
from scipy.linalg import svd
from scipy.spatial import QhullError
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,eye,hstack,vstack
from gmpy2 import mpq
import jax,jax.numpy as jnp
from support_persistence import ROOT,barcode,edge_graphs
from support_search import complex_for
from geometry import angular_scores

@jax.jit
def physical(H,ds,tr,tm):
    X=jnp.linalg.solve(H[ds],jnp.ones((len(ds),3,1))).squeeze(-1)
    a,b,c=X[tr[:,0]],X[tr[:,1]],X[tr[:,2]]
    six=jnp.sum(a*jnp.cross(b,c),axis=1)*tm
    g=jnp.sum(six[:,None]*(a+b+c),axis=0)/(4*six.sum())
    return X,X-g,H/(1-H@g)[:,None],g,six.sum()/6

@jax.jit
def pieces(H,ds,tr,tm,up,sp,p,w):
    X,Z,Q,g,v=physical(H,ds,tr,tm)
    def angles(A,ix):
        d=A[ix]-A
        return jnp.sum(A*d,axis=1)/jnp.sqrt(jnp.maximum(jnp.sum(A*A,axis=1)*jnp.sum(d*d,axis=1),1e-40))
    root,a,b=Q[p[:,0]],Q[p[:,1]],Q[p[:,2]]
    d=b-a;t=jnp.clip(-jnp.sum(a*d,axis=1)/jnp.maximum(jnp.sum(d*d,axis=1),1e-40),0,1)
    birth=jnp.sum(root*root,axis=1);depth=jnp.maximum(birth-jnp.sum((a+t[:,None]*d)**2,axis=1),0)*w/birth
    return jnp.r_[angles(Z,up),angles(Q,sp),jnp.sum(depth*depth),Z.ravel(),Q.ravel()]

jacobian=jax.jit(jax.jacfwd(pieces,argnums=0))

def state(H,allowed=None):
    ds,xm,tr,tm,ym=complex_for(H)
    X,Z,Q,g,v=map(np.asarray,physical(H,ds,tr,tm))
    if v<=0 or not np.isfinite(X).all():raise ValueError('invalid mass/intersection')
    eu,es=edge_graphs(ds,xm)
    p,w,bars=barcode(Q,ym,es)
    us=angular_scores(Z);us[:,xm==0]=-np.inf
    ss=angular_scores(Q);ss[:,ym==0]=-np.inf
    up=us.argmax(1);sp=ss.argmax(1);guards=np.r_[us[np.arange(len(Z)),up],ss[np.arange(len(Q)),sp]]
    ur=int(np.argmax(np.where(xm>0,np.sum(Z*Z,1),-np.inf)))
    if allowed is None:allowed=[int(np.argmax(np.where(ym>0,np.sum(Q*Q,1),-np.inf))),int(p[np.argmax(bars),0])]
    active=np.r_[xm.astype(bool),ym.astype(bool)];active[ur]=False;active[len(Z)+np.array(allowed)]=False
    raw=np.asarray(pieces(H,ds,tr,tm,up,sp,p,w));nm=len(guards)
    return dict(H=H,X=X,Z=Z,Q=Q,g=g,v=float(v),ds=ds,xm=xm,tr=tr,tm=tm,ym=ym,up=up,sp=sp,p=p,w=w,
                guards=guards,active=active,allowed=allowed,nm=nm,loss=float(raw[nm]),minimum=float(guards[active].min()),
                S=int(((guards[len(Z):]<0)&(ym>0)).sum()),U=int(((guards[:len(Z)]<0)&(xm>0)).sum()),
                V=int(xm.sum()),F=int(ym.sum()),cells={tuple(sorted(map(int,t))) for t in ds[xm>0]})

def run(src,out,iters=1500,eps=1e-7):
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False);raw=src.read_bytes()
    if src.suffix=='.npy':H=np.load(src).copy()
    else:
        r=json.loads(raw);g=np.array([float(mpq(x)) for x in r['raw_centroid']]);H=np.array([[float(mpq(x,mpq(h))) for x in n] for n,h in zip(r['normals'],r['offsets'])]);H=H/(1-H@g)[:,None]
    assert len(H)<=84
    np.save(out/'source.npy',H);(out/'provenance.json').write_text(json.dumps(dict(source=str(src),source_sha256=hashlib.sha256(raw).hexdigest(),eps=eps),indent=2)+'\n')
    first=state(H);allowed=first['allowed'];H=first['Q']*np.max(np.linalg.norm(first['Z'][first['xm']>0],axis=1))
    n=len(H);D=3*n;trust=.02;history=[];events=[];start=time.time()
    (out/'allowed_support_roots.json').write_text(json.dumps(allowed)+'\n')
    def Jmatrix(A,s):return np.asarray(jacobian(A,s['ds'],s['tr'],s['tm'],s['up'],s['sp'],s['p'],s['w'])).reshape(-1,D)
    def metric(s,J):
        G=J[s['nm']+1:];nx=3*len(s['Z']);M=np.vstack([G[:nx]/np.sqrt(np.mean(s['Z']**2)),G[nx:]/np.sqrt(np.mean(s['Q']**2)),np.eye(D)*.05])
        _,d,Vt=svd(M,full_matrices=False,check_finite=False);return Vt.T/d
    def retract(A,radius,W):
        for correction in range(10):
            try:s=state(A,allowed)
            except (ValueError,QhullError,np.linalg.LinAlgError,AssertionError):return None
            if s['minimum']>.999*eps:return A
            J=Jmatrix(A,s);C=J[:s['nm']][s['active']]@W;rhs=s['guards'][s['active']]-eps;bound=radius/np.sqrt(D)
            keep=rhs<=bound*np.sum(abs(C),axis=1)+1e-10;C=C[keep];rhs=rhs[keep];I=eye(D)
            M=vstack([hstack([-csr_matrix(C*1000),csr_matrix((len(C),D))]),hstack([I,-I]),hstack([-I,-I])],format='csr')
            opt=linprog(np.r_[np.zeros(D),np.ones(D)],A_ub=M,b_ub=np.r_[rhs*1000,np.zeros(2*D)],bounds=[(-bound,bound)]*D+[(0,None)]*D,method='highs-ipm',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-9,time_limit=10.))
            if not opt.success:return None
            A=A+(W@opt.x[:D]).reshape(n,3)
        return None
    first=state(H,allowed)
    if first['minimum']<.999*eps:
        A=retract(H,.05,metric(first,Jmatrix(H,first)))
        if A is None:raise ValueError('initial strict physical support correction failed')
        H=A
    for it in range(iters):
        s=state(H,allowed);row={k:s[k] for k in ['S','U','V','F','loss','minimum']};row.update(it=it,Q=float(np.sqrt(s['loss'])),trust=trust,seconds=time.time()-start)
        history.append(row);np.save(out/'latest.npy',H);(out/'history.json').write_text(json.dumps(history,indent=2)+'\n')
        if it%5==0:print('FREE_SUPPORT_STRICT211',row,flush=True)
        if s['S']==s['U']==1:
            np.save(out/'NUMERICAL_NOMINATION.npy',H);(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');print('NUMERICAL_REQUIRES_EXACT',row,flush=True);break
        if s['S']>2 or s['U']>1 or s['minimum']<.8*eps:raise ValueError('strict own constraint failure')
        J=Jmatrix(H,s);W=metric(s,J);C=J[:s['nm']][s['active']]@W;rhs=s['guards'][s['active']]-eps;bound=trust/np.sqrt(D);keep=rhs<=bound*np.sum(abs(C),axis=1)+1e-10
        opt=linprog(J[s['nm']]@W,A_ub=-C[keep]*1000,b_ub=rhs[keep]*1000,bounds=[(-bound,bound)]*D,method='highs-ipm',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-9,time_limit=10.))
        if not opt.success:
            trust*=.5
            if trust<1e-11:break
            continue
        step=(W@opt.x).reshape(n,3);accepted=False
        for back in range(18):
            trial=retract(H+2**-back*step,max(trust*2**-back,1e-7),W)
            if trial is None:continue
            try:
                t=state(trial,allowed);trial=t['Q']*np.max(np.linalg.norm(t['Z'][t['xm']>0],axis=1));t=state(trial,allowed)
            except (ValueError,QhullError,np.linalg.LinAlgError,AssertionError):continue
            if t['minimum']<.9*eps or t['S']>2 or t['U']>1:continue
            if t['loss']<s['loss']-1e-12*max(1,s['loss']):
                removed=s['cells']-t['cells'];added=t['cells']-s['cells']
                if removed or added:
                    name=f'event_{len(events):04d}_it{it}';np.save(out/(name+'.npy'),trial);event=dict(it=it,coordinates=name+'.npy',removed=[list(x) for x in sorted(removed)],added=[list(x) for x in sorted(added)],Q=float(np.sqrt(t['loss'])),V=t['V'],F=t['F']);events.append(event);(out/'events.json').write_text(json.dumps(events,indent=2)+'\n');print('TRUE_SUPPORT_EVENT',name,len(removed),len(added),'Q',event['Q'],flush=True)
                H=trial;accepted=True;row['alpha']=2**-back;break
        if accepted and back==0:trust=min(.25,trust*1.4)
        if not accepted:trust*=.4
        if trust<1e-11:print('FINITE_FLOW_STALLED',row,flush=True);break
    np.save(out/'final.npy',H)
    return H

if __name__=='__main__':run(ROOT/sys.argv[1],ROOT/sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 1500,float(sys.argv[4]) if len(sys.argv)>4 else 1e-7)
