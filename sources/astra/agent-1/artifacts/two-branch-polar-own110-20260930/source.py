"""Two independent polar escape chains, actual mass, and a literal axial apex.

Each chain has20 C2 orbits. The top completion is constructed at the ACTUAL
largest polar z coordinate, not at an assumed endpoint. Thus at most83
support planes and a genuine four-plane axial vertex give E<=242 when all
planes are active. All actual hulls/centroids/equilibria are checked afresh.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import pathlib,json,time
import numpy as np
from scipy.optimize import differential_evolution,brentq
from scipy.spatial import QhullError
from geometry import halfspace_mesh,arrows,census
from persistence_search import pairs
from polyhedral_slab_mass import SlabMass

class Found(Exception):pass

def chain(parameters,phase,m=20):
    power,endgap,omega,b1,b2,b3,logdamp=parameters
    theta=(np.arange(1,m+1)/m)**power*(np.pi-endgap)
    phi=phase+omega*theta+b1*np.sin(theta)+b2*np.sin(2*theta)+b3*np.sin(3*theta)
    D=np.c_[np.sin(theta)*np.cos(phi),np.sin(theta)*np.sin(phi),-np.cos(theta)]
    parent=np.array([0.,0.,-1.]);points=[];margins=[]
    for d in D:
        mirror=parent*np.array([-1.,-1.,1.]);par=parent if d@parent>=d@mirror else mirror
        projection=d@par
        if projection<=1e-8:raise ValueError('Chain has no finite parent projection')
        q=np.exp(-10**logdamp)*projection*d;margin=float(q@(par-q))
        if margin<=1e-13:raise ValueError('Chain escape is not strict at search precision')
        points.extend([q,q*np.array([-1.,-1.,1.])]);margins.append(margin);parent=q
    return np.array(points),margins

def construct(parameters):
    z=np.asarray(parameters);a,ma=chain(z[:7],0);b,mb=chain(z[7:14],z[14]);other=np.r_[a,b]
    parent=other[int(np.argmax(other[:,2]))]
    if parent[2]<=0:raise ValueError('Polar body has no positive top level')
    alpha,beta=z[15:];xy=parent[:2];perp=np.array([-xy[1],xy[0]])
    p=np.r_[alpha*xy+beta*np.sqrt(alpha*(1-alpha))*perp,parent[2]]
    margin=float(p@(parent-p))
    if margin<=1e-12:raise ValueError('Explicit axial apex completion lacks a positive escape witness')
    return np.r_[other,[p,p*np.array([-1.,-1.,1.])]],dict(chainA=ma,chainB=mb,top=margin)

def run(out,scouts=2400,iterations=350,seed=932241):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);rng=np.random.default_rng(seed)
    calls=0;best=np.inf;minU=999;history=[];pool=[];start=time.time();bad={}
    (out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes())
    one=[(.4,2.),(.04,1.54),(-3.2,3.2),(-2.,2.),(-1.4,1.4),(-.8,.8),(-6.,-2.2)]
    bounds=one+one+[(0,np.pi),(.08,.92),(.08,.99)]
    (out/'definition.json').write_text(json.dumps(dict(seed=seed,scouts=scouts,iterations=iterations,bounds=bounds,
        support_rows=83,scope='Two literal polar escape branches, own mass and complete numerical census; exact audit required for any110'),indent=2))
    def nominate(Q,m,z,stage):
        st=census(m,0)
        if 17<=st['E']<=249 and st['S']==st['U']==1:
            np.savez(out/'POTENTIAL_OWN110.npz',Q=Q,X=m['X'],parameters=z)
            (out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(calls=calls,stage=stage,**st),indent=2));raise Found()
        return st
    def evaluate(z):
        nonlocal calls,best,minU
        calls+=1
        try:
            other,witnesses=construct(z);W=arrows(other);sinks=np.flatnonzero(W.max(1)<=1e-12)
            if not len(sinks) or np.any(other[sinks,2]>=0):raise ValueError('No strict negative-z polar sink bound')
            hmax=float(np.min(-other[sinks,2]/np.sum(other[sinks]**2,axis=1)))*(1-1e-10)
            Q=np.r_[[[0,0,-1/hmax]],other];m=halfspace_mesh(Q);st=nominate(Q,m,z,'height limit actual centre')
            if m['g'][2]>=0:score=1+float(m['g'][2]/np.max(np.linalg.norm(m['X'],axis=1)))
            else:
                slabs=SlabMass(m);height=brentq(slabs.centroid,hmax*1e-7,hmax,xtol=1e-12)
                Q[0,2]=-1/height;m=halfspace_mesh(Q)
                if np.max(abs(m['g']))>2e-9:raise ValueError('Independent own volume-centroid closure failed')
                st=nominate(Q,m,z,'mass closed body')
                if st['S']!=1:raise ValueError('Actual stable census contradicts strict escape construction')
                P=m['X']-m['g'];pp,h=pairs(P,m['edges']);bars=1-h[pp[:,1]]/np.sum(P[pp[:,0]]**2,axis=1)
                score=float(max(bars,default=0)+.02*bars.sum())
                if score<best or st['U']<minU:
                    best=min(best,score);minU=min(minU,st['U']);row=dict(calls=calls,score=score,P=bars.tolist(),Pmax=float(max(bars,default=0)),parameters=list(z),seconds=time.time()-start,**st)
                    history.append(row);p=out/f'candidate{calls:06d}';p.mkdir();np.savez(p/'body.npz',Q=Q,X=m['X'],parameters=z)
                    (p/'summary.json').write_text(json.dumps(row,indent=2));(p/'witnesses.json').write_text(json.dumps(witnesses,indent=2))
                    np.savez(out/'best.npz',Q=Q,X=m['X'],parameters=z);(out/'improvements.json').write_text(json.dumps(history,indent=2))
                    print('TWO_BRANCH_OWN110',json.dumps({k:v for k,v in row.items() if k not in ['S_ids','U_ids','P','parameters']}),flush=True)
            if calls<=scouts:pool.append((score,np.array(z)))
            return score
        except (ValueError,RuntimeError,AssertionError,QhullError,np.linalg.LinAlgError) as error:
            key=str(error).split('\n')[0];bad[key]=bad.get(key,0)+1
            return 4.
    try:
        for i in range(scouts):
            z=np.array([rng.uniform(a,b) for a,b in bounds])
            if i%3==0:
                # Explicit correlated subfamily: same path, independently
                # rotated. Other samples keep both chains fully independent.
                z[7:14]=z[:7]
            evaluate(z)
        population=[z for _,z in sorted(pool,key=lambda t:t[0])[:60]]
        while len(population)<120:population.append(np.array([rng.uniform(a,b) for a,b in bounds]))
        (out/'scout.json').write_text(json.dumps(dict(calls=calls,feasible=len(pool),best=best,minU=minU,failures=bad),indent=2))
        differential_evolution(evaluate,bounds,init=np.array(population),seed=seed,maxiter=iterations,workers=1,
            updating='immediate',tol=1e-9,atol=1e-10,polish=False)
    except Found:return
    (out/'FINITE_END.json').write_text(json.dumps(dict(calls=calls,best=best,minU=minU,failures=bad,seconds=time.time()-start,
        scope='Finite direct search ended without a qualifying figure'),indent=2))

if __name__=='__main__':
    import sys
    run(sys.argv[1],int(sys.argv[2]) if len(sys.argv)>2 else 2400,int(sys.argv[3]) if len(sys.argv)>3 else 350)
