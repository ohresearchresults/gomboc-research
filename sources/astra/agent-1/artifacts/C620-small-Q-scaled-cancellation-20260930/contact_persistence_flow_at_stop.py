"""True-centroid persistence descent with full planar contact preservation.

Every predictor is corrected on the same physical own-centroid body. Geometry is
the full contact realization, so planar quadrilateral ownership is preserved even
when a seed's more restrictive construction family is released.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,json,pathlib,time
import numpy as np
from scipy.optimize import linprog,minimize,LinearConstraint,Bounds
from contact_forest import ContactModel,correct
from contact_retraction import retract

def objective(c,e,side='P'):
    s=0 if side=='P' else 1
    if not e['bars'][s]:return 0.,np.zeros(c.free)
    record=max(e['bars'][s],key=lambda r:r['relative']);b=record['birth'];edges=c.eu if s==0 else c.es;u,v=edges[record['edge']]
    P=e['P'] if s==0 else e['Q'];DP=e['DP'] if s==0 else e['DQ'];a=P[u];d=P[v]-a;t=np.clip(-a@d/(d@d),0,1);f=a+t*d;h=f@f;born=P[b]@P[b]
    dh=2*f@((1-t)*DP[u]+t*DP[v]);db=2*P[b]@DP[b]
    return float(1-h/born),-dh/born+h*db/born**2

def normalized_volume(e):
    P=e['P'];r=np.sqrt(np.mean(np.sum(P*P,axis=1)));dr=np.einsum('ic,icp->p',P,e['DP'])/(len(P)*r)
    return e['volume']/r**3,e['DV']/r**3-3*e['volume']*dr/r**4

def run(source,out,side='P',input=None,steps=300,eps=1e-7,edge_event_tolerance=None):
    c=ContactModel(source,2 if side=='P' else 1,1 if side=='P' else 2,'local',exempt_junior=True);z=np.load(input)['z'] if input else c.initial.copy();out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True)
    e=c.evaluate(z);nv,_=normalized_volume(e);floor=.05*nv;trust=.02;history=[];start=time.time()
    (out/'source.json').write_text(json.dumps(dict(source=str(pathlib.Path(source).resolve()),side=side,chart_E=c.meta['E'],normalized_volume_floor=float(floor),junior_root_guard='exempt from positive and negative guard; its disappearance is allowed',edge_event_tolerance=edge_event_tolerance),indent=2))
    for it in range(steps):
        e=c.evaluate(z);value,gradient=objective(c,e,side);nv,DV=normalized_volume(e);v=e['mechanical']
        row=dict(it=it,S=e['S'],U=e['U'],E=c.meta['E'],objective=value,minimum=float(v.min()),minimum_gap=e['minimum_gap'],minimum_turn=e['minimum_turn'],normalized_volume=float(nv),trust=trust,seconds=time.time()-start);history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));np.savez(out/'latest.npz',z=z,X=e['X'],Q=e['Y'])
        if it%5==0:print('CONTACT_PERSISTENCE',json.dumps(row),flush=True)
        if e['S']==e['U']==1 and v.min()>1e-10:
            np.savez(out/'POTENTIAL_OWN110.npz',z=z,X=e['X'],Q=e['Y']);print('POTENTIAL_TRUE_CONTACT_BODY_REQUIRES_RATIONAL_AUDIT',flush=True);return
        if e['S']>c.root_counts[1] or e['U']>c.root_counts[0]:raise ValueError('search iterate lost its strict equilibrium class')
        if edge_event_tolerance is not None:
            lengths=[float(np.min(np.linalg.norm(A[ed[:,0]]-A[ed[:,1]],axis=1))/np.sqrt(np.mean(A*A))) for A,ed in [(e['X'],c.eu),(e['Y'],c.es)]]
            if min(lengths)<edge_event_tolerance:
                (out/'EDGE_EVENT.json').write_text(json.dumps(dict(scope='Small edge nominates a new contact complex; no exact incidence claim',primal=lengths[0],polar=lengths[1],threshold=edge_event_tolerance),indent=2));print('EXPLICIT_TOPOLOGY_EVENT_REQUEST',lengths,flush=True);return
        W=c.metric(e);d=c.free;bound=trust/np.sqrt(d);A=np.vstack([-e['J']@W,-e['gapJ']@W,-DV@W]);rhs=np.r_[v-eps,e['gapv']*.8,nv-floor]
        keep=rhs<=bound*np.abs(A).sum(1)+1e-10;A=A[keep];rhs=rhs[keep]
        scale=np.maximum(bound*np.abs(A).sum(1),1e-12);A=A/scale[:,None];rhs=rhs/scale;gg=gradient@W
        objective_scale=max(float(np.max(abs(gg))),1e-30)
        decrease_tolerance=max(1e-14,1e-9*value)
        lp=linprog(gg/objective_scale,A_ub=A,b_ub=rhs,bounds=[(-bound,bound)]*d,method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
        if not lp.success or gg@lp.x>-.1*decrease_tolerance:
            trust*=.5
            if trust<1e-9:break
            continue
        descent=.8*(gg@lp.x);descent_scale=max(abs(descent),1e-30)
        # The progress inequality must be dimensionless: an absolute1e-8
        # residual can otherwise swallow the entire requested tiny-Q step.
        qp=minimize(lambda x:(.5*x@x,x),lp.x*.8,jac=True,method='SLSQP',bounds=Bounds(-bound,bound),constraints=[LinearConstraint(A,-np.inf,rhs),LinearConstraint(gg/descent_scale,-np.inf,-1.)],options={'ftol':1e-13,'maxiter':90})
        row.update(predicted_decrease=float(-descent),qp_relative_progress_residual=float(gg@qp.x/descent_scale+1))
        if np.max(A@qp.x-rhs)>1e-8 or gg@qp.x/descent_scale>-1+1e-8:
            trust*=.5
            if trust<1e-9:break
            continue
        dz=W@qp.x;accepted=False
        for level in range(8):
            try:
                zz,ee,receipt=retract(c,e,dz,2**-level)
                if ee['S']>c.root_counts[1] or ee['U']>c.root_counts[0] or ee['mechanical'].min()<.8*eps:
                    zz,ee,ok=correct(c,zz,out/f'correct{it:04d}-{level}',steps=14,eps=eps,trust=.003,verbose=False,polish_margin=True,physical_retraction=True)
                    if not ok:continue
                if ee['S']==ee['U']==1:
                    np.savez(out/'POTENTIAL_OWN110.npz',z=zz,X=ee['X'],Q=ee['Y']);print('POTENTIAL_TRUE_CONTACT_BODY_REQUIRES_RATIONAL_AUDIT',flush=True);return
                newvalue=max([r['relative'] for r in ee['bars'][0 if side=='P' else 1]],default=0)
                rr=np.sqrt(np.mean(np.sum(ee['P']**2,axis=1)))
                if ee['volume']/rr**3>floor and ee['mechanical'].min()>.8*eps and newvalue<value-decrease_tolerance:
                    z=zz;accepted=True;row['accepted_alpha']=2**-level;row['retraction']=receipt;break
            except (ValueError,AssertionError,RuntimeError,np.linalg.LinAlgError):continue
        if accepted and level==0:trust=min(.15,trust*1.2)
        if accepted and level>=3:trust*=.7
        if not accepted:trust*=.4
        if trust<1e-9:break

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--source',required=True);ap.add_argument('--out',required=True);ap.add_argument('--input');ap.add_argument('--side',choices=['P','Q'],default='P');ap.add_argument('--steps',type=int,default=300);a=ap.parse_args();run(a.source,a.out,a.side,a.input,a.steps)
