"""Negative self-polar add/cut growth and actual uniform centering.

See SELF_DUAL_CONE_BRANCH_20260930/derivation.md for the construction proof.
Search begins only after two construction steps give C>=34. All later
candidate counts are complete numerical physical counts; exact certification
is still mandatory for a potential own110.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import pathlib,json,time
import numpy as np
from scipy.spatial.distance import cdist
from scipy.spatial import QhullError
from free_primal_goal import mesh_points
from primal_chain_mass_goal import quick_mass
from geometry import arrows
from persistence_search import pairs

def transform(X,t):
    s=1+t@t;den=1-t@t-2*X@t
    if den.min()<=1e-8:raise ValueError('Orthogonal section left the positive homogeneous domain')
    return (s*X-2*(X@t)[:,None]*t[None,:]+2*t)/den[:,None]

def center(X):
    t=np.zeros(3);initial=quick_mass(X)[1];history=[]
    for it in range(30):
        Y=transform(X,t);V,g=quick_mass(Y);value=np.linalg.norm(g);history.append(value)
        if value<1e-11:return Y,dict(t=t.tolist(),initial_centroid=initial.tolist(),residual=float(value),iterations=it)
        h=1e-6;J=np.column_stack([(quick_mass(transform(X,t+np.eye(3)[j]*h))[1]-quick_mass(transform(X,t-np.eye(3)[j]*h))[1])/(2*h) for j in range(3)])
        dt=np.linalg.solve(J,-g);accepted=False
        for k in range(18):
            tt=t+dt*2**-k
            try:gg=quick_mass(transform(X,tt))[1]
            except (ValueError,QhullError):continue
            if np.linalg.norm(gg)<value*(1-1e-4*2**-k):t=tt;accepted=True;break
        if not accepted:raise ValueError('Actual mass-centering Newton path failed')
    raise ValueError('Actual mass-centering iteration limit')

def check(X):
    m=mesh_points(X);a=m['active']
    if len(a)!=len(X):raise ValueError('Paired construction retained a nonextreme point')
    q=m['Q'];dist=cdist(-X,q);error=max(float(dist.min(0).max()),float(dist.min(1).max()))
    if error>2e-8 or len(q)!=len(X) or m['row']['E']!=2*len(X)-2:raise ValueError('Independent negative self-polar hull identity failed')
    m['selfpolar_error']=error;return m

def add_cut(X,m,w,rng):
    old=X[w];face=np.flatnonzero(abs(X@old+1)<1e-8)
    if len(face)<3:raise ValueError('Opposite maximal facet absent')
    weights=rng.dirichlet(np.full(len(face),rng.choice([.3,1.,3.,10.])))
    base=weights@X[face];direction=-old/(old@old)
    slack=1+X@base;slope=X@direction;others=np.arange(len(X))!=w;lim=np.inf
    for j in np.flatnonzero(others&(slope<0)):lim=min(lim,slack[j]/(-slope[j]))
    raw=10**rng.uniform(-2.,1.2);height=min(raw,lim*rng.uniform(.04,.94))
    if height<=1e-8:raise ValueError('Add/cut has no finite admissible height')
    v=base+height*direction;sv=1+X@v
    if sv[w]>=-1e-10 or sv[others].min()<=1e-9:raise ValueError('New point does not violate exactly one strict old support')
    edges=m['ep'];neighbors=sorted(set(int(j if i==w else i) for i,j in edges if i==w or j==w));cut=[]
    for j in neighbors:
        t=(-1-v@old)/(v@(X[j]-old))
        if not 0<t<1:raise ValueError('Literal edge cut lies outside its old edge')
        cut.append(old+t*(X[j]-old))
    Y=np.r_[np.delete(X,w,axis=0),v[None,:],cut]
    if len(Y)>125:raise ValueError('Self-polar genuine complexity budget exceeded')
    mm=check(Y);return Y,mm,dict(old_vertex=int(w),new_point=v.tolist(),old_degree=len(neighbors),edge_neighbors=neighbors,height=float(height),face=face.tolist())

def assess(X):
    m=check(X);st=m['row']
    if not 17<=st['E']<=248:raise ValueError('Actual hull outside the requested complexity range')
    pp,h=pairs(m['P'],m['ep']);bars=1-h[pp[:,1]]/np.sum(m['P'][pp[:,0]]**2,axis=1)
    row=dict(**st,Pmax=float(max(bars,default=0)),Pbars=bars.tolist(),selfpolar_error=m['selfpolar_error'])
    return m,row

def run(out,trials=600,depth=22,choices=24,seed=930851):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);rng=np.random.default_rng(seed);history=[];best_count=999;best_bar=np.inf;start=time.time();failure={}
    tetra=np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],float)
    (out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes());(out/'definition.json').write_text(json.dumps(dict(trials=trials,depth=depth,choices=choices,seed=seed,
        scope='Literal negative-self-polar paired additions/cuts, common O4 physical centering, actual complete own census; exact required'),indent=2))
    def candidate(X,row,trail,label):
        nonlocal best_count,best_bar
        count=row['S']+row['U'];value=row['Pmax']
        if row['S']==row['U']==1:
            np.savez(out/'POTENTIAL_OWN110.npz',X=X,Q=-X);(out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(trail=trail,label=label,**row),indent=2));return True
        if count<best_count or count==best_count and value<best_bar:
            best_count=count;best_bar=value;p=out/f'candidate{len(history):06d}';p.mkdir();np.savez(p/'body.npz',X=X,Q=-X)
            record=dict(label=label,trail=trail,seconds=time.time()-start,**row);(p/'summary.json').write_text(json.dumps(record,indent=2));history.append(record)
            (out/'improvements.json').write_text(json.dumps(history,indent=2));np.savez(out/'best.npz',X=X,Q=-X)
            print('SELF_POLAR_OWN_GOAL',json.dumps({k:v for k,v in record.items() if k not in ['trail','Pbars']}),flush=True)
        return False
    for trial in range(trials):
        try:
            # Necessary construction intermediates, not equilibrium searches
            # below C34. Two paired additions produce V>=10,E>=18.
            X=tetra.copy();m=check(X);trail=[]
            for _ in range(2):
                X,m,step=add_cut(X,m,int(rng.integers(len(X))),rng);trail.append(step)
            X,centering=center(X);m,row=assess(X);trail.append(dict(centering=centering))
            if candidate(X,row,trail,dict(trial=trial,depth=0)):return
            for level in range(depth):
                roots=np.flatnonzero(arrows(m['P']).max(1)<0);options=[]
                for j in range(choices):
                    w=int(rng.choice(roots if j%4 else np.arange(len(X))))
                    try:
                        Y,_,step=add_cut(X,m,w,rng);Y,centering=center(Y);mm,rr=assess(Y)
                        newtrail=trail+[step,dict(centering=centering)]
                        if candidate(Y,rr,newtrail,dict(trial=trial,depth=level+1,choice=j)):return
                        # Equilibrium number is primary; the radial barrier
                        # only orders equal-census search states.
                        score=(rr['S']+rr['U'],rr['Pmax']);options.append((score,Y,mm,rr,newtrail))
                    except (ValueError,RuntimeError,AssertionError,QhullError,np.linalg.LinAlgError) as error:
                        key=str(error).split('\n')[0];failure[key]=failure.get(key,0)+1
                if not options:break
                options.sort(key=lambda x:x[0]);choice=options[0] if trial%4!=0 else options[int(rng.integers(min(4,len(options))))]
                _,X,m,row,trail=choice
        except (ValueError,RuntimeError,AssertionError,QhullError,np.linalg.LinAlgError) as error:
            key=str(error).split('\n')[0];failure[key]=failure.get(key,0)+1
        if trial%5==0:
            (out/'checkpoint.json').write_text(json.dumps(dict(trials_completed=trial+1,best_count=best_count,best_bar=best_bar,seconds=time.time()-start,failures=failure),indent=2));print('SELF_POLAR_CHECKPOINT',trial+1,best_count,best_bar,flush=True)
    (out/'FINITE_END.json').write_text(json.dumps(dict(trials=trials,best_count=best_count,best_bar=best_bar,seconds=time.time()-start,failures=failure,
        scope='Finite geometric family search; no qualifying own110 body found'),indent=2))

if __name__=='__main__':
    import sys
    run(sys.argv[1],int(sys.argv[2]) if len(sys.argv)>2 else 600,int(sys.argv[3]) if len(sys.argv)>3 else 22,int(sys.argv[4]) if len(sys.argv)>4 else 24)
