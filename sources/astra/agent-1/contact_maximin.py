"""Strict physical continuation maximizing the least equilibrium escape margin.

Every retained body remains in its specified actual-centroid chamber. This
optimizes a geometric margin; it neither claims optimality nor removes edges.
Exact claims require independent rational reconstruction and auditing.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,json,pathlib,time
import numpy as np
from scipy.optimize import linprog,minimize,LinearConstraint,Bounds
from contact_forest import ContactModel
from contact_retraction import retract
from contact_persistence_flow import normalized_volume

def run(source,input,out,steps=250):
    c=ContactModel(source,1,1,'local');z=np.load(input)['z'];out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False)
    e=c.evaluate(z);assert e['S']==e['U']==1 and e['mechanical'].min()>0
    volume0=normalized_volume(e)[0];history=[];start=time.time();trust=.01
    (out/'definition.json').write_text(json.dumps(dict(source=str(pathlib.Path(source).resolve()),input=str(pathlib.Path(input).resolve()),scope='Floating strict own110 maximin continuation; exact audit required',E=c.meta['E'],volume_floor=.1*volume0),indent=2))
    for it in range(steps):
        e=c.evaluate(z);v=e['mechanical'];m=float(v.min());W=c.metric(e);d=c.free;bound=trust/np.sqrt(d);B=e['J']@W;G=e['gapJ']@W;nv,DV=normalized_volume(e)
        # t is the absolute angular margin, not an auxiliary loss tolerance.
        A=np.vstack([np.c_[-B,np.ones(len(v))],np.c_[-G,np.zeros(len(G))],np.r_[-DV@W,0][None]])
        rhs=np.r_[v,.8*e['gapv'],nv-.1*volume0]
        possible=bound*np.abs(A[:,:d]).sum(1)
        scale=np.maximum(possible+np.abs(A[:,-1])*max(1e-5,m),1e-12)
        A/=scale[:,None];rhs/=scale
        lp=linprog(np.r_[np.zeros(d),-1.],A_ub=A,b_ub=rhs,bounds=[(-bound,bound)]*d+[(m,None)],method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
        row=dict(it=it,margin=m,S=e['S'],U=e['U'],minimum_gap=e['minimum_gap'],minimum_turn=e['minimum_turn'],trust=trust,seconds=time.time()-start)
        history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));np.savez(out/'latest-strict.npz',z=z,X=e['X'],Q=e['Y'])
        if it%5==0:print('STRICT_MAXIMIN',json.dumps(row),flush=True)
        if not lp.success or lp.x[-1]-m<max(1e-13,m*1e-6):
            trust*=.5
            if trust<1e-10:break
            continue
        gain=lp.x[-1]-m;target=m+.5*gain
        # Small physical displacement at a fixed fraction of the predicted
        # improvement reduces second-order contact and mass-integration drift.
        rhsq=rhs-A[:,-1]*target
        qp=minimize(lambda x:(.5*x@x,x),lp.x[:d]*.5,jac=True,method='SLSQP',bounds=Bounds(-bound,bound),constraints=[LinearConstraint(A[:,:d],-np.inf,rhsq)],options={'ftol':1e-15,'maxiter':100})
        if np.max(A[:,:d]@qp.x-rhsq)>1e-8:
            row['qp_failure']=str(qp.message);trust*=.5
            if trust<1e-10:break
            continue
        dz=W@qp.x;accepted=False
        for level in range(22):
            try:zz,ee,receipt=retract(c,e,dz,2**-level)
            except (ValueError,RuntimeError,np.linalg.LinAlgError):continue
            actual=float(ee['mechanical'].min())
            if ee['S']==ee['U']==1 and actual>m+max(1e-14,.02*gain*2**-level):
                z=zz;accepted=True;row.update(predicted=target,actual=actual,level=level,receipt=receipt);break
        if accepted and level==0:trust=min(.15,trust*1.3)
        elif accepted and level>5:trust*=.7
        elif not accepted:trust*=.4
        if trust<1e-10:break
    np.savez(out/'latest-strict.npz',z=z,X=c.evaluate(z,False)['X'],Q=c.evaluate(z,False)['Y'])
    (out/'history.json').write_text(json.dumps(history,indent=2))

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--source',required=True);ap.add_argument('--input',required=True);ap.add_argument('--out',required=True);ap.add_argument('--steps',type=int,default=250);a=ap.parse_args();run(a.source,a.input,a.out,a.steps)
