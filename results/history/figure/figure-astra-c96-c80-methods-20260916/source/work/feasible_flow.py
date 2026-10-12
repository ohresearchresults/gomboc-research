"""Trust-region LP continuation with true-mass U=1 checks on every accepted step.

The previous SLSQP trials left the feasible chamber. This method explicitly
rejects those finite steps, recomputes the complete hull, and records every
accepted checkpoint. It is a new bounded experiment, not a proof of reachability.
"""
import argparse
import json
import time
from pathlib import Path

import numpy as np
from scipy.optimize import linprog
from scipy.spatial import QhullError

from geometry import baseline,census,escape_table,mass,persistence,write_json


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',required=True)
    ap.add_argument('--steps',type=int,default=350)
    ap.add_argument('--extra',type=int,default=0)
    ap.add_argument('--input');ap.add_argument('--root',type=int,default=14)
    ap.add_argument('--margin',type=float,default=.0002)
    ap.add_argument('--lift',type=float,default=0.)
    ap.add_argument('--seed',type=int,default=96)
    ap.add_argument('--analytic',action='store_true')
    ap.add_argument('--buffer',type=float,default=0.)
    ap.add_argument('--chamber',action='store_true')
    ap.add_argument('--pyramid',action='store_true')
    ap.add_argument('--apex',type=int,default=15)
    ap.add_argument('--max-stable',type=int,default=0)
    ap.add_argument('--roundness',type=float,default=0.)
    ap.add_argument('--roundness-weight',type=float,default=10.)
    ap.add_argument('--roundness-min',type=float,default=0.)
    ap.add_argument('--resume-state')
    args=ap.parse_args();resume=None
    if args.resume_state:
        parent=Path(args.resume_state)
        old=json.loads((parent/'SEARCH.json').read_text())
        resume=json.loads((parent/'BEST.json').read_text())
        destination,steps,state=args.out,args.steps,args.resume_state
        args=argparse.Namespace(**old['config'])
        args.out=destination;args.steps=steps;args.resume_state=state
    out=Path(args.out);out.mkdir(exist_ok=False)
    p=baseline() if args.input is None else np.array(json.loads(Path(args.input).read_text())['points'],float)
    p-=mass(p)[1];p/=max(np.linalg.norm(p,axis=1))
    rng=np.random.default_rng(args.seed)
    if args.lift:
        # A literal shape change, saved as input, not Qhull joggling.
        p[:,1]+=args.lift*rng.integers(-1000,1001,len(p))/1000
    if args.extra:
        p=np.r_[p,np.array([rng.dirichlet(np.ones(len(p)))@p for _ in range(args.extra)])]
    if args.pyramid:
        assert args.lift==0 and args.extra==0
        assert np.ptp(p[[i for i in range(len(p)) if i!=args.apex],1])<1e-12
    if resume is not None:
        p=np.array(resume['points'],float)
    write_json(out/'INITIAL.json',dict(points=p.tolist(),census=census(p)))
    protect=np.array([i for i in range(len(p)) if i!=args.root])
    volume0=mass(p)[0];shape=p.shape;dof=p.size;trust=.03
    start_step=0
    if resume is not None:
        original=json.loads((parent/'INITIAL.json').read_text())
        volume0=mass(np.array(original['points'],float))[0]
        trust=resume['trust'];start_step=resume['step']+1
        write_json(out/'RESUMPTION.json',dict(parent=str(parent),completed_through=resume['step'],
                   parent_log_last_step=old['history'][-1]['step'],volume_reference=volume0,
                   inherited_trust=trust))
    history=[];evals=0;start=time.time()

    def evaluate(z,witness=None):
        nonlocal evals
        evals+=1
        r=census(z,True);x=z-np.array(r['centroid']);rr=np.einsum('ij,ij->i',x,x)
        table=escape_table(x)
        if witness is None:
            witness=table.argmax(axis=1)
        con=table[protect,witness[protect]]-args.margin
        con=np.r_[con,r['volume']/volume0-.5]
        if args.roundness_min:
            ratio=1/np.sqrt(max(rr)*max(np.einsum('ij,ij->i',r['q'],r['q'])))
            con=np.r_[con,ratio-args.roundness_min]
        score=persistence(r['q'])/max(rr)
        if args.roundness:
            ratio=1/np.sqrt(max(rr)*max(np.einsum('ij,ij->i',r['q'],r['q'])))
            score+=args.roundness_weight*max(0.,args.roundness-ratio)**2
        return score,con,r,witness

    for step in range(start_step,args.steps):
        score,con,r,w=evaluate(p)
        assert min(con)>-1e-7
        if args.analytic:
            from differential import derivatives
            _,_,grad,jac,_=derivatives(p,protect,w,volume0,args.margin,args.roundness,args.roundness_weight)
            if args.roundness_min:
                from differential import roundness_derivative
                _,dr=roundness_derivative(p,r)
                jac=np.r_[jac,dr[None,:]]
        else:
            derivative=np.empty((len(con)+1,dof))
            eps=1e-6
            for j in range(dof):
                z=p.copy().ravel();z[j]+=eps
                plus=evaluate(z.reshape(shape),w)
                z[j]-=2*eps
                minus=evaluate(z.reshape(shape),w)
                derivative[:,j]=(np.r_[plus[0],plus[1]]-np.r_[minus[0],minus[1]])/(2*eps)
            grad=derivative[0];jac=derivative[1:]
        x=p-np.array(r['centroid'])
        gauges=np.zeros((4,dof))
        for j in range(3):
            gauges[j,j::3]=1
        gauges[3]=x.ravel()
        if args.pyramid:
            gauges=gauges[[0,2,3]]
        movement_bounds=[(-trust,trust)]*dof
        if args.pyramid:
            movement_bounds=[(0.,0.) if i%3==1 and i//3!=args.apex else (-trust,trust) for i in range(dof)]
        budget=con-args.buffer*trust
        if args.max_stable:
            from differential import stable_escape_derivatives
            sg,sj=stable_escape_derivatives(p,r)
            jac=np.r_[jac,sj]
            budget=np.r_[budget,sg]
        if args.chamber:
            from differential import convexity_derivatives
            gaps,gapjac=convexity_derivatives(p,r)
            jac=np.r_[jac,gapjac]
            budget=np.r_[budget,.95*gaps]
        lin=linprog(grad,A_ub=-jac,b_ub=budget,A_eq=gauges,b_eq=np.zeros(len(gauges)),
                    bounds=movement_bounds,method='highs',
                    options={'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9,'threads':1})
        if not lin.success or lin.fun>=-1e-12:
            history.append(dict(step=step,score=score,stopped='No strict LP descent',message=lin.message))
            break
        # Near-optimal descent with minimum L1 motion, avoiding unused bang-bang freedom.
        aub=np.vstack([np.c_[-jac,np.zeros_like(jac)],np.r_[grad,np.zeros(dof)],
                       np.c_[np.eye(dof),-np.eye(dof)],np.c_[-np.eye(dof),-np.eye(dof)]])
        bub=np.r_[budget,.95*lin.fun,np.zeros(2*dof)]
        tie=linprog(np.r_[np.zeros(dof),np.ones(dof)],A_ub=aub,b_ub=bub,
                    A_eq=np.c_[gauges,np.zeros_like(gauges)],b_eq=np.zeros(len(gauges)),
                    bounds=movement_bounds+[(0.,trust)]*dof,method='highs',
                    options={'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9,'threads':1})
        if not tie.success:
            history.append(dict(step=step,score=score,stopped='L1 selection LP failed',message=tie.message))
            break
        delta=tie.x[:dof].reshape(shape);accepted=False;trials=[]
        for alpha in [1.,.5,.25,.125,.0625,.03125,.015625,.0078125]:
            proposal=p+alpha*delta
            try:
                newscore,newcon,newr,_=evaluate(proposal,w)
                trials.append(dict(alpha=alpha,score=newscore,minimum_constraint=float(min(newcon)),S=newr['S'],U=newr['U']))
                stable_ok=(not args.max_stable) or (newr['S']<=args.max_stable and newr['S_uncertain']==0)
                if min(newcon)>=0 and newscore<score-1e-9 and newr['U']==1 and newr['U_uncertain']==0 and stable_ok:
                    p=proposal;accepted=True;break
            except (QhullError,ValueError,AssertionError,np.linalg.LinAlgError):
                continue
        if accepted:
            trust=min(.08,trust*(1.15 if alpha>=.5 else .8))
            rr=census(p)
            rec=dict(step=step,score=newscore,trust=trust,alpha=alpha,
                     minimum_constraint=float(min(newcon)),census=rr,points=p.tolist(),nfev=evals)
            rec['inradius_to_circumradius']=float(1/np.sqrt(max(np.einsum('ij,ij->i',newr['x'],newr['x']))*max(np.einsum('ij,ij->i',newr['q'],newr['q']))))
            write_json(out/'BEST.json',rec)
            history.append({k:v for k,v in rec.items() if k!='points'})
            if step%10==0:
                print('FLOW_ACCEPT',step,newscore,rr['S'],rr['U'],rr['E_proposal'],trust,flush=True)
            if rr['S']==rr['U']==1 and rr['S_uncertain']==rr['U_uncertain']==0:
                write_json(out/'PROPOSAL110.json',rec)
                break
        else:
            trust*=.35
            history.append(dict(step=step,score=score,accepted=False,trust=trust,
                                linear_prediction=float(lin.fun),gradient_norm=float(np.linalg.norm(grad)),trials=trials))
            if trust<1e-6:
                break
        write_json(out/'SEARCH.json',dict(config=vars(args),history=history,nfev=evals,elapsed=time.time()-start))
    write_json(out/'SEARCH.json',dict(config=vars(args),history=history,nfev=evals,elapsed=time.time()-start))
    print('FEASIBLE_FLOW_FINISHED',len(history),evals,census(p)['S'],census(p)['U'],time.time()-start,flush=True)


if __name__=='__main__':
    main()
