"""Own-U1 widest-tree flow with free85supports and an exact degree4 apex.

The complete polar chord graph supplies a widest-path arborescence. The LP
raises its minimum angular link, then the actual re-hulled body is integrated
and rechecked. This is an adaptation of the peer's published capacity-tree
idea to a different physical family whose non-apex incidences are unrestricted.
Chords do not count in hull complexity. Final acceptance is exact, not a score.
"""
import sys,json,time,hashlib
from pathlib import Path
import numpy as np
from scipy.linalg import svd
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,eye,hstack,vstack
from scipy.spatial import QhullError
import jax
import jax.numpy as jnp
from apex_quad_supports import state,physical,unpack,ROOT
from geometry import angular_scores

def tree(Y):
    G=angular_scores(Y);root=int(np.argmax(np.sum(Y*Y,1)));n=len(Y);capacity=np.full(n,-np.inf);capacity[root]=np.inf;parent=np.full(n,-1,int);done=np.zeros(n,bool)
    for _ in range(n):
        u=int(np.argmax(np.where(done,-np.inf,capacity)))
        if done[u] or not np.isfinite(capacity[u]) and u!=root:raise ValueError('widest tree failed reachability')
        done[u]=True
        for v in np.flatnonzero(~done):
            value=min(capacity[u],G[v,u])
            if value>capacity[v]:capacity[v]=value;parent[v]=u
    parent[root]=root;active=np.arange(n)!=root;weights=G[np.arange(n)[active],parent[active]];cap=float(weights.min())
    for i in np.flatnonzero(active):
        seen=set();v=int(i)
        while v!=root:
            if v in seen:raise ValueError('widest tree cycle')
            seen.add(v);v=int(parent[v])
    if abs(cap-float(capacity[active].min()))>1e-12:raise ValueError('tree does not realize computed bottleneck')
    return parent,active,cap

@jax.jit
def pieces(q,R,T,A,up,parent):
    X,Z,Y,g,v=physical(q,R,T,A)
    def angles(B,p):
        delta=B[p]-B;score=jnp.sum(B*delta,1)/jnp.sqrt(jnp.maximum(jnp.sum(B*B,1)*jnp.sum(delta*delta,1),1e-40));return jnp.where(p==jnp.arange(len(B)),0.,score)
    # Positive values of this dimensionless dot product are exactly the
    # non-unstability condition. Unlike the angular quotient it does not
    # divide by the length of an almost-collapsed physical edge.
    ug=jnp.sum(Z*(Z[up]-Z),1)/jnp.sum(Z*Z,1)
    return jnp.r_[ug,angles(Y,parent),Z.ravel(),Y.ravel()]
derivative=jax.jit(jax.jacfwd(pieces,argnums=0))

def independent_pieces(q,R,T,A,up,parent):
    """Independent NumPy analytic extension, for complex-step validation."""
    H=np.r_[np.c_[q[:8].reshape(4,2),np.ones(4)],q[8:].reshape(-1,3)]
    X=np.r_[[[0.,0.,1.]],np.linalg.solve(H[R[1:]],np.ones((len(R)-1,3,1))).squeeze(-1)]
    a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];six=np.sum(a*np.cross(b,c),axis=1)
    g=np.sum(six[:,None]*(a+b+c),axis=0)/(4*six.sum());Z=X-g;Y=H[A]/(1-H[A]@g)[:,None]
    ug=np.sum(Z*(Z[up]-Z),1)/np.sum(Z*Z,1)
    sg=np.zeros(len(Y),dtype=q.dtype);active=parent!=np.arange(len(Y));delta=Y[parent[active]]-Y[active]
    sg[active]=np.sum(Y[active]*delta,1)/np.sqrt(np.sum(Y[active]*Y[active],1)*np.sum(delta*delta,1))
    return np.r_[ug,sg,Z.ravel(),Y.ravel()]

