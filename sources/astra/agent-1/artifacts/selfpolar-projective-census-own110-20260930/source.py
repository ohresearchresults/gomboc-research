"""Physical projective search from a reference110 contact body.

The eight parameters define ONE physical embedding y=A x/(1+b.x), detA=1.
The mass is reintegrated on that same image; the polar is A^-T(q+b), then
translated by that actual centroid. Positive denominators preserve incidence.
No independent primal/dual metric or artificial centre is used for acceptance.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import pathlib,json,time,hashlib
import numpy as np
from scipy.optimize import differential_evolution,root,minimize
from contact_forest import ContactModel
from geometry import arrows
from persistence_search import pairs

class Found(Exception):pass

def run(source,input,out,iterations=800,seed=929572,objective='local',source_origin='reference'):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);c=ContactModel(source)
    controls=np.load(input)['z'];e=c.evaluate(controls,False)
    if source_origin=='reference':rawX,rawQ=e['X'],e['Y']
    elif source_origin=='centroid':rawX,rawQ=e['P'],e['Q']
    else:raise ValueError('Unknown explicitly requested source origin')
    scale=np.max(np.linalg.norm(rawX,axis=1));X=rawX/scale;Q=rawQ*scale;tt=c.tri
    if source_origin=='reference' and (sum(arrows(X).max(1)<0)!=1 or sum(arrows(Q).max(1)<0)!=1):raise ValueError('Input is not a physical reference110 seed')
    np.savez(out/'physical_parent.npz',X=X,Q=Q,triangles=tt,primal_edges=c.eu,polar_edges=c.es,controls=controls,scale=scale)
    (out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes())
    (out/'definition.json').write_text(json.dumps(dict(source=str(pathlib.Path(source).resolve()),input=str(pathlib.Path(input).resolve()),
        input_sha256=hashlib.sha256(pathlib.Path(input).read_bytes()).hexdigest(),iterations=iterations,seed=seed,E=c.meta['E'],objective=objective,source_origin=source_origin,
        scope='Single physical projective embedding with actual uniform centroid and unchanged genuine incidence; only own110 nominated'),indent=2))
    def body(z):
        A=np.array([[np.exp(z[0]),z[2],z[3]],[0,np.exp(z[1]),z[4]],[0,0,np.exp(-z[0]-z[1])]])
        b=np.asarray(z[5:]);den=1+X@b
        if den.min()<=.025:raise ValueError('Physical projective denominator outside explicit positive search domain')
        Y=(X@A.T)/den[:,None];H=np.linalg.solve(A.T,(Q+b).T).T;a=Y[tt]
        six=np.einsum('ij,ij->i',a[:,0],np.cross(a[:,1],a[:,2]));V=six.sum()/6
        if six.min()<=0 or V<=0:raise ValueError('Transformed physical mass is not positively oriented')
        g=(six[:,None]*a.sum(1)).sum(0)/(4*six.sum());P=Y-g;D=1-H@g
        if D.min()<=0:raise ValueError('Own centroid is not inside physical support body')
        R=H/D[:,None]
        return dict(X=Y,Q=H,P=P,R=R,A=A,b=b,g=g,volume=V,denmin=float(den.min()))
    calls=0;history=[];start=time.time();best=np.inf;bestz=np.zeros(8)
    def evaluate(z):
        nonlocal calls,best,bestz
        calls+=1
        try:d=body(z)
        except (ValueError,np.linalg.LinAlgError,FloatingPointError):return 1000.
        deficit=[];counts=[];margins=[]
        for A in [d['P'],d['R']]:
            rr=np.sum(A*A,axis=1);W=(A@A.T-rr[:,None])/rr[:,None];np.fill_diagonal(W,-np.inf)
            w=W.max(1);counts.append(int(sum(w<0)));root_id=int(np.argmax(rr));keep=np.arange(len(A))!=root_id
            deficit.extend(np.maximum(1e-9-w[keep],0));margins.append(float(w[keep].min()))
        U,S=counts
        if U==S==1:
            np.savez(out/'POTENTIAL_OWN110.npz',parameters=z,**d)
            (out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(calls=calls,S=S,U=U,E=c.meta['E'],margins=margins,seconds=time.time()-start),indent=2));raise Found()
        deficit=np.asarray(deficit);score=float(deficit.max(initial=0)+.1*deficit.sum()+1e-4*(S+U-2))
        bs=None
        if objective in ('persistence','census'):
            bs=[]
            for A,ed in [(d['P'],c.eu),(d['R'],c.es)]:
                pp,h=pairs(A,ed);bs.append((1-h[pp[:,1]]/np.sum(A[pp[:,0]]**2,axis=1)).tolist())
            allbars=bs[0]+bs[1]
            if objective=='persistence':score=float(max(allbars,default=0)+.05*sum(allbars)+1e-5*(S+U-2))
            else:score=float(S+U-2+.45*max(allbars,default=0)+.05*(np.mean(allbars) if allbars else 0))
        elif objective!='local':raise ValueError('Unknown explicit projective objective')
        if score<best:
            best=score;bestz=np.array(z)
            if bs is None:
                bs=[]
                for A,ed in [(d['P'],c.eu),(d['R'],c.es)]:
                    pp,h=pairs(A,ed);bs.append((1-h[pp[:,1]]/np.sum(A[pp[:,0]]**2,axis=1)).tolist())
            row=dict(calls=calls,score=score,S=S,U=U,E=c.meta['E'],parameters=list(z),P=bs[0],Qbars=bs[1],
                Pmax=max(bs[0],default=0),Qmax=max(bs[1],default=0),margins=margins,centroid=d['g'].tolist(),seconds=time.time()-start)
            history.append(row);np.savez(out/'best.npz',parameters=z,**d);(out/'history.json').write_text(json.dumps(history,indent=2))
            print('REFERENCE_PROJECTIVE_OWN110',json.dumps({k:v for k,v in row.items() if k not in ['parameters','P','Qbars']}),flush=True)
        return score
    # Compute the body's projective mass-centering parameter as an independent
    # explicit initialization. It has no inherited equilibrium claim.
    def centroid(b):
        try:return body(np.r_[np.zeros(5),b])['g']
        except (ValueError,np.linalg.LinAlgError):return np.full(3,1e3)
    sol=root(centroid,np.zeros(3),tol=1e-11)
    centered=None
    if sol.success and np.linalg.norm(centroid(sol.x))<1e-9:centered=np.r_[np.zeros(5),sol.x]
    (out/'projective_mass_initialization.json').write_text(json.dumps(dict(solver_success=bool(sol.success),parameter=sol.x.tolist(),
        actual_centroid=centroid(sol.x).tolist(),admitted=centered is not None),indent=2))
    rng=np.random.default_rng(seed);bounds=[(-1.5,1.5),(-1.5,1.5),(-2.5,2.5),(-2.5,2.5),(-2.5,2.5)]+[(-.85,.85)]*3
    population=[np.zeros(8)]
    if centered is not None:population.append(centered)
    while len(population)<100:
        r=rng.normal(size=8);r[:5]*=.25;r[5:]*=.1
        if len(population)%3==0:r=np.array([rng.uniform(a,b) for a,b in bounds])
        population.append(r)
    try:
        differential_evolution(evaluate,bounds,init=np.array(population),seed=seed,maxiter=iterations,workers=1,
            updating='immediate',tol=1e-10,atol=1e-11,polish=False)
        # The same exact numerical objective, now locally optimized after its
        # discrete escape witnesses were selected by the global exploration.
        minimize(evaluate,bestz,method='Nelder-Mead',bounds=bounds,options={'maxiter':8000,'xatol':1e-10,'fatol':1e-11})
    except Found:return
    (out/'FINITE_END.json').write_text(json.dumps(dict(calls=calls,best=best,seconds=time.time()-start,
        scope='Finite physical projective search ended without a qualifying own110 body'),indent=2))

if __name__=='__main__':
    import sys
    run(sys.argv[1],sys.argv[2],sys.argv[3],int(sys.argv[4]) if len(sys.argv)>4 else 800,
        objective=sys.argv[5] if len(sys.argv)>5 else 'local')
