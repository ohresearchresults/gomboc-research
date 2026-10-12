"""Minimum-norm physical homotopy of an edge of a strict own110 body.

Convex quadratic subproblems impose all active linearized geometric and
equilibrium constraints as hard inequalities. Every admitted nonlinear body
has its own integrated mass centre, exact contacts, and numerical strict110.
Exact checkpoints retain the genuine unchanged edge count until contraction.
"""
import argparse
import json
import time
from pathlib import Path

import numpy as np
from scipy.optimize import minimize

from contact_numpy import Chart
from contact_physical_110 import PhysicalGuards, freeze
from contact_quota_polish import metric
from strict110_edge_homotopy import edge


def evaluate(c, G, q, pair, kind, target, targets):
    g=c.physical(q,require_valid=False)
    v,J,t,JT,cl=G.evaluate(g)
    vv=np.r_[g['noncontact'],t,v]
    JJ=np.vstack((g['Dgap'][~c.incidence],JT,J))
    e,Je=edge(g,pair,kind);length=float(np.linalg.norm(e))
    derivative=e@Je/length
    residual=length-target
    merit=float(np.maximum(targets-vv,0).sum()+abs(residual))
    return g,vv,JJ,cl,length,derivative,residual,merit


def retract(c,G,q,pair,kind,target,targets,out):
    out=Path(out);out.mkdir(parents=True,exist_ok=False)
    hist=[]
    for it in range(24):
        g,v,J,cl,length,Je,res,merit=evaluate(c,G,q,pair,kind,target,targets)
        row=dict(it=it,valid=bool(g['valid']),edge_error=abs(res),merit=merit,minimum_slack=float(min(v-targets)),**cl)
        hist.append(row);np.save(out/'latest_q.npy',q);(out/'trace.json').write_text(json.dumps(hist,indent=2))
        if g['valid'] and cl['S']==cl['U']==1 and min(v-targets)>-min(targets)*.05 and abs(res)<1e-10:
            return q,True,hist
        W=metric(c,g);bound=.05/np.sqrt(c.d)
        B=(J@W)*bound;rhs=targets-v
        keep=rhs>=-np.sum(abs(B),axis=1)-1e-12
        B,rhs=B[keep],rhs[keep]
        scale=np.linalg.norm(B,axis=1)
        good=scale>1e-16
        if np.any(rhs[~good]>0):
            row['error']='positive constraint deficit has a numerically zero derivative'
            return q,False,hist
        B,rhs=B[good]/scale[good,None],rhs[good]/scale[good]
        E=(Je@W)*bound;sc=np.linalg.norm(E)
        if sc<=1e-16:
            row['error']='zero edge-length derivative'
            return q,False,hist
        E,eb=E/sc,-res/sc
        cons=[dict(type='ineq',fun=lambda z:B@z-rhs,jac=lambda z:B),
              dict(type='eq',fun=lambda z:np.array([E@z-eb]),jac=lambda z:E[None,:])]
        t0=time.time()
        r=minimize(lambda z:.5*float(z@z),np.zeros(c.d),jac=lambda z:z,method='SLSQP',
                   bounds=[(-1.,1.)]*c.d,constraints=cons,
                   options=dict(ftol=1e-12,maxiter=180,disp=False))
        row.update(qp_seconds=time.time()-t0,qp_success=bool(r.success),qp_iterations=int(r.nit),qp_message=r.message)
        linear_violation=max(float(max(rhs-B@r.x)),abs(float(E@r.x-eb)))
        row['linear_violation']=linear_violation
        if not r.success or linear_violation>2e-9:
            return q,False,hist
        dq=W@(bound*r.x);accepted=False
        for k in range(12):
            qq=q+2.**-k*dq
            try:
                *_,mm=evaluate(c,G,qq,pair,kind,target,targets)
            except (ValueError,np.linalg.LinAlgError):
                continue
            if np.isfinite(mm) and mm<merit-max(1e-14,merit*1e-8):
                q,accepted=qq,True;row['alpha']=2.**-k;break
        if not accepted:
            row['error']='no nonlinear merit decrease in finite line search'
            return q,False,hist
    return q,False,hist


def run(source,out,pair,kind,steps):
    c=Chart(source);G=PhysicalGuards(c,True);out=Path(out);out.mkdir(parents=True,exist_ok=False)
    q=c.q0.copy();g=c.physical(q);v,J,t,JT,cl=G.evaluate(g)
    assert cl['S']==cl['U']==1 and min(v)>0
    targets=np.r_[np.full(len(g['noncontact']),min(1e-11,min(g['noncontact'])*.1)),
                  np.full(len(t),min(1e-12,min(t)*.1)),
                  np.minimum(1e-8,np.full(len(v),min(v)*.1))]
    initial=float(np.linalg.norm(edge(g,pair,kind)[0]));fraction=.03;history=[];start=time.time();checkpoint=initial
    (out/'source_construction.json').write_bytes(Path(source).read_bytes())
    (out/'method.json').write_text(json.dumps(dict(source=str(Path(source).resolve()),pair=pair,kind=kind,initial_length=initial,minimum_equilibrium_target=float(min(targets[-len(v):])),method='minimum-norm convex QP with hard first-order constraints and complete nonlinear physical readmission'),indent=2))
    for it in range(steps):
        old=float(np.linalg.norm(edge(c.physical(q),pair,kind)[0]));target=old*(1-fraction)
        qq,good,detail=retract(c,G,q.copy(),pair,kind,target,targets,out/f'attempt{it:03d}')
        row=dict(it=it,fraction=fraction,accepted=good,correction_steps=len(detail),seconds=time.time()-start)
        if good:
            q=qq;fraction=min(.25,fraction*1.5)
        else:
            fraction*=.5
        gg=c.physical(q);vv,_,_,_,cc=G.evaluate(gg)
        assert cc['S']==cc['U']==1 and min(vv)>0
        length=float(np.linalg.norm(edge(gg,pair,kind)[0]));row.update(length_ratio=length/initial,minimum=float(min(vv)),gap=float(min(gg['noncontact'])))
        history.append(row);np.save(out/'latest_q.npy',q);(out/'trace.json').write_text(json.dumps(history,indent=2))
        print('STRICT110_QP_HOMOTOPY',row,flush=True)
        if length<checkpoint*.8:
            freeze(c,q,out/f'exact_checkpoint_it{it}');checkpoint=length
        if fraction<1e-6 or length<initial*1e-4:
            break
    np.save(out/'endpoint_q.npy',q)
    freeze(c,q,out/'exact_endpoint')


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--pair',type=int,nargs=2,required=True);p.add_argument('--kind',choices=['primal','dual'],default='primal');p.add_argument('--steps',type=int,default=200);a=p.parse_args();run(a.source,a.out,a.pair,a.kind,a.steps)
