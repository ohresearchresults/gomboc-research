"""Physical radial deformation, anisotropic C2 section, and uniform mass root.

The radial law is applied to literal points; no smooth-body equilibrium claim
is transferred to their convex hull. A fresh bottom quadrilateral is completed
with a strict diameter-ball escape. The full hull and own mass decide admission.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import pathlib,json,time,hashlib
import numpy as np
from scipy.optimize import differential_evolution,minimize
from scipy.spatial import QhullError
from cyclic_flower_mass_goal import close_mass,Found
from free_primal_goal import mesh_points
from persistence_search import pairs

def run(source,out,iterations=360,seed=937281,objective='census'):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);data=pathlib.Path(source).read_bytes();(out/'source_body.npz').write_bytes(data)
    X=np.load(out/'source_body.npz')['X'];m=mesh_points(X);X=X[m['active']];rr=np.linalg.norm(X[1:],axis=1);logr=np.log(rr/np.median(rr))
    if max(abs(X[0,:2]))>1e-12:raise ValueError('Literal axial root not present')
    bounds=[(-.65,1.5),(-.35,.35),(-1.2,1.2),(-np.pi/2,np.pi/2),(-1.1,1.1),(.08,.92),(.06,.98)]
    (out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes());(out/'definition.json').write_text(json.dumps(dict(source=str(pathlib.Path(source).resolve()),sha256=hashlib.sha256(data).hexdigest(),iterations=iterations,seed=seed,objective=objective,bounds=bounds,
        scope='One physical radial/anisotropic embedding with actual maximal hull and uniform mass closure; only own110 qualifies'),indent=2))
    def body(z):
        p,b,s,theta,v,a,beta=z;c=np.cos(theta);t=np.sin(theta);R=np.array([[c,-t],[t,c]]);A=R@np.diag([np.exp(s),np.exp(-s)])@R.T
        Y=X.copy();Y[1:]*=np.exp(p*logr+b*logr**2)[:,None];Y[1:,:2]=Y[1:,:2]@A.T;Y[1:,2]*=np.exp(v)
        parent=Y[1+int(np.argmin(Y[1:,2]))];xy=parent[:2];q=np.r_[a*xy+beta*np.sqrt(a*(1-a))*np.array([-xy[1],xy[0]]),parent[2]]
        if q@(parent-q)<=1e-12:raise ValueError('Bottom completion escape failed')
        Y=np.r_[Y,[q,q*np.array([-1,-1,1])]];return close_mass(Y)
    calls=0;best=float('inf');bestz=None;hist=[];bad={};start=time.time();rng=np.random.default_rng(seed)
    def evaluate(z):
        nonlocal calls,best,bestz
        calls+=1
        try:
            Y,closed=body(z);mm=mesh_points(Y);row=mm['row']
            if not 17<=row['E']<=249:return 100+max(row['E']-249,0)
            if row['S']==row['U']==1:
                np.savez(out/'POTENTIAL_OWN110.npz',X=Y,Q=mm['Q'],parameters=z);(out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(calls=calls,**row),indent=2));raise Found()
            if not closed:return 30+abs(float(mm['g'][2]))
            if row['U']!=1 or max(abs(mm['g']))>2e-9:raise ValueError('Independent own U1/mass check failed')
            pp,h=pairs(mm['R'],mm['eq']);bars=1-h[pp[:,1]]/np.sum(mm['R'][pp[:,0]]**2,axis=1);qmax=float(max(bars,default=0))
            if objective=='census':score=float(row['S']-1+.7*qmax+.1*(np.mean(bars) if len(bars) else 0))
            elif objective=='barrier':score=float(qmax+.03*bars.sum())
            else:raise ValueError('Unknown explicit objective')
            if score<best:
                best=score;bestz=np.array(z);record=dict(calls=calls,score=score,Qmax=qmax,Qbars=bars.tolist(),parameters=list(z),seconds=time.time()-start,**row);hist.append(record)
                np.savez(out/'best.npz',X=Y[mm['active']],Q=mm['Q'],parameters=z);(out/'history.json').write_text(json.dumps(hist,indent=2));print('RADIAL_CYCLIC_GOAL',json.dumps({k:v for k,v in record.items() if k not in ['Qbars','parameters']}),flush=True)
            return score
        except (ValueError,RuntimeError,AssertionError,QhullError,np.linalg.LinAlgError) as err:
            key=str(err).split('\n')[0];bad[key]=bad.get(key,0)+1;return 100.
    pop=[np.array([0.,0.,0.,0.,0.,.5,.5])]
    while len(pop)<84:
        if len(pop)<28:
            z=pop[0]+rng.normal(size=7)*np.array([.15,.07,.2,.5,.2,.12,.15]);z=np.clip(z,np.array(bounds)[:,0],np.array(bounds)[:,1])
        else:z=np.array([rng.uniform(a,b) for a,b in bounds])
        pop.append(z)
    try:
        differential_evolution(evaluate,bounds,init=np.array(pop),seed=seed,maxiter=iterations,workers=1,updating='immediate',tol=1e-9,atol=1e-10,polish=False)
        if bestz is not None:minimize(evaluate,bestz,method='Nelder-Mead',bounds=bounds,options={'maxiter':4500,'xatol':1e-9,'fatol':1e-10})
    except Found:return
    (out/'FINITE_END.json').write_text(json.dumps(dict(calls=calls,best=best,failures=bad,seconds=time.time()-start,scope='Finite radial mass-closed physical family ended without a qualifying body'),indent=2))

if __name__=='__main__':
    import sys
    run(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 360,objective=sys.argv[4] if len(sys.argv)>4 else 'census')
