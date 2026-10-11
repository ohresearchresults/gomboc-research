"""Direct search for own110 in the explicit homogeneous polar spiral family.
Both the limiting reference-S1 body and the mass-closed body are checked at
their OWN centroids. Failed mass closure is not used to discard a qualifying
actual body. Piecewise section integration only accelerates a scalar root;
the final boundary volume and moment remain independently recomputed.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import pathlib,json,time
import numpy as np
from scipy.optimize import differential_evolution,brentq
from scipy.spatial import QhullError
from centred_polar_spiral import construct
from geometry import arrows,halfspace_mesh,census
from persistence_search import pairs
from polyhedral_slab_mass import SlabMass

class Found(Exception):pass

def run(pool,out,iterations=450,seed=928113):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);history=[];calls=0;best=np.inf;start=time.time()
    old=json.loads(pathlib.Path(pool).read_text());rng=np.random.default_rng(seed)
    (out/'definition.json').write_text(json.dumps(dict(pool=str(pathlib.Path(pool).resolve()),iterations=iterations,seed=seed,
        scope='Direct same-body own110 search; intermediate and mass-closed actual centroids checked; no residual or reference success'),indent=2))
    (out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes())
    def nominate(Q,m,parameters,stage):
        st=census(m,0)
        if 17<=st['E']<250 and st['S']==st['U']==1:
            np.savez(out/'POTENTIAL_OWN110.npz',Q=Q,X=m['X'],parameters=parameters)
            (out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(stage=stage,calls=calls,**st),indent=2));raise Found()
        return st
    def evaluate(parameters):
        nonlocal calls,best
        calls+=1;z=np.array(parameters);z[6]=10**z[6]
        try:
            other,_=construct(z);W=arrows(other);sinks=np.flatnonzero(W.max(1)<=1e-12)
            if not len(sinks) or np.any(other[sinks,2]>=0):return 3.
            hmax=float(np.min(-other[sinks,2]/np.sum(other[sinks]**2,axis=1)))*(1-1e-8)
            Q=np.r_[[[0,0,-1/hmax]],other];m=halfspace_mesh(Q);st=nominate(Q,m,z,'reference height limit')
            if m['g'][2]>=0:
                return 1.+m['g'][2]/np.max(np.linalg.norm(m['X'],axis=1))
            slabs=SlabMass(m);height=float(brentq(slabs.centroid,hmax*1e-7,hmax,xtol=1e-12))
            Q[0,2]=-1/height;m=halfspace_mesh(Q)
            if abs(m['g']).max()>2e-9:raise ValueError('Independent final mass integration failed')
            st=nominate(Q,m,z,'actual mass closure')
            if st['S']!=1:raise ValueError('Final S1 construction check failed')
            P=m['X']-m['g'];pp,h=pairs(P,m['edges']);bars=np.maximum(0,1-h[pp[:,1]]/(P[pp[:,0]]**2).sum(1))
            value=float(max(bars,default=0)+.02*bars.sum())
            if value<best:
                best=value;row=dict(calls=calls,score=value,Pmax=float(max(bars,default=0)),P=bars.tolist(),parameters=z.tolist(),seconds=time.time()-start,**st)
                history.append(row);np.savez(out/'best.npz',Q=Q,X=m['X'],parameters=z);(out/'improvements.json').write_text(json.dumps(history,indent=2))
                print('SPIRAL_OWN110_OBJECTIVE',json.dumps({k:v for k,v in row.items() if k not in ['S_ids','U_ids','P']}),flush=True)
            return value
        except (ValueError,RuntimeError,AssertionError,QhullError,np.linalg.LinAlgError):return 3.
    bounds=[(.55,1.8),(.02,.95),(-2.6,2.6),(-1.4,1.4),(-1.,1.),(-.7,.7),(-6.,-2.3),(.08,.92),(.08,.99)]
    valid=sorted([r for r in old if 'Pmax' in r],key=lambda r:r['Pmax'])[:45]
    population=[]
    for r in valid:
        z=np.array(r['parameters']);z[6]=np.log10(z[6]);population.append(z)
    while len(population)<90:population.append(np.array([rng.uniform(a,b) for a,b in bounds]))
    try:
        # The old parameter screen omitted own-centroid checks at mass-infeasible
        # height limits. This is a direct candidate check, not a reference replay.
        for r in old:
            z=np.array(r['parameters']);z[6]=np.log10(z[6])
            if 'Pmax' not in r:evaluate(z)
        result=differential_evolution(evaluate,bounds,init=np.array(population),seed=seed,maxiter=iterations,
            updating='immediate',workers=1,tol=1e-9,atol=1e-10,polish=False)
    except Found:return
    (out/'FINITE_END.json').write_text(json.dumps(dict(calls=calls,best=best,seconds=time.time()-start,scope='Finite direct search; no qualifying body found'),indent=2))
