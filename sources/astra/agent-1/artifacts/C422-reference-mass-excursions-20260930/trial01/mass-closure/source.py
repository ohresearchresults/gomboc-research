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
from scipy.sparse import csr_matrix,eye,hstack,vstack,diags
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


def repair_reference(c,z,out,eps=1e-9,steps=100):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);history=[];trust=.003
    floor=.2*normalized(c.evaluate(z))[2]
    for it in range(steps):
        e=c.evaluate(z);v=e['mechanical'];value=float(np.maximum(eps-v,0).sum())
        row=dict(it=it,referenceS=e['S'],referenceU=e['U'],ownS=e['ownS'],ownU=e['ownU'],merit=value,minimum=float(v.min()),trust=trust)
        history.append(row);np.savez(out/'latest.npz',z=z,X=e['X'],Q=e['Y']);(out/'history.json').write_text(json.dumps(history,indent=2))
        if e['ownS']==e['ownU']==1:
            np.savez(out/'POTENTIAL_OWN110.npz',z=z,X=e['X'],Q=e['Y']);return z,e,False
        if e['S']==e['U']==1 and v.min()>.8*eps:return z,e,True
        W=metric(e);d=c.free;n=len(v);bound=trust/np.sqrt(d);J=e['J']@W
        scale=np.maximum(bound*np.abs(J).sum(1),1e-12);_,_,nv,DV=normalized(e)
        G=np.vstack([e['gapJ']@W,DV@W]);b=np.r_[.8*e['gapv'],nv-floor]
        keep=b<=bound*np.abs(G).sum(1)+1e-10;G=G[keep];b=b[keep];gs=np.maximum(bound*np.abs(G).sum(1),1e-12)
        I=eye(d);O=csr_matrix((d,n));A=vstack([hstack([-csr_matrix(J/scale[:,None]),-diags(1/scale),csr_matrix((n,d))]),
            hstack([-csr_matrix(G/gs[:,None]),csr_matrix((len(b),n+d))]),hstack([I,O,-I]),hstack([-I,O,-I])],format='csr')
        rhs=np.r_[(v-eps)/scale,b/gs,np.zeros(2*d)]
        lp=linprog(np.r_[np.zeros(d),np.ones(n),np.full(d,1e-7)],A_ub=A,b_ub=rhs,bounds=[(-bound,bound)]*d+[(0,None)]*(n+d),method='highs',
            options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
        if not lp.success:trust*=.5;continue
        dz=W@lp.x[:d];accepted=False
        for level in range(12):
            try:
                zz,ee,_=retract(c,e,dz,2**-level);r=np.max(np.linalg.norm(ee['X'],axis=1))
                if ee['volume']/r**3>floor and np.maximum(eps-ee['mechanical'],0).sum()<value*(1-1e-6):
                    z=zz;accepted=True;break
            except (ValueError,RuntimeError,AssertionError,np.linalg.LinAlgError):continue
        if accepted and level==0:trust=min(.1,trust*1.2)
        elif not accepted:trust*=.4
        if trust<1e-9:break
    return z,c.evaluate(z),False


def continuation(source,input,out,rounds=35,steps=300,eps=1e-9):
    from merge_contact_facets import run as merge_facets
    from merge_contact_vertices import run as merge_vertices
    from repair_contact_domain import run as admit
    source=pathlib.Path(source);input=pathlib.Path(input);out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);history=[]
    (out/'definition.json').write_text(json.dumps(dict(source=str(source.resolve()),input=str(input.resolve()),rounds=rounds,steps=steps,eps=eps,
        scope='Actual-centroid closure through explicitly reconstructed reference110 hull chambers; complete own census is the acceptance gate'),indent=2))
    for k in range(rounds):
        p=out/f'stage{k:03d}';p.mkdir();c=ReferenceBody(source);z=np.load(input)['z'];e=c.evaluate(z)
        if e['S']!=1 or e['U']!=1 or e['mechanical'].min()<.8*eps:
            z,e,ok=repair_reference(c,z,p/'reference-repair',eps=eps);np.savez(p/'repaired.npz',z=z,X=e['X'],Q=e['Y']);input=p/'repaired.npz'
            if e['ownS']==e['ownU']==1:
                (out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(chart=str(source.resolve()),input=str(input.resolve())),indent=2));return
            if not ok:return
        run(source,input,p/'flow',steps=steps,eps=eps)
        if (p/'flow/POTENTIAL_OWN110.json').exists():
            (out/'POTENTIAL_OWN110.json').write_bytes((p/'flow/POTENTIAL_OWN110.json').read_bytes());return
        input=p/'flow/latest.npz';row=json.loads((p/'flow/history.json').read_text())[-1];row.pop('retraction',None)
        row.update(stage=k,chart=str(source.resolve()),input=str(input.resolve()));history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2))
        if not (p/'flow/EDGE_EVENT.json').exists():return
        kind='facets' if row['lengths'][1]<1e-8 else 'vertices';target=p/f'merge-{kind}'
        try:
            if kind=='facets':merge_facets(source,input,target,1e-8,300,300,'balanced',cleanup=True)
            else:merge_vertices(source,input,target,1e-8,300,300,'balanced')
            nextinput=target/'realization.npz'
        except (ValueError,RuntimeError,AssertionError,np.linalg.LinAlgError) as err:
            (p/'UNADMITTED_PROPOSAL.json').write_text(json.dumps(dict(error=repr(err)),indent=2))
            if not (target/'chart/chart.json').exists():return
            try:admit(target/'chart',target/'admission',nU=300,nS=300,eps=1e-10,steps=100)
            except (ValueError,RuntimeError,AssertionError,np.linalg.LinAlgError) as error:
                (p/'ADMISSION_ERROR.json').write_text(json.dumps(dict(error=repr(error)),indent=2));return
            nextinput=target/'admission/ADMITTED.npz'
            if not nextinput.exists():return
        source=target/'chart';input=nextinput;c=ReferenceBody(source);c.evaluate(np.load(input)['z'])
        if not 17<=c.meta['E']<250:raise ValueError('New complex outside requested edge range')
