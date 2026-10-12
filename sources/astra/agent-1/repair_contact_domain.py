"""Convex-realization feasibility for an explicitly unverified contact proposal.

Intermediate arrays may violate supporting inequalities and are NOT physical
body nominations. Only a complete contact/noncontact/orientation/mass evaluation
can admit an endpoint, followed by a separate exact audit for scientific claims.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,json,pathlib,time
import numpy as np,torch
from scipy.linalg import svd
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,eye,hstack,vstack
from contact_forest import ContactModel
torch.set_num_threads(1);torch.set_default_dtype(torch.float64)

def run(source,out,nU=2,nS=1,eps=1e-9,steps=80):
    c=ContactModel(source,nU,nS,'local');z=c.initial.copy();out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True);history=[];trust=.003;start=time.time();fi,vi=np.where(~c.inc);d=c.free
    def domain(z,jacobian=False):
        zz=torch.tensor(z);A=c.reconstruct(zz).detach().numpy();Y=A[:c.F];X=A[c.F:];gap=1-(Y[fi]*X[vi]).sum(1)
        if not np.isfinite(A).all():raise ValueError('nonfinite proposal')
        if not jacobian:return gap,A
        DA=torch.func.jacrev(c.reconstruct)(zz).detach().numpy();DY=DA[:c.F];DX=DA[c.F:];J=-np.einsum('ic,icp->ip',Y[fi],DX[vi])-np.einsum('ic,icp->ip',X[vi],DY[fi])
        scale=np.r_[np.full(c.F*3,np.sqrt(np.mean(Y**2))),np.full(len(X)*3,np.sqrt(np.mean(X**2)))];_,s,Vt=svd(DA.reshape(-1,d)/scale[:,None],full_matrices=False,check_finite=False);W=Vt.T/s
        return gap,A,J,W
    for it in range(steps):
        gap,A,J,W=domain(z,True);merit=float(np.maximum(eps-gap,0).sum());row=dict(it=it,scope='unverified contact arrays until admitted',minimum_gap=float(gap.min()),gap_defect=merit,trust=trust,seconds=time.time()-start);history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));np.savez(out/'latest.npz',z=z)
        if it%5==0:print('DOMAIN_REPAIR',json.dumps(row),flush=True)
        if gap.min()>.8*eps:
            e=c.evaluate(z,False);summary=dict(scope='Numerically admitted convex contact realization; exact audit required',V=len(e['X']),E=c.meta['E'],F=c.F,S=e['S'],U=e['U'],minimum=float(e['mechanical'].min()),minimum_gap=e['minimum_gap'],minimum_turn=e['minimum_turn'],bars=e['bars']);(out/'summary.json').write_text(json.dumps(summary,indent=2));np.savez(out/'ADMITTED.npz',z=z,X=e['X'],Q=e['Y']);print('ADMITTED_CONVEX_REALIZATION',summary,flush=True);return
        bound=trust/np.sqrt(d);B=J@W;rhs=gap-eps;keep=rhs<=bound*np.abs(B).sum(1)+1e-10;B=B[keep];rhs=rhs[keep];n=len(rhs);scale=np.maximum(bound*np.abs(B).sum(1),1e-12);I=eye(d);O=csr_matrix((d,n))
        mat=vstack([hstack([-csr_matrix(B/scale[:,None]),-eye(n),csr_matrix((n,d))]),hstack([I,O,-I]),hstack([-I,O,-I])],format='csr');b=np.r_[rhs/scale,np.zeros(2*d)]
        lp=linprog(np.r_[np.zeros(d),scale,np.full(d,1e-7)],A_ub=mat,b_ub=b,bounds=[(-bound,bound)]*d+[(0,None)]*(n+d),method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
        if not lp.success:
            trust*=.5
            if trust<1e-10:break
            continue
        dz=W@lp.x[:d];accepted=False
        for k in range(14):
            zz=z+dz*2**-k
            try:vv,_=domain(zz)
            except (ValueError,RuntimeError,np.linalg.LinAlgError):continue
            new=float(np.maximum(eps-vv,0).sum())
            if new<merit*(1-1e-6):z=zz;accepted=True;break
        if accepted and k==0:trust=min(.03,trust*1.2)
        if not accepted:trust*=.4
        if trust<1e-10:break
    print('NO_ADMITTED_BODY_FROM_FINITE_DOMAIN_REPAIR',flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--source',required=True);ap.add_argument('--out',required=True);ap.add_argument('--epsilon',type=float,default=1e-9);ap.add_argument('--steps',type=int,default=80);a=ap.parse_args();run(a.source,a.out,eps=a.epsilon,steps=a.steps)
