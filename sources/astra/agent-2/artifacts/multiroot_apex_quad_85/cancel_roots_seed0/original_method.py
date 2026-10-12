"""Sequential stable-root cancellation in an actual 85-support convex body.

At each stage, all currently nonstable polar vertices and every primal vertex
except the prescribed apex retain a strict positive radial dot witness. A
chosen extra stable facet is then driven toward a positive witness. All dot
products are evaluated at the integrated volume centroid of the same body.
The complete physical hull is rebuilt on every nonlinear trial. Counts, not
linear predictions or optimization residuals, decide numerical cancellation.
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
from apex_quad_supports import state,physical,ROOT
from apex_quad_capacity_flow import independent_pieces

@jax.jit
def pieces(q,R,T,A,up,sp):
    X,Z,Y,g,v=physical(q,R,T,A)
    def dots(B,p):return jnp.sum(B*(B[p]-B),1)/jnp.sum(B*B,1)
    return jnp.r_[dots(Z,up),dots(Y,sp),Z.ravel(),Y.ravel()]
jacobian=jax.jit(jax.jacfwd(pieces,argnums=0))

def model(q):
    s=state(q)
    for B,key in [(s['Z'],'u'),(s['Y'],'s')]:
        raw=np.einsum('ij,ikj->ik',B,B[None]-B[:,None])/np.sum(B*B,1)[:,None]
        np.fill_diagonal(raw,-np.inf);p=raw.argmax(1);s[key+'p']=p;s[key+'raw']=raw[np.arange(len(B)),p]
    return s

def jac(q,s):return np.asarray(jacobian(q,s['R'],s['T'],s['A'],s['up'],s['sp']))

def gauge(q):
    s=state(q);u=np.array([0.,0.,1.])-s['g'];radius=np.linalg.norm(u);ez=u/radius
    axis=np.eye(3)[np.argmin(abs(ez))];ex=axis-ez*(axis@ez);ex/=np.linalg.norm(ex);ey=np.cross(ez,ex)
    H=s['H']/(1-s['H']@s['g'])[:,None];H=H@np.column_stack([ex,ey,ez])*radius
    if abs(H[:4,2]-1).max()>1e-8:raise ValueError('gauge violates apex incidence')
    return np.r_[H[:4,:2].ravel(),H[4:].ravel()]

def run(src,out,stages=70,steps=160,seed=0):
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False);q=np.load(src);D=len(q);start=time.time();hist=[];rng=np.random.default_rng(seed)
    (out/'source.npy').write_bytes(src.read_bytes());(out/'source.json').write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(src.read_bytes()).hexdigest(),method=__doc__,seed=seed),indent=2)+'\n')
    epsu=1e-10;epss=1e-9
    def metric(s,J):
        V,F=s['V'],s['F'];G=J[V+F:];M=np.vstack([G[:3*V]/np.sqrt(np.mean(s['Z']**2)),G[3*V:]/np.sqrt(np.mean(s['Y']**2)),np.eye(D)*.03]);_,d,Vt=svd(M,full_matrices=False,check_finite=False);return Vt.T/d
    def guards(s,allowed):
        protected=np.flatnonzero(~np.isin(s['A'],list(allowed)));ix=np.r_[np.arange(1,s['V']),s['V']+protected]
        values=np.r_[s['uraw'][1:],s['sraw'][protected]];floors=np.r_[np.full(s['V']-1,epsu),np.full(len(protected),epss)]
        return ix,values,floors
    def repair(q,allowed,radius,W=None,nsteps=16):
        for k in range(nsteps):
            try:s=model(q)
            except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError):return None
            ix,g,e=guards(s,allowed)
            if np.min(g/e)>.999:return q
            J=jac(q,s)
            if W is None:W=metric(s,J)
            C=J[ix]@W;bound=radius/np.sqrt(D);I=eye(D)
            M=vstack([hstack([-csr_matrix(C*1000),csr_matrix((len(C),D))]),hstack([I,-I]),hstack([-I,-I])],format='csr')
            sol=linprog(np.r_[np.zeros(D),np.ones(D)],A_ub=M,b_ub=np.r_[(g-e)*1000,np.zeros(2*D)],bounds=[(-bound,bound)]*D+[(0,None)]*D,method='highs-ipm',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-9,time_limit=10.))
            if not sol.success:return None
            step=W@sol.x[:D];old=np.maximum(e-g,0).sum();accepted=False
            for back in range(14):
                trial=q+step*2**-back
                try:t=model(trial);_,tg,te=guards(t,allowed)
                except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError):continue
                if np.maximum(te-tg,0).sum()<old*(1-1e-7):q=trial;accepted=True;break
            if not accepted:return None
        return None
    first=model(q);d=rng.normal(size=D);d/=np.linalg.norm(d);J=jac(q,first);args=[first[k] for k in ['R','T','A','up','sp']]
    # Independent complex extension, replacing only the polar normalization.
    def independent(qq):
        R,T,A,up,sp=args;H=np.r_[np.c_[qq[:8].reshape(4,2),np.ones(4)],qq[8:].reshape(-1,3)];X=np.r_[[[0.,0.,1.]],np.linalg.solve(H[R[1:]],np.ones((len(R)-1,3,1))).squeeze(-1)]
        a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];six=np.sum(a*np.cross(b,c),1);g=np.sum(six[:,None]*(a+b+c),0)/(4*six.sum());Z=X-g;Y=H[A]/(1-H[A]@g)[:,None]
        def dot(B,p):return np.sum(B*(B[p]-B),1)/np.sum(B*B,1)
        return np.r_[dot(Z,up),dot(Y,sp),Z.ravel(),Y.ravel()]
    err=np.max(abs(np.imag(independent(q.astype(complex)+1e-25j*d))/1e-25-J@d))/max(1,np.max(abs(J@d)));verr=np.max(abs(independent(q)-np.asarray(pieces(q,*args))))
    (out/'derivative_check.json').write_text(json.dumps(dict(relative_error=float(err),value_error=float(verr)),indent=2)+'\n')
    if err>1e-7 or verr>1e-9:raise ValueError('independent physical derivative mismatch')
    if first['U']!=1:raise ValueError('source is not actual U1')
    tried=set()
    for stage in range(stages):
        s=model(q);stable=set(map(int,s['A'][s['sraw']<=0]));elder=int(s['A'][np.argmax(np.sum(s['Y']**2,1))])
        if len(stable)==1:
            dest=out/'NUMERICAL_NOMINATION';dest.mkdir(exist_ok=False);np.save(dest/'q.npy',q);np.save(dest/'H.npy',s['H']);from audit_free_supports import audit;audit(dest/'H.npy',dest/'exact_g16',10**16);return q
        order=[int(s['A'][i]) for i in np.argsort(-s['sraw']) if int(s['A'][i]) in stable and int(s['A'][i])!=elder and int(s['A'][i]) not in tried]
        if not order:print('FINITE_ALL_REMAINING_ROOTS_STALLED',sorted(tried),flush=True);break
        if seed and len(order)>1:
            target=int(rng.choice(order[:min(6,len(order))]))
        else:target=order[0]
        originalS=s['S'];allowed=stable.copy();trust=.04;accepted_any=False
        for it in range(steps):
            s=model(q);sid=np.flatnonzero(s['A']==target);_,gv,ge=guards(s,allowed)
            if np.min(gv/ge)<.8 or s['U']!=1:raise ValueError('a required strict witness was lost')
            score=float(s['sraw'][sid[0]]) if len(sid) else float('inf')
            row={k:s[k] for k in ['V','E','F','S','U','Pmax','Qmax','minimum_noncontact']};row.update(stage=stage,it=it,target=target,target_score=score,trust=trust,seconds=time.time()-start)
            hist.append(row);np.save(out/'latest_q.npy',q);np.save(out/'latest_H.npy',s['H']);(out/'history.json').write_text(json.dumps(hist,indent=2)+'\n')
            if it%10==0:print('ROOT_CANCELLATION',row,flush=True)
            if (not len(sid) or score>=epss) and s['S']<originalS:
                stageout=out/f'cancel{stage:02d}';stageout.mkdir(exist_ok=False);np.save(stageout/'q.npy',q);np.save(stageout/'H.npy',s['H']);(stageout/'summary.json').write_text(json.dumps(row,indent=2)+'\n');print('NUMERICAL_ROOT_REMOVED',row,flush=True);tried.clear();break
            J=jac(q,s);W=metric(s,J);ix,g,e=guards(s,allowed);C=J[ix]@W;targetj=s['V']+sid[0];grad=J[targetj]@W;bound=trust/np.sqrt(D)
            sol=linprog(-grad*1000,A_ub=-C*1000,b_ub=(g-e)*1000,bounds=[(-bound,bound)]*D,method='highs-ipm',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-9,time_limit=10.))
            if not sol.success:trust*=.5;continue
            step=W@sol.x;accepted=False
            for back in range(18):
                trial=repair(q+step*2**-back,allowed,max(trust*2**-back,1e-7),W)
                if trial is None:continue
                try:trial=gauge(trial);t=model(trial);_,tg,te=guards(t,allowed)
                except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError):continue
                if t['U']!=1 or np.min(tg/te)<.9:continue
                ti=np.flatnonzero(t['A']==target);newscore=float(t['sraw'][ti[0]]) if len(ti) else float('inf')
                if newscore>score+1e-13:q=trial;accepted=True;accepted_any=True;row['alpha']=2**-back;break
            if accepted and back==0:trust=min(.4,trust*1.4)
            if not accepted:trust*=.35
            if trust<1e-11:break
        else:pass
        end=model(q);isid=np.flatnonzero(end['A']==target)
        if len(isid) and end['sraw'][isid[0]]<epss:tried.add(target)
    np.save(out/'final_q.npy',q);np.save(out/'final_H.npy',model(q)['H']);(out/'FINITE_BRANCH_END.json').write_text(json.dumps(dict(stages=stages,steps=steps,goal_complete=False),indent=2)+'\n')
    return q

if __name__=='__main__':run(ROOT/sys.argv[1],ROOT/sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 70,int(sys.argv[4]) if len(sys.argv)>4 else 160,int(sys.argv[5]) if len(sys.argv)>5 else 0)
