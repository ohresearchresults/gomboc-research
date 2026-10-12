"""Maximize uniform-volume fraction using coupled physical shape/centroid steps.
lambda<1 is never an own-centroid claim; a final exact uniform-body audit is required.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,torch,json,pathlib,time,argparse
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,eye,hstack,vstack
from mass_homotopy import guards,repair,check_own
torch.set_num_threads(1);torch.set_default_dtype(torch.float64)

def run(input,out,stages=120,eps=2e-6):
    dat=np.load(input);X=dat['X'];w=dat['w'];lam=float(dat['lam']);out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True);history=[];trust=.02;t0=time.time()
    for stage in range(stages):
        m,c,v,pa,sg,st=guards(X,w,lam);tt=torch.tensor(m['T']);tp=torch.tensor(m['polar_triangles']);ti=torch.tensor(m['active']);tw=torch.tensor(w);parents=list(map(torch.tensor,pa));signs=list(map(torch.tensor,sg));d=X.size
        def calc(z):
            x=z[:d].reshape(X.shape);t=z[-1];a=x[tt];vol=(a[:,0]*torch.linalg.cross(a[:,1],a[:,2])).sum(1)/6;g=(vol[:,None]*a.sum(1)).sum(0)/(4*vol.sum());c=t*g+(1-t)*(tw@x);P=x[ti]-c;Q=torch.linalg.solve(x[tp]-c,torch.ones((len(tp),3,1)))[:,:,0];vals=[]
            for A,p,s in zip([P,Q],parents,signs):
                delta=A[p]-A;vals.append(s*(A*delta).sum(1)/(torch.linalg.vector_norm(A,dim=1)*torch.linalg.vector_norm(delta,dim=1)).clamp(min=1e-18))
            return torch.cat(vals)
        J=torch.func.jacrev(calc)(torch.tensor(np.r_[X.ravel(),lam])).detach().numpy();I=eye(d+1);A=vstack([hstack([-csr_matrix(J),csr_matrix((len(v),d+1))]),hstack([I,-I]),hstack([-I,-I])],format='csr');b=np.r_[v-eps,np.zeros(2*(d+1))];cost=np.r_[np.zeros(d),-1,np.full(d,1e-5),0];scale=np.sqrt(np.mean((X-c)**2));bound=trust*scale
        lp=linprog(cost,A_ub=A,b_ub=b,bounds=[(-bound,bound)]*d+[(0,min(1-lam,.1))]+[(0,None)]*(d+1),method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
        if not lp.success or lp.x[d]<1e-8:trust*=.5;print('NO_PREDICTOR',stage,lam,trust,lp.message,flush=True)
        else:
            dx=lp.x[:d].reshape(X.shape);dl=lp.x[d];accepted=False;folder=out/f'stage{stage:03d}';folder.mkdir(exist_ok=True)
            for level in range(7):
                target=lam+dl*2**-level;trial=X+dx*2**-level;dest=folder/f'repair{level}';Y,ok,stats=repair(trial,w,target,dest,steps=70,eps=eps)
                if ok:
                    X=Y;lam=target;accepted=True;row=dict(stage=stage,backtrack=level,lambda_step=dl*2**-level,trust=trust,seconds=time.time()-t0,source=str(dest/'strict_reference110.npz'),**stats);history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));np.savez(out/'latest-strict.npz',X=X,w=w,lam=lam);print('MASS_PREDICTOR_PROGRESS',json.dumps(row),flush=True);break
            if accepted and level==0:trust=min(.1,trust*1.25)
            if not accepted:trust*=.4
            if accepted and check_own(X,w,out):return
        if lam>=1-1e-14:
            mm,cc,vv,_,_,ss=guards(X,w,1.)
            if ss['S']==ss['U']==1 and min(vv)>1e-6:
                np.savez(out/'NOMINATION_OWN110.npz',X=X,w=w,lam=1.);print('POTENTIAL_OWN110_REQUIRES_EXACT',flush=True);return
        if trust<1e-8:print('MASS_PREDICTOR_LOCAL_STALL',lam,flush=True);break

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--input',required=True);ap.add_argument('--out',required=True);ap.add_argument('--stages',type=int,default=120);ap.add_argument('--epsilon',type=float,default=2e-6);a=ap.parse_args();run(a.input,a.out,a.stages,a.epsilon)
