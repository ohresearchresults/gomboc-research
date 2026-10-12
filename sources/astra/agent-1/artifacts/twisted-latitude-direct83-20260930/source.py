"""Direct under-budget physical support search from twisted latitudes.

At most83 support planes, with a literal four-plane axial vertex and one
axial bottom facet. All other planes occur in half-turn pairs. The actual
uniform centroid and all equilibria are recomputed on every physical hull.
Smooth-body calculations motivate seeds only and certify none of these hulls.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import pathlib,json,time
import numpy as np
from scipy.spatial import QhullError
from geometry import halfspace_mesh,census,arrows
from persistence_search import pairs,polar_edges


def seed(epsilon,k,phase,apex,bottom,slope,m=39,latitude_power=1.):
    w=-.96+1.9*(np.arange(m)+.5)/m
    w=np.sign(w)*abs(w)**latitude_power
    phi=(np.arange(m)*np.pi*(3-np.sqrt(5))+phase)%np.pi
    u=np.sqrt(1-w*w)*np.cos(phi);v=np.sqrt(1-w*w)*np.sin(phi)
    co=np.cos(k*u);si=np.sin(k*u)
    n=np.c_[u,v*co+w*si,-v*si+w*co]
    f=n[:,2]*co+n[:,1]*si
    grad=np.c_[k*(n[:,1]*co-n[:,2]*si),si,co]
    grad-=np.einsum('ij,ij->i',n,grad)[:,None]*n
    radius=1+epsilon*f
    q=n/radius[:,None]-epsilon*grad/radius[:,None]**2
    # Deliberately retire supports that would cut off the requested apex.
    # This is a new literal H-body, not an inherited smooth-body assertion.
    q=q[q[:,2]<1/apex-1e-6]
    rotate=np.array([-1.,-1.,1.]);normals=np.r_[q,q*rotate]
    angles=phase+np.arange(4)*np.pi/2
    top=np.c_[slope*np.cos(angles),slope*np.sin(angles),np.full(4,1/apex)]
    return np.r_[[[0.,0.,-1/bottom]],top,normals]


def score(H):
    m=halfspace_mesh(H);st=census(m,0)
    if not 17<=st['E']<249:raise ValueError('Outside explicit edge range')
    if abs(m['g'][:2]).max()>1e-8:raise ValueError('Half-turn mass symmetry failed')
    if 0 not in m['active']:raise ValueError('The axial stable facet is absent')
    axial=np.flatnonzero(np.linalg.norm(m['X'][:,:2],axis=1)<1e-7)
    if not len(axial):raise ValueError('The designated axial vertex is absent')
    P=m['X']-m['g'];Q=H[m['active']];Q=Q/(1-Q@m['g'])[:,None]
    pu=int(axial[np.argmax(P[axial,2])]);sq=int(np.where(m['active']==0)[0][0])
    vals=[]
    for A,r in [(P,pu),(Q,sq)]:
        vv=arrows(A).max(1);vv[r]*=-1;vals.extend(vv)
    merit=float(np.maximum(1e-7-np.array(vals),0).sum())
    bp,hp=pairs(P,m['edges']);eq=polar_edges(m);bq,hq=pairs(H/(1-H@m['g'])[:,None],eq)
    pp=1-hp[bp[:,1]]/(P[bp[:,0]]**2).sum(1)
    allQ=H/(1-H@m['g'])[:,None];qq=1-hq[bq[:,1]]/(allQ[bq[:,0]]**2).sum(1)
    return dict(merit=merit,Pmax=max(pp,default=0),Qmax=max(qq,default=0),**st),m


def run(out,trials=2200,seed_value=973813):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);rng=np.random.default_rng(seed_value)
    history=[];best=np.inf;best_count=999;start=time.time()
    (out/'definition.json').write_text(json.dumps(dict(trials=trials,seed=seed_value,
        supports_at_most=83,edge_bound=3*83-6,scope='Direct physical own110 search, exact verification only on qualifying nominations'),indent=2))
    (out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes())
    for i in range(trials):
        epsilon=float(rng.choice([.035,.05,.08,.12,.2,.35,.5,.65]))
        k=float(rng.uniform(2.5,7.));phase=float(rng.uniform(0,np.pi))
        apex=float(1+epsilon+rng.uniform(-.02,.3));bottom=float(rng.uniform(.55,1.15))
        slope=float(rng.uniform(.08,.8));power=float(rng.uniform(.6,1.8))
        params=dict(epsilon=epsilon,k=k,phase=phase,apex=apex,bottom=bottom,slope=slope,latitude_power=power)
        H=seed(**params)
        try:
            row,m=score(H);row.update(trial=i,parameters=params,seconds=time.time()-start)
            if row['merit']<best or row['S']+row['U']<best_count:
                p=out/f'trial{i:05d}';p.mkdir();np.savez(p/'body.npz',Q=H,X=m['X'])
                (p/'summary.json').write_text(json.dumps(row,indent=2));row['folder']=str(p.resolve())
                best=min(best,row['merit']);best_count=min(best_count,row['S']+row['U'])
                print('TWISTED_DIRECT_BEST',json.dumps({k:v for k,v in row.items() if k not in ['S_ids','U_ids']}),flush=True)
            if row['S']==row['U']==1 and min(row['min_primal_nonroot'],row['min_polar_nonroot'])>1e-9:
                np.savez(out/'POTENTIAL_OWN110.npz',Q=H,X=m['X']);(out/'POTENTIAL_OWN110.json').write_text(json.dumps(row,indent=2));return
        except (ValueError,QhullError,np.linalg.LinAlgError) as error:row=dict(trial=i,parameters=params,error=repr(error))
        history.append(row)
        if i%25==0:(out/'history.json').write_text(json.dumps(history,indent=2))
    (out/'history.json').write_text(json.dumps(history,indent=2))
