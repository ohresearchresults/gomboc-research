"""Direct own-centroid110 search with scaled guard rows and explicit small step regularizer.
Minimise all nonroot local-escape deficits. Unlike the two-root continuation,
there is no exempt surplus equilibrium; intermediate bodies may have many roots.
Every trial is a convex hull of literal points and has freshly integrated mass.
Only an exact full audit can accept a numerical one-root endpoint.
"""
import sys,json,time,hashlib
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.spatial import QhullError
from scipy.linalg import svd
from scipy.sparse import csr_matrix,eye,hstack,vstack
from free_hull_metric121 import state as rawstate,jacobian,embedding_jac
from support_persistence import ROOT

def run(src,out,steps=600,eps=1e-7):
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False);raw=src.read_bytes();X=np.load(src);assert len(X)<=84
    (out/'source.npy').write_bytes(raw);(out/'source.json').write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(raw).hexdigest(),eps=eps,lp_guard_scale=1000,step_regularization=eps*1e-5),indent=2)+'\n');n=len(X);D=3*n;trust=.02;hist=[];start=time.time()
    def state(A):
        s=rawstate(A);ur=int(np.argmax(np.sum(s['Z']**2,1)));sr=int(np.argmax(np.sum(s['Q']**2,1)));active=np.ones(len(s['guards']),bool);active[:n]=False;active[np.unique(s['T'])]=True;active[ur]=False;active[n+sr]=False;s['active110']=active;s['merit']=float(np.maximum(eps-s['guards'][active],0).sum());s['minimum110']=float(s['guards'][active].min());return s
    for it in range(steps):
        s=state(X);row=dict(it=it,S=s['S'],U=s['U'],V=s['V'],E=s['E'],F=s['F'],merit=s['merit'],minimum=s['minimum110'],trust=trust,seconds=time.time()-start);hist.append(row);np.save(out/'latest.npy',X);(out/'history.json').write_text(json.dumps(hist,indent=2)+'\n')
        if it%5==0:print('ONE_ROOT_PHYSICAL',row,flush=True)
        if s['S']==s['U']==1 and s['minimum110']>0:
            np.save(out/'NUMERICAL_GOAL.npy',X);(out/'NUMERICAL_GOAL_REQUIRES_EXACT.json').write_text(json.dumps(row,indent=2)+'\n');print('NUMERICAL_GOAL_REQUIRES_EXACT',row,flush=True);break
        J=np.asarray(jacobian(X,s['T'],s['up'],s['sp'],s['p'],s['w'])).reshape(-1,D);K=np.asarray(embedding_jac(X,s['T'])).reshape(-1,D);metric=np.vstack([K[:D]/np.sqrt(np.mean(s['Z']**2)),K[D:]/np.sqrt(np.mean(s['Q']**2)),np.eye(D)*.05]);_,d,Vt=svd(metric,full_matrices=False,check_finite=False);W=Vt.T/d;C=J[:-1][s['active110']]@W;g=s['guards'][s['active110']];m=len(g);bound=trust/np.sqrt(D);I=eye(D);O=csr_matrix((D,m))
        A=vstack([hstack([-csr_matrix(C*1000),-eye(m)*1000,csr_matrix((m,D))]),hstack([I,O,-I]),hstack([-I,O,-I])],format='csr');b=np.r_[(g-eps)*1000,np.zeros(2*D)]
        opt=linprog(np.r_[np.zeros(D),np.ones(m),np.full(D,eps*1e-5)],A_ub=A,b_ub=b,bounds=[(-bound,bound)]*D+[(0,None)]*(m+D),method='highs-ipm',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-9,time_limit=10.));accepted=False
        if opt.success:
            step=(W@opt.x[:D]).reshape(n,3)
            for back in range(20):
                A=X+2**-back*step
                try:
                    t=state(A);A=t['Z']/np.max(np.linalg.norm(t['Z'],axis=1));t=state(A)
                    if t['E']<17:continue
                except (ValueError,QhullError,np.linalg.LinAlgError,AssertionError):continue
                if t['merit']<s['merit']*(1-1e-7):X=A;accepted=True;row['alpha']=2**-back;break
        if accepted and back==0:trust=min(.4,trust*1.4)
        if not accepted:trust*=.4
        if trust<1e-11:print('ONE_ROOT_FINITE_STALL',row,flush=True);break
    np.save(out/'final.npy',X);return X
if __name__=='__main__':run(ROOT/sys.argv[1],ROOT/sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 600,float(sys.argv[4]) if len(sys.argv)>4 else 1e-7)
