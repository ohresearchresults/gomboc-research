"""Direct monounstable homogeneous family with a moving axial apex.

Strict positive arrows in the literal vertex set certify referenceU1. Their
sink inequalities give the minimum axial apex height. Raising that apex until
the uniform first moment vanishes produces an ownU1 body when closure exists.
The only acceptance gate is a complete same-body own110 nomination followed
by exact verification. All genuine hulls use <=83 vertices, hence E<=243.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import pathlib,json,time
import numpy as np
from scipy.spatial import ConvexHull,QhullError
from scipy.optimize import differential_evolution,brentq
from two_branch_polar_goal import chain
from free_primal_goal import mesh_points
from geometry import arrows
from persistence_search import pairs

class Found(Exception):pass

def construct(z):
    other,margins=chain(z[:7],0,m=40);other[:,2]*=-1
    parent=other[int(np.argmin(other[:,2]))];alpha,beta=z[7:];xy=parent[:2]
    p=np.r_[alpha*xy+beta*np.sqrt(alpha*(1-alpha))*np.array([-xy[1],xy[0]]),parent[2]]
    margin=float(p@(parent-p))
    if margin<=1e-12:raise ValueError('Literal bottom-facet completion has no strict escape')
    return np.r_[other,[p,p*np.array([-1.,-1.,1.])]],dict(chain=margins,bottom=margin)

def quick_mass(X):
    h=ConvexHull(X)
    if h.equations[:,3].max()>=-1e-10:raise ValueError('Literal point hull does not contain the reference origin')
    tri=h.simplices.copy();a=X[tri];normal=np.cross(a[:,1]-a[:,0],a[:,2]-a[:,0]);flip=np.einsum('ij,ij->i',normal,h.equations[:,:3])<0
    tri[flip]=tri[flip][:,[0,2,1]];a=X[tri];six=np.einsum('ij,ij->i',a[:,0],np.cross(a[:,1],a[:,2]))
    if six.min()<=0:raise ValueError('Nonpositive oriented physical tetrahedron')
    V=six.sum()/6;g=(six[:,None]*a.sum(1)).sum(0)/(4*six.sum())
    return V,g

def run(out,scouts=2200,iterations=380,seed=936499):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);rng=np.random.default_rng(seed);calls=0;best=np.inf;minS=999;history=[];pool=[];bad={};start=time.time()
    bounds=[(.4,2.),(.04,1.54),(-3.2,3.2),(-2.,2.),(-1.4,1.4),(-.8,.8),(-6.,-2.2),(.08,.92),(.08,.99)]
    (out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes());(out/'definition.json').write_text(json.dumps(dict(seed=seed,scouts=scouts,iterations=iterations,bounds=bounds,
        maximum_vertices=83,edge_upper_bound=243,scope='Literal vertex escape chains, moving-apex own uniform mass closure; complete own census required'),indent=2))
    def nominate(X,z,stage):
        m=mesh_points(X);st=m['row']
        if 17<=st['E']<=249 and st['S']==st['U']==1:
            np.savez(out/'POTENTIAL_OWN110.npz',X=X,Q=m['Q'],parameters=z)
            (out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(calls=calls,stage=stage,**st),indent=2));raise Found()
        return m
    def evaluate(z):
        nonlocal calls,best,minS
        calls+=1
        try:
            other,witnesses=construct(z);W=arrows(other);sinks=np.flatnonzero(W.max(1)<=1e-12)
            if not len(sinks) or np.any(other[sinks,2]<=0):raise ValueError('No strict positive-z sink bound for the apex')
            rmin=float(np.max(np.sum(other[sinks]**2,axis=1)/other[sinks,2]))*(1+1e-10)
            X=np.r_[[[0.,0.,rmin]],other];m=nominate(X,z,'minimum apex, actual centre');g=m['g']
            if g[2]>=0:score=1+float(g[2]/np.max(np.linalg.norm(X,axis=1)))
            else:
                def centroid(r):
                    Y=X.copy();Y[0,2]=r;return float(quick_mass(Y)[1][2])
                high=rmin*2
                while centroid(high)<0 and high<1000*rmin:high*=2
                if centroid(high)<0:raise ValueError('No mass bracket within explicit finite apex domain')
                r=brentq(centroid,rmin,high,xtol=1e-12);X[0,2]=r;m=nominate(X,z,'uniform mass-closed apex')
                if np.max(abs(m['g']))>2e-9:raise ValueError('Independent maximal-facet volume integration failed mass closure')
                if m['row']['U']!=1:raise ValueError('Own unstable census contradicts the strict chain construction')
                pp,h=pairs(m['R'],m['eq']);bars=1-h[pp[:,1]]/np.sum(m['R'][pp[:,0]]**2,axis=1)
                score=float(max(bars,default=0)+.02*bars.sum());st=m['row']
                if score<best or st['S']<minS:
                    improved=score<best;best=min(best,score);minS=min(minS,st['S']);row=dict(calls=calls,score=score,Qmax=float(max(bars,default=0)),Qbars=bars.tolist(),parameters=list(z),seconds=time.time()-start,**st)
                    history.append(row);p=out/f'candidate{calls:06d}';p.mkdir();np.savez(p/'body.npz',X=X,Q=m['Q'],parameters=z)
                    (p/'summary.json').write_text(json.dumps(row,indent=2));(p/'witnesses.json').write_text(json.dumps(witnesses,indent=2))
                    if improved:np.savez(out/'best.npz',X=X,Q=m['Q'],parameters=z)
                    (out/'improvements.json').write_text(json.dumps(history,indent=2));print('PRIMAL_CHAIN_OWN110',json.dumps({k:v for k,v in row.items() if k not in ['parameters','Qbars']}),flush=True)
            if calls<=scouts:pool.append((score,np.array(z)))
            return score
        except (ValueError,RuntimeError,AssertionError,QhullError,np.linalg.LinAlgError) as error:
            key=str(error).split('\n')[0];bad[key]=bad.get(key,0)+1;return 4.
    try:
        for _ in range(scouts):evaluate(np.array([rng.uniform(a,b) for a,b in bounds]))
        pop=[z for _,z in sorted(pool,key=lambda t:t[0])[:45]]
        while len(pop)<90:pop.append(np.array([rng.uniform(a,b) for a,b in bounds]))
        (out/'scout.json').write_text(json.dumps(dict(calls=calls,feasible=len(pool),best=best,minS=minS,failures=bad),indent=2))
        differential_evolution(evaluate,bounds,init=np.array(pop),seed=seed,maxiter=iterations,workers=1,updating='immediate',tol=1e-9,atol=1e-10,polish=False)
    except Found:return
    (out/'FINITE_END.json').write_text(json.dumps(dict(calls=calls,best=best,minS=minS,failures=bad,seconds=time.time()-start,
        scope='Finite direct actual-mass search ended without a qualifying body'),indent=2))

if __name__=='__main__':
    import sys
    run(sys.argv[1],int(sys.argv[2]) if len(sys.argv)>2 else 2200,int(sys.argv[3]) if len(sys.argv)>3 else 380)
