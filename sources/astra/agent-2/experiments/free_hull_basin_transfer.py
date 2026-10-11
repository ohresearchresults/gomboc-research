"""Finite actual-own cross-basin search allowing genuine hull adjacency changes.
One old elder-reaching component retains within-component positive witnesses.
A new positive cross-chord plus increased reachability nominates a transfer,
never the target body. Every physical hull/mass and guard is re-evaluated.
"""
import sys,json,time,hashlib
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.spatial import QhullError
from scipy.sparse import csr_matrix,eye,hstack,vstack
from scipy.linalg import svd
import jax,jax.numpy as jnp
from free_hull_metric121 import state as rawstate,physical,jacobian,embedding_jac
from basin_transfer121 import reachable
from geometry import angular_scores
from support_persistence import ROOT

@jax.jit
def crossgrad(X,T,child,parent):
    def value(X):
        Z,Q,g,v=physical(X,T);a,b=Z[child],Z[parent];d=b-a
        return -jnp.sum(a*d)/jnp.sqrt(jnp.sum(a*a)*jnp.sum(d*d))
    return jax.value_and_grad(value)(X)

def run(src,out,steps=1500,eps=5e-8,elder=None):
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False);raw=src.read_bytes();X=np.load(src);assert len(X)<=84
    s=rawstate(X);X=s['Z']/np.max(np.linalg.norm(s['Z'],axis=1));s=rawstate(X);allowed=s['allowed'];ur=int(np.argmax(np.sum(s['Z']**2,1))) if elder is None else int(elder);seen,sc=reachable(s['Z'],ur,.5*eps)
    _,child,parent=max((sc[i,j],int(i),int(j)) for i in np.flatnonzero(~seen) for j in np.flatnonzero(seen));oldcount=int(seen.sum());n=len(X);D=3*n;trust=.02;hist=[];events=[];start=time.time()
    np.save(out/'source_X.npy',X);(out/'nomination.json').write_text(json.dumps(dict(source=str(src),source_sha256=hashlib.sha256(raw).hexdigest(),child=child,parent=parent,elder=ur,allowed=allowed,initial_reachable=np.flatnonzero(seen).tolist(),initial_cross=float(sc[child,parent]),eps=eps,no_goal_claim=True),indent=2)+'\n')
    def state(A):
        s=rawstate(A,allowed)
        if s['E']<17:raise ValueError('outside owner complexity search range')
        u=angular_scores(s['Z']);u[np.ix_(seen,~seen)]=-np.inf;s['up']=u.argmax(1);s['guards'][:n]=u[np.arange(n),s['up']]
        # A retired submitted point can remain a witness used by other points.
        # Preserve its path too; otherwise the old component need not persist.
        s['active'][np.flatnonzero(seen)]=True;s['active'][ur]=False
        s['minimum']=float(s['guards'][s['active']].min());value,grad=crossgrad(A,s['T'],child,parent);s['cross_loss']=float(value);s['cross_grad']=np.asarray(grad).ravel();return s
    def jac(A,s):return np.asarray(jacobian(A,s['T'],s['up'],s['sp'],s['p'],s['w'])).reshape(-1,D)
    def metric(A,s):
        J=np.asarray(embedding_jac(A,s['T'])).reshape(-1,D);M=np.vstack([J[:3*n]/np.sqrt(np.mean(s['Z']**2)),J[3*n:]/np.sqrt(np.mean(s['Q']**2)),np.eye(D)*.05]);_,d,Vt=svd(M,full_matrices=False,check_finite=False);return Vt.T/d
    def retract(A,radius,W):
        for _ in range(10):
            try:s=state(A)
            except (ValueError,QhullError,np.linalg.LinAlgError,AssertionError):return None
            if s['minimum']>.999*eps:return A
            C=jac(A,s)[:-1][s['active']]@W;rhs=s['guards'][s['active']]-eps;bound=radius/np.sqrt(D);keep=rhs<=bound*np.sum(abs(C),1)+1e-10;C=C[keep];rhs=rhs[keep];I=eye(D)
            mat=vstack([hstack([-csr_matrix(C*1000),csr_matrix((len(C),D))]),hstack([I,-I]),hstack([-I,-I])],format='csr')
            opt=linprog(np.r_[np.zeros(D),np.ones(D)],A_ub=mat,b_ub=np.r_[rhs*1000,np.zeros(2*D)],bounds=[(-bound,bound)]*D+[(0,None)]*D,method='highs-ipm',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-9,time_limit=10.))
            if not opt.success:return None
            A=A+(W@opt.x[:D]).reshape(n,3)
        return None
    initial=state(X)
    if initial['minimum']<.999*eps:
        prepared=retract(X,.05,metric(X,initial))
        if prepared is None:raise ValueError('old component strict preparation failed')
        X=prepared
    for it in range(steps):
        s=state(X);live,_=reachable(s['Z'],ur,.5*eps);row=dict(it=it,S=s['S'],U=s['U'],cross=-s['cross_loss'],reachable=int(live.sum()),minimum=s['minimum'],V=s['V'],E=s['E'],F=s['F'],trust=trust,seconds=time.time()-start);hist.append(row);np.save(out/'latest.npy',X);(out/'history.json').write_text(json.dumps(hist,indent=2)+'\n')
        if it%5==0:print('FREE_HULL_BASIN',row,flush=True)
        if s['S']==s['U']==1:
            np.save(out/'NUMERICAL_GOAL.npy',X);(out/'NUMERICAL_GOAL_REQUIRES_EXACT.json').write_text(json.dumps(row,indent=2)+'\n');print('NUMERICAL_GOAL_REQUIRES_EXACT',row,flush=True);break
        if row['cross']>eps and int(live.sum())>oldcount:
            np.save(out/'FINITE_TRANSFER.npy',X);(out/'FINITE_TRANSFER_NOT_GOAL.json').write_text(json.dumps(row,indent=2)+'\n');print('FINITE_TRANSFER_REQUIRES_EXACT',row,flush=True);break
        if s['minimum']<.8*eps or s['S']>1 or s['U']>2:raise ValueError('strict actual-own guards failed')
        J=jac(X,s);W=metric(X,s);C=J[:-1][s['active']]@W;rhs=s['guards'][s['active']]-eps;bound=trust/np.sqrt(D);keep=rhs<=bound*np.sum(abs(C),1)+1e-10
        opt=linprog(s['cross_grad']@W,A_ub=-C[keep]*1000,b_ub=rhs[keep]*1000,bounds=[(-bound,bound)]*D,method='highs-ipm',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-9,time_limit=10.));accepted=False
        if opt.success:
            step=(W@opt.x).reshape(n,3)
            for back in range(18):
                A=retract(X+2**-back*step,max(trust*2**-back,1e-7),W)
                if A is None:continue
                try:
                    t=state(A);A=t['Z']/np.max(np.linalg.norm(t['Z'],axis=1));t=state(A)
                except (ValueError,QhullError,np.linalg.LinAlgError,AssertionError):continue
                if t['minimum']<.9*eps or t['S']>1 or t['U']>2:continue
                if np.linalg.norm(t['Z'][child]-t['Z'][parent])<1e-3*np.sqrt(np.mean(t['Z']**2)):continue
                if t['cross_loss']<s['cross_loss']-1e-12:
                    removed=s['facets']-t['facets'];added=t['facets']-s['facets']
                    if removed or added:
                        name=f'event_{len(events):04d}_it{it}';np.save(out/(name+'.npy'),A);events.append(dict(it=it,coordinates=name+'.npy',removed=[list(x) for x in sorted(removed)],added=[list(x) for x in sorted(added)],cross=-t['cross_loss']));(out/'events.json').write_text(json.dumps(events,indent=2)+'\n')
                    X=A;accepted=True;row['alpha']=2**-back;break
        if accepted and back==0:trust=min(.2,trust*1.4)
        if not accepted:trust*=.4
        if trust<1e-11:print('FINITE_BASIN_FLOW_STALLED',row,flush=True);break
    np.save(out/'final.npy',X)
    return X
if __name__=='__main__':run(ROOT/sys.argv[1],ROOT/sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 1500)
