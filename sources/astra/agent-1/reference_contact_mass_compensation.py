"""Close the actual centroid of a reference-211 cap in its full contact family.

Reference guards and actual own-centroid counts are separate throughout. A
small mass residual never triggers a winning claim. All physical contacts,
noncontacts, orientations and volume are checked after each finite step.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,pathlib,json,time,contextlib
import numpy as np
from scipy.optimize import linprog,minimize,LinearConstraint,Bounds
from contact_forest import ContactModel
from contact_retraction import retract
from geometry import arrows,halfspace_mesh
from stable_face_augmentation import halfspaces
from make_contact_atlas import make

def reference(e,derivatives=True,stable_guards=True):
    values=[];jac=[];counts=[]
    for A,D in [(e['X'],e.get('DX')),(e['Y'],e.get('DY'))]:
        W=arrows(A);w=W.max(1);counts.append(int(np.sum(w<0)));elder=int(np.argmax((A*A).sum(1)));other=[int(i) for i in np.flatnonzero(w<0) if i!=elder];ix=np.arange(len(A));parents=W.argmax(1);sign=np.ones(len(A));sign[elder]=-1;keep=np.ones(len(A),bool)
        if len(counts)==2 and len(other)==1:keep[other[0]]=False
        include=stable_guards or len(counts)==1
        if include:values.append((sign*w)[keep])
        if derivatives and include:
            delta=A[parents]-A;rr=(A*A).sum(1);dd=(delta*delta).sum(1);den=np.sqrt(rr*dd);v=(A*delta).sum(1)/den;ga=(delta-A)/den[:,None]-v[:,None]*(A/rr[:,None]-delta/dd[:,None]);gb=A/den[:,None]-v[:,None]*delta/dd[:,None];J=sign[:,None]*(np.einsum('ic,icp->ip',ga,D)+np.einsum('ic,icp->ip',gb,D[parents]));jac.append(J[keep])
    return np.concatenate(values),np.vstack(jac) if derivatives else None,dict(referenceU=counts[0],referenceS=counts[1])

def close_mass(chart,out,steps=70,stable_limit=2):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);c=ContactModel(chart,1,2,'local',exempt_junior=True);z=c.initial.copy();e=c.evaluate(z);volume0=e['volume'];trust=.015;history=[];start=time.time()
    for it in range(steps):
        e=c.evaluate(z);v,J,ref=reference(e,stable_guards=bool(stable_limit));r=np.sqrt(np.mean(np.sum(e['X']**2,axis=1)));mass_norm=float(np.linalg.norm(e['g'])/r);row=dict(it=it,relative_mass_error=mass_norm,minimum_reference=float(v.min()),stable_limit=stable_limit,ownS=e['S'],ownU=e['U'],E=c.meta['E'],trust=trust,seconds=time.time()-start,**ref);history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));np.savez(out/'latest.npz',z=z,X=e['X'],Q=e['Y']);print('REFERENCE_CONTACT_MASS',json.dumps(row),flush=True)
        if e['S']==e['U']==1:
            own=np.r_[np.sort(arrows(e['P']).max(1))[1:],np.sort(arrows(e['Q']).max(1))[1:]]
            if own.min()>1e-9:np.savez(out/'POTENTIAL_OWN110.npz',z=z,X=e['X'],Q=e['Y']);return True
        if mass_norm<1e-12 and e['U']==1 and (not stable_limit or e['S']<=stable_limit) and v.min()>1e-9:
            np.savez(out/('CENTROID_CLOSED_STRICT_CLASS.npz' if stable_limit else 'CENTROID_CLOSED_UNIQUE_U.npz'),z=z,X=e['X'],Q=e['Y']);return True
        if ref['referenceU']!=1 or (stable_limit and not 1<=ref['referenceS']<=stable_limit) or v.min()<=0:raise ValueError('source left the permitted strict reference chamber')
        W=c.metric(e);d=c.free;bound=trust/np.sqrt(d);A=np.vstack([-J@W,-e['gapJ']@W,-e['DV']@W]);rhs=np.r_[v-1e-8,.8*e['gapv'],e['volume']-.3*volume0];keep=rhs<=bound*np.abs(A).sum(1)+1e-10;A=A[keep];rhs=rhs[keep];scale=np.maximum(bound*np.abs(A).sum(1),1e-12);A/=scale[:,None];rhs/=scale;M=e['Dg']@W;g=e['g']
        mass_scale=max(float(np.linalg.norm(g)),1e-15);EM=M/mass_scale;eg=g/mass_scale
        lp=linprog(np.r_[np.zeros(d),-1.],A_ub=np.c_[A,np.zeros(len(A))],b_ub=rhs,A_eq=np.c_[EM,eg],b_eq=np.zeros(3),bounds=[(-bound,bound)]*d+[(0,1)],method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9,'time_limit':20})
        if not lp.success or lp.x[-1]<1e-7:
            trust*=.5
            if trust<1e-9:return False
            continue
        fraction=.9*lp.x[-1];qp=minimize(lambda x:(.5*x@x,x),lp.x[:-1]*.9,jac=True,method='SLSQP',bounds=Bounds(-bound,bound),constraints=[LinearConstraint(A,-np.inf,rhs),LinearConstraint(EM,-fraction*eg,-fraction*eg)],options={'ftol':1e-14,'maxiter':100})
        if np.max(A@qp.x-rhs)>1e-8 or np.max(abs(EM@qp.x+fraction*eg))>1e-8:
            trust*=.5
            if trust<1e-9:return False
            continue
        dz=W@qp.x;accepted=False
        for level in range(14):
            try:zz,ee,receipt=retract(c,e,dz,2**-level);vv,_,rr=reference(ee,False,stable_guards=bool(stable_limit))
            except (ValueError,RuntimeError,np.linalg.LinAlgError):continue
            if rr['referenceU']==1 and (not stable_limit or 1<=rr['referenceS']<=stable_limit) and vv.min()>5e-9 and ee['volume']>.3*volume0 and np.linalg.norm(ee['g'])<np.linalg.norm(g)*(1-1e-6):z=zz;accepted=True;row['retraction']=receipt;break
        if accepted and level==0:trust=min(.1,trust*1.2)
        if not accepted:trust*=.4
        if trust<1e-9:return False
    return False

def run(scout,out,limit=10,stable_limit=2,selection='score'):
    if stable_limit not in (0,2):raise ValueError('Supported stable limits: 2, or 0 for unrestricted')
    scout=pathlib.Path(scout);out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);P=np.load(scout/'original.npz')['X'];rows=json.loads((scout/'screen.json').read_text());rows=sorted([r for r in rows if r.get('referenceU')==1 and (not stable_limit or 1<=r.get('referenceS',999)<=stable_limit) and 17<=r['E']<249],key=lambda r:r['score'] if selection=='score' else max(r['Q'],default=0));history=[]
    (out/'definition.json').write_text(json.dumps(dict(scout=str(scout.resolve()),stable_limit=stable_limit,selection=selection,scope='Physical centroid closure; stable roots unrestricted when stable_limit=0; not a goal certificate'),indent=2))
    for trial,r in enumerate(rows[:limit]):
        folder=out/f'trial{trial:02d}-sample{r["sample"]:05d}';folder.mkdir();X=np.r_[P,np.array(r['added_vertex'])[None]];Q=halfspaces(X);m=halfspace_mesh(Q);Y=Q[m['active']];proposal=dict(scope='Reference-class cap at old origin, actual centroid still to be closed',source=str((scout/'screen.json').resolve()),sample=r['sample'],V=len(m['X']),E=len(m['edges']),F=len(Y),faces=m['faces'],edges=m['edges'].tolist(),active=list(range(len(Y))),raw_vertices=[[str(v) for v in p] for p in m['X']],raw_halfspaces=[[str(v) for v in p]+['1'] for p in Y]);(folder/'proposal.json').write_text(json.dumps(proposal,indent=2));make(folder/'proposal.json',folder/'chart',balanced=True)
        try:
            with (folder/'calculation.log').open('w') as log,contextlib.redirect_stdout(log):ok=close_mass(folder/'chart',folder/'mass-closure',stable_limit=stable_limit)
            c=ContactModel(folder/'chart',1,2,'local',exempt_junior=True);e=c.evaluate(np.load(folder/'mass-closure/latest.npz')['z'],False);row=dict(trial=trial,sample=r['sample'],closed=ok,S=e['S'],U=e['U'],E=c.meta['E'],mass_norm=float(np.linalg.norm(e['g'])),Pmax=max((b['relative'] for b in e['bars'][0]),default=0),Qmax=max((b['relative'] for b in e['bars'][1]),default=0),chart=str((folder/'chart').resolve()),input=str((folder/'mass-closure/latest.npz').resolve()))
            if (folder/'mass-closure/POTENTIAL_OWN110.npz').exists():
                (out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(chart=str((folder/'chart').resolve()),input=str((folder/'mass-closure/POTENTIAL_OWN110.npz').resolve())),indent=2));return
        except (ValueError,AssertionError,RuntimeError,np.linalg.LinAlgError) as error:row=dict(trial=trial,sample=r['sample'],error=repr(error))
        history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));print('CONTACT_MASS_COMPENSATION_TRIAL',json.dumps(row),flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--scout',required=True);ap.add_argument('--out',required=True);ap.add_argument('--limit',type=int,default=10);ap.add_argument('--stable-limit',type=int,choices=[0,2],default=2);ap.add_argument('--selection',choices=['score','qdepth'],default='score');a=ap.parse_args();run(a.scout,a.out,a.limit,a.stable_limit,a.selection)
