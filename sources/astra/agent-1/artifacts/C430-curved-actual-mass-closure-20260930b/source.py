"""Actual centroid closure along a curved path in a reference110 chamber.

Unlike the old straight-ray constraint Dg*d=-alpha*g, this experiment only
requires decrease of |g|/R. The two transverse centroid components are free.
Every step retracts all physical contacts and rechecks reference and OWN counts.
No reference census or small mass residual is a qualifying Figure.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import pathlib,json,time
import numpy as np
from scipy.optimize import linprog,minimize,LinearConstraint,Bounds
from contact_forest import ContactModel
from contact_escape_choices import arrow_rows
from contact_retraction import retract
from contact_centroid_flow import normalized,metric
from geometry import arrows


class ReferenceBody(ContactModel):
    def __init__(self,source):super().__init__(source,1,1,'local')
    def evaluate(self,z,jacobian=True):
        e=super().evaluate(z,jacobian);e['ownS']=e['S'];e['ownU']=e['U']
        e['ownP']=e['P'];e['ownQ']=e['Q'];e['P']=e['X'];e['Q']=e['Y']
        if jacobian:e['DP']=e['DX'];e['DQ']=e['DY']
        vals=[];Js=[];roots=[];counts=[]
        for side in ('P','Q'):
            A=e[side];W=arrows(A);root=int(np.argmax((A*A).sum(1)));ii=np.arange(len(A));jj=W.argmax(1)
            sg=np.ones(len(A));sg[root]=-1;vals.append(sg*W[ii,jj]);roots.append([root]);counts.append(int(np.sum(W.max(1)<0)))
            if jacobian:
                _,J=arrow_rows(A,e['D'+side],ii,jj);Js.append(sg[:,None]*J)
        e['mechanical']=np.r_[tuple(vals)];e['roots']=roots;e['U']=counts[0];e['S']=counts[1]
        if jacobian:e['J']=np.vstack(Js)
        return e


def run(source,input,out,steps=400,eps=1e-9):
    source=pathlib.Path(source).resolve();input=pathlib.Path(input).resolve();out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False)
    c=ReferenceBody(source);z=np.load(input)['z'];e=c.evaluate(z)
    assert e['S']==e['U']==1 and e['mechanical'].min()>.8*eps and 17<=c.meta['E']<250
    floor=.2*normalized(e)[2];trust=.015;history=[];start=time.time()
    (out/'definition.json').write_text(json.dumps(dict(source=str(source),input=str(input),steps=steps,epsilon=eps,normalized_volume_floor=floor,
        scope='Physical reference110 chamber, curved uniform-centroid descent; only actual own110 with a separate exact audit can qualify'),indent=2))
    (out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes())
    for it in range(steps):
        e=c.evaluate(z);m,M,nv,DV=normalized(e);value=float(np.linalg.norm(m));v=e['mechanical']
        lengths=[float(np.min(np.linalg.norm(A[ed[:,0]]-A[ed[:,1]],axis=1))/np.sqrt(np.mean(A*A)))
                 for A,ed in [(e['X'],c.eu),(e['Y'],c.es)]]
        row=dict(it=it,ownS=e['ownS'],ownU=e['ownU'],referenceS=e['S'],referenceU=e['U'],E=c.meta['E'],mass_distance=value,
            mass=m.tolist(),reference_guard=float(v.min()),noncontact=e['minimum_gap'],normalized_volume=float(nv),lengths=lengths,trust=trust,seconds=time.time()-start)
        history.append(row);np.savez(out/'latest.npz',z=z,X=e['X'],Q=e['Y']);(out/'history.json').write_text(json.dumps(history,indent=2))
        if it%5==0:print('CURVED_MASS_CLOSURE',json.dumps(row),flush=True)
        if e['ownS']==e['ownU']==1:
            np.savez(out/'POTENTIAL_OWN110.npz',z=z,X=e['X'],Q=e['Y']);(out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(chart=str(source),input=str((out/'POTENTIAL_OWN110.npz').resolve())),indent=2));return
        if min(lengths)<1e-8:
            (out/'EDGE_EVENT.json').write_text(json.dumps(row,indent=2));return
        W=metric(e);d=c.free;bound=trust/np.sqrt(d);gradient=(m@M/max(value,1e-30))@W
        A=np.vstack([-e['J']@W,-e['gapJ']@W,-DV@W]);b=np.r_[v-eps,.8*e['gapv'],nv-floor]
        keep=b<=bound*np.abs(A).sum(1)+1e-10;A=A[keep];b=b[keep]
        scale=np.maximum(bound*np.abs(A).sum(1),1e-12);A/=scale[:,None];b/=scale
        lp=linprog(gradient/max(float(np.max(abs(gradient))),1e-30),A_ub=A,b_ub=b,bounds=[(-bound,bound)]*d,method='highs',
            options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
        if not lp.success or gradient@lp.x>=-max(1e-13,value*1e-10):
            trust*=.5
            if trust<1e-9:break
            continue
        descent=.8*gradient@lp.x;scale_d=max(abs(descent),1e-30)
        qp=minimize(lambda x:(.5*x@x,x),.8*lp.x,jac=True,method='SLSQP',bounds=Bounds(-bound,bound),
            constraints=[LinearConstraint(A,-np.inf,b),LinearConstraint(gradient/scale_d,-np.inf,-1.)],options={'ftol':1e-13,'maxiter':100})
        if max(float(np.max(A@qp.x-b)),float(gradient@qp.x/scale_d+1))>1e-8:
            trust*=.5
            if trust<1e-9:break
            continue
        dz=W@qp.x;accepted=False
        for level in range(12):
            try:
                zz,ee,receipt=retract(c,e,dz,2**-level)
                if ee['ownS']==ee['ownU']==1:
                    np.savez(out/'POTENTIAL_OWN110.npz',z=zz,X=ee['X'],Q=ee['Y']);(out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(chart=str(source),input=str((out/'POTENTIAL_OWN110.npz').resolve())),indent=2));return
                if ee['S']!=1 or ee['U']!=1 or ee['mechanical'].min()<.8*eps:continue
                rr=np.max(np.linalg.norm(ee['X'],axis=1));mm=ee['g']/rr;vv=ee['volume']/rr**3
                if vv>floor and np.linalg.norm(mm)<value-max(1e-13,value*1e-9):
                    z=zz;accepted=True;row.update(alpha=2**-level,retraction=receipt);break
            except (ValueError,RuntimeError,AssertionError,np.linalg.LinAlgError):continue
        if accepted and level==0:trust=min(.15,trust*1.2)
        elif accepted and level>=3:trust*=.7
        elif not accepted:trust*=.4
        if trust<1e-9:break
    (out/'history.json').write_text(json.dumps(history,indent=2))
