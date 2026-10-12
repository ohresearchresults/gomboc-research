"""Free physical point flow across genuine convex-hull contact events.

Every accepted trial is re-hulled and its uniform volume centroid recomputed.
We preserve numerical exclusion margins for all but one stable and two unstable
equilibria, but impose no fixed facet-incidence inequalities.  The objective is
the complete squared relative primal persistence, without a positive-bar cutoff.
Changing integration triangles alone is not treated as a geometric improvement.
All outputs are numerical candidates until a separate exact physical audit.
"""
import sys, json, time, hashlib
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull, QhullError
from scipy.optimize import linprog
from scipy.sparse import csr_matrix, eye, hstack, vstack
import jax
import jax.numpy as jnp
from support_persistence import ROOT, barcode
from geometry import angular_scores

jax.config.update('jax_enable_x64', True)

def physical(X, T):
    a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]]
    six=jnp.sum(a*jnp.cross(b,c),axis=1)
    g=jnp.sum(six[:,None]*(a+b+c),axis=0)/(4*six.sum())
    Z=X-g
    Q=jnp.linalg.solve(Z[T],jnp.ones((len(T),3,1))).squeeze(-1)
    return Z,Q,g,six.sum()/6

@jax.jit
def pieces(X,T,up,sp,p,w):
    Z,Q,g,v=physical(X,T)
    def angles(A,ix):
        d=A[ix]-A
        return jnp.sum(A*d,axis=1)/jnp.sqrt(jnp.maximum(jnp.sum(A*A,axis=1)*jnp.sum(d*d,axis=1),1e-40))
    root,a,b=Z[p[:,0]],Z[p[:,1]],Z[p[:,2]]
    d=b-a
    t=jnp.clip(-jnp.sum(a*d,axis=1)/jnp.maximum(jnp.sum(d*d,axis=1),1e-40),0,1)
    birth=jnp.sum(root*root,axis=1)
    depth=jnp.maximum(birth-jnp.sum((a+t[:,None]*d)**2,axis=1),0)*w/birth
    return jnp.r_[angles(Z,up),angles(Q,sp),jnp.sum(depth*depth)]

jacobian=jax.jit(jax.jacfwd(pieces,argnums=0))

def state(X,allowed=None):
    h=ConvexHull(X)
    T=h.simplices.copy()
    a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]]
    flip=np.einsum('ij,ij->i',np.cross(b-a,c-a),h.equations[:,:3])<0
    T[flip]=T[flip][:,[0,2,1]]
    Z,Q,g,vol=map(np.asarray,physical(X,T))
    if not np.isfinite(Q).all() or vol<=0:raise ValueError('invalid physical hull')
    eu=np.unique(np.sort(np.concatenate([T[:,[0,1]],T[:,[1,2]],T[:,[2,0]]]),axis=1),axis=0)
    mask=np.zeros(len(X));mask[h.vertices]=1
    p,w,bars=barcode(Z,mask,eu)
    us=angular_scores(Z);us[:,mask==0]=-np.inf
    ss=angular_scores(Q)
    up=us.argmax(1);sp=ss.argmax(1)
    guards=np.r_[us[np.arange(len(X)),up],ss[np.arange(len(T)),sp]]
    ur=int(np.argmax(np.sum(Z*Z,1)*mask))
    sr=int(np.argmax(np.sum(Q*Q,1)))
    if allowed is None:
        allowed=[ur,int(p[np.argmax(bars),0])]
    active=np.r_[mask.astype(bool),np.ones(len(T),bool)]
    active[np.array(allowed,dtype=int)]=False;active[len(X)+sr]=False
    raw=np.asarray(pieces(X,T,up,sp,p,w))
    return dict(X=X,Z=Z,Q=Q,g=g,volume=float(vol),T=T,eu=eu,p=p,w=w,up=up,sp=sp,
                guards=guards,active=active,allowed=allowed,loss=float(raw[-1]),
                S=int((guards[len(X):]<0).sum()),U=int(((guards[:len(X)]<0)&(mask>0)).sum()),
                minimum=float(guards[active].min()),V=len(h.vertices),F=len(T),E=len(eu),
                facets={tuple(sorted(map(int,t))) for t in T})

