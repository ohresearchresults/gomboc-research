"""Own-mass C2 correction with necessary global radial-root inequalities.

The axial apex and diamond base supply the two allowed roots. Every other
genuine vertex/facet must have a positive escape. Re-hull after every trial;
transverse centroid zero is guaranteed by the literal physical symmetry.
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
from support_persistence import ROOT
from geometry import angular_scores
from c2_twisted_ladder import coordinates

def run(src,out,side='point',iters=500,eps=1e-7):
    if side=='point':from c2_twisted_ladder import state as body,physical
    elif side=='support':from c2_dual_morse import state as body,physical
    else:raise ValueError('explicit point or support family required')
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False);raw=src.read_bytes();q=np.load(src);(out/'source.npy').write_bytes(raw);(out/'source.json').write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(raw).hexdigest(),side=side,eps=eps),indent=2)+'\n')
    D=len(q);trust=.02;history=[];start=time.time()
    def pieces(q,T,R,A,up,sp):
        X,Z,Y,g,v,rr=physical(q,T,R) if side=='point' else physical(q,R,T,A)
        def angles(B,p):
            delta=B[p]-B;return jnp.sum(B*delta,1)/jnp.sqrt(jnp.maximum(jnp.sum(B*B,1)*jnp.sum(delta*delta,1),1e-40))
        return jnp.r_[angles(Z,up),angles(Y,sp),1-jnp.sum(Z*Z,1)/jnp.sum(Z[0]*Z[0]),1-jnp.sum(Y*Y,1)/jnp.sum(Y[0]*Y[0]),Z.ravel(),Y.ravel()]
    derivative=jax.jit(jax.jacfwd(pieces,argnums=0))
    def state(q):
        s=body(q);N=len(s['Z']);F=len(s['Y']);active_vertices=s['vertices'] if side=='point' else np.arange(N);valid=np.zeros(N,bool);valid[active_vertices]=True
        us=angular_scores(s['Z']);us[:,~valid]=-np.inf;ss=angular_scores(s['Y']);up=us.argmax(1);sp=ss.argmax(1);guards=np.r_[us[np.arange(N),up],ss[np.arange(F),sp],1-np.sum(s['Z']**2,1)/np.sum(s['Z'][0]**2),1-np.sum(s['Y']**2,1)/np.sum(s['Y'][0]**2)];base_active=np.r_[valid,np.ones(F,bool)];base_active[0]=False;base_active[N]=False;active=np.r_[base_active,base_active];merit=float(np.maximum(eps-guards[active],0).sum());s.update(up=up,sp=sp,guards=guards,exclude=active,merit=merit);return s
    qlo=np.r_[[-4.]*3,np.tile([-8.,-3.,-3.],(D-3)//3)];qhi=np.r_[[1.]*3,np.tile([8.,3.,3.],(D-3)//3)]
    for it in range(iters):
        s=state(q);row={k:s[k] for k in ['V','E','F','S','U','Pmax','Qmax','merit']};row.update(it=it,minimum=float(s['guards'][s['exclude']].min()),trust=trust,seconds=time.time()-start);history.append(row);np.save(out/'latest_q.npy',q);np.save(out/('latest_points.npy' if side=='point' else 'latest_supports.npy'),np.asarray(coordinates(q)));(out/'history.json').write_text(json.dumps(history,indent=2)+'\n')
        if it%5==0:print('C2_GLOBAL_OWN110',row,flush=True)
        if s['S']==s['U']==1 and row['minimum']>0:
            np.save(out/'NUMERICAL_NOMINATION_q.npy',q);(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');print('C2_NUMERICAL_REQUIRES_EXACT',row,flush=True);break
        N=len(s['Z']);F=len(s['Y']);A=s['active'] if side=='support' else np.array([],int);J=np.asarray(derivative(q,s['T'],s['R'],A,s['up'],s['sp']));embedding=J[2*(N+F):];metric=np.vstack([embedding[:3*N]/np.sqrt(np.mean(s['Z']**2)),embedding[3*N:]/np.sqrt(np.mean(s['Y']**2)),np.eye(D)*.05]);_,dd,Vt=svd(metric,full_matrices=False,check_finite=False);W=Vt.T/dd;C=J[:2*(N+F)][s['exclude']]@W;rhs=s['guards'][s['exclude']]-eps;ng=len(C);I=eye(D);O=csr_matrix((D,ng));M=vstack([hstack([-csr_matrix(C*1000),-eye(ng)*1000,csr_matrix((ng,D))]),hstack([I,O,-I]),hstack([-I,O,-I]),hstack([csr_matrix(W),csr_matrix((D,ng+D))]),hstack([-csr_matrix(W),csr_matrix((D,ng+D))])],format='csr');b=np.r_[rhs*1000,np.zeros(2*D),qhi-q,q-qlo];bound=trust/np.sqrt(D)
        sol=linprog(np.r_[np.zeros(D),np.ones(ng),np.full(D,1e-6)],A_ub=M,b_ub=b,bounds=[(-bound,bound)]*D+[(0,None)]*(ng+D),method='highs-ipm',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-9,time_limit=10.))
        if not sol.success:
            trust*=.5
            if trust<1e-10:break
            continue
        step=W@sol.x[:D];accepted=False
        for back in range(18):
            trial=q+2**-back*step
            if (trial<qlo-1e-12).any() or (trial>qhi+1e-12).any():continue
            try:t=state(trial)
            except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError):continue
            if t['merit']<s['merit']*(1-1e-6):q=trial;accepted=True;row['alpha']=2**-back;break
        if accepted and back==0:trust=min(.3,trust*1.4)
        if not accepted:trust*=.4
        if trust<1e-10:print('FINITE_C2_CORRECTION_STALLED',row,flush=True);break
    np.save(out/'final_q.npy',q)
    return q

if __name__=='__main__':run(ROOT/sys.argv[1],ROOT/sys.argv[2],sys.argv[3] if len(sys.argv)>3 else 'point',int(sys.argv[4]) if len(sys.argv)>4 else 500)