def run(src,out,iters=1200,eps=1e-9):
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False);raw=src.read_bytes();q=np.load(src).copy();D=len(q);start=time.time();history=[];events=[];trust=.01
    (out/'source.npy').write_bytes(raw);(out/'source.json').write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(raw).hexdigest(),eps=eps,method='actual-mass free85support quad-apex plus complete widest escape tree',conceptual_source='agent-1/contact_persistence_flow.py capacity-tree; implemented independently here'),indent=2)+'\n')
    def model(q):
        s=state(q);Z=s['Z'];raw=np.einsum('ij,ikj->ik',Z,Z[None]-Z[:,None])/np.sum(Z*Z,1)[:,None];np.fill_diagonal(raw,-np.inf);up=raw.argmax(1)
        parent,active,capacity=tree(s['Y']);s.update(parent=parent,polar_active=active,capacity=capacity,up=up,uguards=raw[np.arange(len(Z)),up]);return s
    def jac(q,s):return np.asarray(derivative(q,s['R'],s['T'],s['A'],s['up'],s['parent']))
    def metric(s,J):
        V,F=s['V'],s['F'];G=J[V+F:];M=np.vstack([G[:3*V]/np.sqrt(np.mean(s['Z']**2)),G[3*V:]/np.sqrt(np.mean(s['Y']**2)),np.eye(D)*.05]);_,d,Vt=svd(M,full_matrices=False,check_finite=False);return Vt.T/d
    def gauge(q):
        s=state(q);u=np.array([0.,0.,1.])-s['g'];radius=np.linalg.norm(u);ez=u/radius;axis=np.eye(3)[np.argmin(abs(ez))];ex=axis-ez*(axis@ez);ex/=np.linalg.norm(ex);ey=np.cross(ez,ex);R=np.column_stack([ex,ey,ez]);H=s['H']/(1-s['H']@s['g'])[:,None];H=H@R*radius
        if abs(H[:4,2]-1).max()>1e-8:raise ValueError('gauge violates the actual apex star')
        return np.r_[H[:4,:2].ravel(),H[4:].ravel()]
    def repair(q,radius,W=None,steps=14):
        for k in range(steps):
            try:s=model(q)
            except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError):return None
            minimum=float(s['uguards'][1:].min())
            if minimum>.999*eps:return q
            J=jac(q,s)
            if W is None:W=metric(s,J)
            C=J[1:s['V']]@W;rhs=s['uguards'][1:]-eps;bound=radius/np.sqrt(D);I=eye(D);M=vstack([hstack([-csr_matrix(C*1000),csr_matrix((len(C),D))]),hstack([I,-I]),hstack([-I,-I])],format='csr');sol=linprog(np.r_[np.zeros(D),np.ones(D)],A_ub=M,b_ub=np.r_[rhs*1000,np.zeros(2*D)],bounds=[(-bound,bound)]*D+[(0,None)]*D,method='highs-ipm',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-9,time_limit=10.))
            if not sol.success:return None
            step=W@sol.x[:D];old=float(np.maximum(eps-s['uguards'][1:],0).sum());accepted=False
            for back in range(15):
                trial=q+2**-back*step
                try:t=model(trial)
                except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError):continue
                if np.maximum(eps-t['uguards'][1:],0).sum()<old*(1-1e-7):q=trial;accepted=True;break
            if not accepted:return None
        return None
    first=model(q);checkdir=np.random.default_rng(1181).normal(size=D);checkdir/=np.linalg.norm(checkdir);J=jac(q,first);args=[first[k] for k in ['R','T','A','up','parent']]
    value_error=float(np.max(abs(independent_pieces(q,*args)-np.asarray(pieces(q,*args)))))
    tests=[]
    for hh in [1e-6,1e-7,1e-8]:
        finite=(independent_pieces(q+hh*checkdir,*args)-independent_pieces(q-hh*checkdir,*args))/(2*hh)
        tests.append(dict(method='central difference',h=hh,relative_error=float(np.max(abs(finite-J@checkdir))/max(1,np.max(abs(J@checkdir))))))
    for hh in [1e-20,1e-25]:
        complex_derivative=np.imag(independent_pieces(q.astype(complex)+1j*hh*checkdir,*args))/hh
        tests.append(dict(method='complex step',h=hh,relative_error=float(np.max(abs(complex_derivative-J@checkdir))/max(1,np.max(abs(J@checkdir))))))
    (out/'directional_check.json').write_text(json.dumps(dict(value_error=value_error,tests=tests,normalization='primal dot/(radius squared); polar angular; self-parent exactly zero',scope='independent fixed-cell algebraic derivative; every accepted iterate gets a fresh physical hull'),indent=2)+'\n')
    if value_error>1e-9 or max(t['relative_error'] for t in tests)>1e-5:raise ValueError('mass/geometry derivative check failed')
    if first['uguards'][1:].min()<.999*eps:
        fixed=repair(q,.08,steps=35)
        if fixed is None:raise ValueError('initial actual-U1 preparation failed')
        q=fixed
    q=gauge(q)
    for it in range(iters):
        s=model(q);row={k:s[k] for k in ['V','E','F','S','U','Pmax','Qmax','capacity','minimum_noncontact']};row.update(it=it,minimum_U_guard=float(s['uguards'][1:].min()),centroid=s['g'].tolist(),volume=s['volume'],trust=trust,seconds=time.time()-start);history.append(row);np.save(out/'latest_q.npy',q);np.save(out/'latest_H.npy',s['H']);(out/'history.json').write_text(json.dumps(history,indent=2)+'\n')
        if it%5==0:print('APEX_QUAD_CAPACITY',row,flush=True)
        if s['S']==s['U']==1:
            (out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');np.save(out/'NUMERICAL_NOMINATION_H.npy',s['H']);from audit_free_supports import audit;exact=audit(out/'NUMERICAL_NOMINATION_H.npy',out/'exact_nomination_g16',10**16);print('EXACT_NOMINATION_COUNTS',exact['counts'],exact['weak'],exact['E'],flush=True);return q
        if s['U']!=1 or s['uguards'][1:].min()<.8*eps:raise ValueError('actual U1 guard was lost')
        J=jac(q,s);W=metric(s,J);V,F=s['V'],s['F'];Cu=J[1:V]@W;Ct=J[V:V+F][s['polar_active']]@W;current=np.asarray(pieces(q,s['R'],s['T'],s['A'],s['up'],s['parent']))[V:V+F][s['polar_active']];A=np.r_[np.c_[-Cu*1000,np.zeros(len(Cu))],np.c_[-Ct,np.ones(len(Ct))]];b=np.r_[(s['uguards'][1:]-eps)*1000,current];bound=trust/np.sqrt(D);sol=linprog(np.r_[np.zeros(D),-1.],A_ub=A,b_ub=b,bounds=[(-bound,bound)]*D+[(-1,1)],method='highs-ipm',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-9,time_limit=10.))
        if not sol.success:trust*=.5;continue
        step=W@sol.x[:D];accepted=False
        for back in range(18):
            trial=repair(q+2**-back*step,max(trust*2**-back,1e-7),W,steps=10)
            if trial is None:continue
            try:trial=gauge(trial);t=model(trial)
            except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError):continue
            if t['U']!=1 or t['uguards'][1:].min()<.9*eps:continue
            if t['capacity']>s['capacity']+1e-12:
                if set(map(tuple,np.sort(t['R'][1:],axis=1)))!=set(map(tuple,np.sort(s['R'][1:],axis=1))):
                    event=dict(it=it,V=t['V'],E=t['E'],F=t['F'],S=t['S'],capacity=t['capacity']);events.append(event);(out/'events.json').write_text(json.dumps(events,indent=2)+'\n')
                q=trial;accepted=True;row['alpha']=2**-back;break
        if accepted and back==0:trust=min(.3,trust*1.3)
        if not accepted:trust*=.4
        if trust<1e-11:print('FINITE_APEX_CAPACITY_STALLED',row,flush=True);break
    np.save(out/'final_q.npy',q)
    return q

if __name__=='__main__':run(ROOT/sys.argv[1],ROOT/sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 1200,float(sys.argv[4]) if len(sys.argv)>4 else 1e-9)