def run(src,out,iters=1500,eps=1e-7,initial_trust=.003):
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False)
    raw=src.read_bytes();X=np.load(src).copy();assert 4<=len(X)<=84
    (out/'source.npy').write_bytes(raw)
    (out/'provenance.json').write_text(json.dumps(dict(source=str(src),source_sha256=hashlib.sha256(raw).hexdigest(),eps=eps),indent=2)+'\n')
    first=state(X);allowed=first['allowed'];X=first['Z']/np.max(np.linalg.norm(first['Z'],axis=1))
    n=len(X);D=3*n;trust=initial_trust;history=[];events=[];start=time.time()
    (out/'allowed_vertex_roots.json').write_text(json.dumps(allowed)+'\n')
    def retract(A,radius):
        for correction in range(10):
            try:s=state(A,allowed)
            except (ValueError,QhullError,np.linalg.LinAlgError):return None
            if s['minimum']>.999*eps:return A
            J=np.asarray(jacobian(A,s['T'],s['up'],s['sp'],s['p'],s['w'])).reshape(-1,D)
            C=J[:-1][s['active']];rhs=s['guards'][s['active']]-eps
            bound=radius/np.sqrt(D)
            keep=rhs <= bound*np.sum(abs(C),axis=1)+1e-10
            C=C[keep];rhs=rhs[keep];I=eye(D)
            M=vstack([hstack([-csr_matrix(C*1000),csr_matrix((len(C),D))]),hstack([I,-I]),hstack([-I,-I])],format='csr')
            opt=linprog(np.r_[np.zeros(D),np.ones(D)],A_ub=M,b_ub=np.r_[rhs*1000,np.zeros(2*D)],bounds=[(-bound,bound)]*D+[(0,None)]*D,method='highs-ipm',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-9,time_limit=10.))
            if not opt.success:return None
            A=A+opt.x[:D].reshape(n,3)
        return None
    # Explicit physical correction is permitted before the strict sequence starts.
    if state(X,allowed)['minimum']<.999*eps:
        corrected=retract(X,.05)
        if corrected is None:raise ValueError('initial strict physical correction failed')
        X=corrected
    for it in range(iters):
        s=state(X,allowed);row={k:s[k] for k in ['S','U','V','E','F','loss','minimum']}
        row.update(it=it,main_P=float(np.sqrt(s['loss'])),trust=trust,seconds=time.time()-start)
        history.append(row);np.save(out/'latest.npy',X);(out/'history.json').write_text(json.dumps(history,indent=2)+'\n')
        if it%5==0:print('FREE_HULL_STRICT121',row,flush=True)
        if s['S']==s['U']==1:
            np.save(out/'NUMERICAL_NOMINATION.npy',X);(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');print('NUMERICAL_REQUIRES_EXACT',row,flush=True);break
        if s['S']>1 or s['U']>2 or s['minimum']<.8*eps:raise ValueError('strict own constraint failure')
        J=np.asarray(jacobian(X,s['T'],s['up'],s['sp'],s['p'],s['w'])).reshape(-1,D)
        C=J[:-1][s['active']];rhs=s['guards'][s['active']]-eps;bound=trust/np.sqrt(D)
        keep=rhs <= bound*np.sum(abs(C),axis=1)+1e-10
        opt=linprog(J[-1],A_ub=-C[keep]*1000,b_ub=rhs[keep]*1000,bounds=[(-bound,bound)]*D,method='highs-ipm',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-9,time_limit=10.))
        if not opt.success:
            trust*=.5;row['LP']=opt.message
            if trust<1e-11:break
            continue
        step=opt.x.reshape(n,3);accepted=False
        for back in range(18):
            trial=retract(X+2**-back*step,max(trust*2**-back,1e-7))
            if trial is None:continue
            try:
                t=state(trial,allowed)
                # Euclidean similarity only; recalculate actual hull again.
                trial=t['Z']/np.max(np.linalg.norm(t['Z'],axis=1));t=state(trial,allowed)
            except (ValueError,QhullError,np.linalg.LinAlgError):continue
            if t['minimum']<.9*eps or t['S']>1 or t['U']>2:continue
            if t['loss']<s['loss']-1e-12*max(1,s['loss']):
                removed=s['facets']-t['facets'];added=t['facets']-s['facets']
                if removed or added:
                    name=f'event_{len(events):04d}_it{it}'
                    np.save(out/(name+'.npy'),trial)
                    event=dict(it=it,coordinates=name+'.npy',removed=[list(x) for x in sorted(removed)],added=[list(x) for x in sorted(added)],P=float(np.sqrt(t['loss'])),V=t['V'],E=t['E'],F=t['F'])
                    events.append(event);(out/'events.json').write_text(json.dumps(events,indent=2)+'\n')
                    print('TRUE_HULL_EVENT',name,len(removed),len(added),'P',event['P'],flush=True)
                X=trial;accepted=True;row['alpha']=2**-back;break
        if accepted and back==0:trust=min(.25,trust*1.4)
        if not accepted:trust*=.4
        if trust<1e-11:
            print('FINITE_FLOW_STALLED',row,flush=True);break
    np.save(out/'final.npy',X)
    return X

if __name__=='__main__':
    run(ROOT/sys.argv[1],ROOT/sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 1500,float(sys.argv[4]) if len(sys.argv)>4 else 1e-7)
