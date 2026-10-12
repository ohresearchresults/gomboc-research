"""Minimum-norm, mass-aware positive-escape spring homotopy.
The small strictly convex quadratic direction problem is solved via its nonnegative dual.
Numerical discovery only; every returned graph/body needs exact audits.
"""
from pathlib import Path
import json,time,sys,collections
import numpy as np
from scipy.optimize import minimize
from tutte_coarsen import ref_exact,dynamicstate,reduced
from tutte_opt import PhysicalTutte
from fit_restoration import embedded_faces

def project(A,b):
    scale=np.maximum(np.linalg.norm(A,axis=1),1e-10);aa=A/scale[:,None];bb=b/scale
    gram=aa@aa.T
    def objective(lam):
        g=gram@lam+bb
        return .5*lam@(g+bb),g
    sol=minimize(objective,np.zeros(len(bb)),jac=True,method='L-BFGS-B',bounds=[(0,None)]*len(bb),options={'ftol':1e-16,'gtol':1e-12,'maxiter':1000,'maxls':30,'maxcor':30})
    d=-aa.T@sol.x
    err=(aa@d-bb).max()
    return d,err,sol.nit

def close_minorm(body,edge,steps=160,keep=8e-6):
    theta=np.zeros(body.K);k=body.free_edges.index(edge);ind=np.array([j for j in range(body.K) if j!=k]);delta=.03;t0=time.time()
    for it in range(steps):
        st=dynamicstate(body,theta);vals=st['vals'];J=st['J']
        if it%10==0:
            ref,new,drop=reduced(body,theta,edge);print('PROJECT_REMOVE',edge,it,'sec',round(time.time()-t0,2),'logw',theta[k],'cos',vals.min(),'drop',drop['audit']['counts'],'delta',delta,flush=True)
            if drop['audit']['counts']==[1,1,0] and drop['audit']['min_gap']>1e-8:return theta,'drop_winner'
        if theta[k]<-15:return theta,'weight_small'
        dk=-delta;A=-J[:,ind];b=vals-keep+J[:,k]*dk;dx,err,nit=project(A,b)
        if err>1e-7 or np.max(abs(dx))>1.:
            delta*=.5
            if delta<1e-8:return theta,'projection_stall'
            continue
        direction=np.zeros(body.K);direction[k]=dk;direction[ind]=dx;accept=False
        for ls in range(24):
            alpha=2.**(-ls);nt=theta+alpha*direction
            try:ns=body.fullstate(nt,jac=False);newcos=ns['vals'].min()
            except Exception:continue
            if newcos>keep*.8 and ns['gaps'][~body.inc].min()>-1e-8 and ns['det'].min()>-1e-10 and ns['V']>0:
                theta=nt;accept=True;delta=min(.4,delta*(1.3 if ls==0 else 1. if ls<3 else .65));break
        if not accept:
            delta*=.4
            if delta<1e-8:return theta,'line_stall'
    return theta,'budget'

if __name__=='__main__':
    R=Path(__file__).parent;name=sys.argv[1] if len(sys.argv)>1 else 'C642_CONTACT26_82';ref=json.loads((R/(name+'_TUTTE_REFERENCE.json')).read_text());body=PhysicalTutte(ref,ref['G']);body.setup(stable=3,unstable=2);zero=np.zeros(body.K);st=dynamicstate(body,zero)
    H=set(tuple(map(int,l.split())) for l in (R/'H213_edges.txt').read_text().splitlines());candidate=[]
    for e in body.free_edges:
        if e in H:continue
        try:
            fs,rt,df=embedded_faces([t for t in body.edges if t!=e],{int(k):v for k,v in ref['rotation'].items()})
            if min(map(len,rt.values()))<3 or len(fs)!=len(body.faces)-1:continue
            f,g=body.df[e],body.df[e[::-1]];length=np.linalg.norm(st['P'][f]-st['P'][g]);candidate.append((length,e))
        except Exception:continue
    candidate.sort();print('CANDIDATES',candidate[:20],flush=True);ledger=[]
    for rank,(length,edge) in enumerate(candidate[:15]):
        theta,status=close_minorm(body,edge);nf,new,nst=reduced(body,theta,edge);rr=nst['audit'];prefix=name+f'_PROJECT_SPRING_{edge[0]}_{edge[1]}'
        np.savez(R/(prefix+'.npz'),theta=theta,q=nst['q'],P=nst['P']);(R/(prefix+'_REFERENCE.json')).write_text(json.dumps(nf,separators=(',',':')));(R/(prefix+'_faces.json')).write_text(json.dumps(new.primal_faces,separators=(',',':')));(R/(prefix+'_numeric.json')).write_text(json.dumps(rr,indent=2))
        ledger.append(dict(edge=edge,status=status,logweight=float(theta[body.free_edges.index(edge)]),audit=rr));(R/(name+'_PROJECT_SPRING_LEDGER.json')).write_text(json.dumps(ledger,indent=2));print('PROJECT_REMOVAL_END',edge,status,rr,flush=True)
        if rr['counts']==[1,1,0] and rr['min_gap']>1e-8 and rr['max_incidence_error']<1e-7:
            print('SPRING_COARSEN_WINNER',prefix,flush=True);break
