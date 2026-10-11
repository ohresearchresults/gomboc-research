"""True volume-centroid transport inside a reference110 contact realization.
The objective is |g|/Rmax, so uniform scaling cannot fake centroid closure.
Contact equations are reconstructed, all noncontacts and orientations checked.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,pathlib,json,time,argparse
from scipy.linalg import svd
from scipy.optimize import linprog,minimize,LinearConstraint,Bounds
from scipy.sparse import csr_matrix,eye,hstack,vstack
from reference_contact_atlas import Atlas
from geometry import arrows

def normalized(e):
    root=int(np.argmax((e['X']*e['X']).sum(1)));a=e['X'][root];r=np.linalg.norm(a);dr=(a/r)@e['DX'][root];m=e['g']/r;M=e['Dg']/r-e['g'][:,None]*dr/r**2;vol=e['volume']/r**3;DV=e['DV']/r**3-3*e['volume']*dr/r**4;return m,M,vol,DV

def metric(e):
    DX=e['DX'].reshape(-1,e['DX'].shape[-1])/np.sqrt(np.mean(e['X']**2));DY=e['DY'].reshape(-1,e['DY'].shape[-1])/np.sqrt(np.mean(e['Y']**2));_,d,Vt=svd(np.vstack([DX,DY]),full_matrices=False,check_finite=False)
    if min(d)<1e-14:raise ValueError('singular reference contact chart')
    return Vt.T/d

def own(e):
    p=e['X']-e['g'];q=e['Y']/(1-e['Y']@e['g'])[:,None];a=arrows(p).max(1);b=arrows(q).max(1);return dict(S=int(np.sum(b<0)),U=int(np.sum(a<0)),minP=float(np.sort(a)[1]),minQ=float(np.sort(b)[1]))

def project_reference(c,z,floor,eps=1e-8,steps=35):
    trust=.012
    for it in range(steps):
        e=c.evaluate(z);v=e['mechanical'];merit=float(np.maximum(eps-v,0).sum())
        if min(v)>eps*.8 and e['S']==e['U']==1:return z,e,True
        W=metric(e);d=len(z);n=len(v);I=eye(d);O=csr_matrix((d,n));A=vstack([hstack([-csr_matrix(e['J']@W),-eye(n),csr_matrix((n,d))]),hstack([I,O,-I]),hstack([-I,O,-I]),hstack([-csr_matrix(e['gapJ']@W),csr_matrix((len(e['gapv']),n+d))])],format='csr');b=np.r_[v-eps,np.zeros(2*d),e['gapv']*.8];bound=trust/np.sqrt(d);lp=linprog(np.r_[np.zeros(d),np.ones(n),np.full(d,1e-7)],A_ub=A,b_ub=b,bounds=[(-bound,bound)]*d+[(0,None)]*(n+d),method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
        if not lp.success:trust*=.5;continue
        dz=W@lp.x[:d];accepted=False
        for level in range(12):
            zz=z+dz*2**-level
            try:ee=c.evaluate(zz);mm,_,vv,_=normalized(ee)
            except Exception:continue
            if vv>floor and np.maximum(eps-ee['mechanical'],0).sum()<merit*(1-1e-5):z=zz;accepted=True;break
        if accepted and level==0:trust=min(.06,trust*1.2)
        if not accepted:trust*=.4
        if trust<1e-9:break
    return z,c.evaluate(z),False

def run(source,out,steps=500,eps=1e-8):
    c=Atlas(source);z=c.initial.copy();e=c.evaluate(z);_,_,vol0,_=normalized(e);floor=.02*vol0;out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True);z,e,ok=project_reference(c,z,floor,eps,80)
    if not ok:raise ValueError('reference110 chamber could not be recovered')
    history=[];trust=.03;start=time.time();(out/'source.json').write_text(json.dumps(dict(source=str(pathlib.Path(source).resolve()),epsilon=eps,normalized_volume_floor=float(floor)),indent=2))
    for it in range(steps):
        e=c.evaluate(z);m,M,vol,DV=normalized(e);oo=own(e);v=e['mechanical'];row=dict(it=it,normalized_mass=float(np.linalg.norm(m)),normalized_volume=float(vol),referenceS=e['S'],referenceU=e['U'],reference_minimum=float(min(v)),own=oo,noncontact=e['minimum_gap'],trust=trust,seconds=time.time()-start);history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));np.savez(out/'latest.npz',z=z,X=e['X'],Q=e['Y']);print('CONTACT_CENTROID',json.dumps(row),flush=True)
        if oo['S']==oo['U']==1 and min(oo['minP'],oo['minQ'])>1e-10 and 17<=c.meta['E']<250:
            np.savez(out/'NOMINATION_OWN110.npz',z=z,X=e['X'],Q=e['Y']);print('POTENTIAL_CONTACT_BODY_REQUIRES_EXACT_PLAN_AUDIT',flush=True);return
        W=metric(e);d=len(z);A=np.vstack([-e['J']@W,-e['gapJ']@W,-DV@W]);b=np.r_[v-eps,e['gapv']*.8,vol-floor];C=M@W;bound=trust/np.sqrt(d);lp=linprog(np.r_[np.zeros(d),-1],A_ub=np.c_[A,np.zeros(len(A))],b_ub=b,A_eq=np.c_[C,m],b_eq=np.zeros(3),bounds=[(-bound,bound)]*d+[(0,1)],method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
        if not lp.success or lp.x[-1]<1e-10:
            trust*=.5;print('CONTACT_MASS_LINEAR_STALL',lp.message,flush=True)
            if trust<1e-9:break
            continue
        fraction=.8*lp.x[-1];qp=minimize(lambda x:(.5*x@x,x),lp.x[:-1]*.8,jac=True,method='SLSQP',bounds=Bounds(-bound,bound),constraints=[LinearConstraint(A,-np.inf,b),LinearConstraint(C,-fraction*m,-fraction*m)],options={'maxiter':120,'ftol':1e-13})
        if np.max(A@qp.x-b)>1e-8 or np.max(abs(C@qp.x+fraction*m))>1e-8:trust*=.4;continue
        dz=W@qp.x;accepted=False
        for level in range(10):
            try:zz,ee,ok=project_reference(c,z+dz*2**-level,floor,eps,35);mm,_,vv,_=normalized(ee)
            except Exception:continue
            if ok and vv>floor and np.linalg.norm(mm)<np.linalg.norm(m)*(1-1e-7):z=zz;accepted=True;row['alpha']=2**-level;break
        if accepted and level==0:trust=min(.15,trust*1.2)
        if not accepted:trust*=.4
        if trust<1e-9:print('CONTACT_CENTROID_LOCAL_STALL',flush=True);break

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--source',required=True);ap.add_argument('--out',required=True);ap.add_argument('--steps',type=int,default=500);ap.add_argument('--epsilon',type=float,default=1e-8);a=ap.parse_args();run(a.source,a.out,a.steps,a.epsilon)
