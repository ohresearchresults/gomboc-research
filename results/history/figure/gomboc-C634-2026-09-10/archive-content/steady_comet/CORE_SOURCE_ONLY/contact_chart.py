"""Reference-conditioned rational contact chart from a planar incidence graph."""
import itertools,json,numpy as np
from numeric import recover

def make_chart(q,points,groups,grid=10**12,prefer='supports'):
    # points[0] is the fixed (0,0,1) anchor; groups[j] lists incident supports.
    n=len(q);X=np.vstack([q,points]);N=len(X);assert np.linalg.norm(points[0]-[0,0,1])<1e-7
    adj=[set() for _ in range(N)]
    for j,cy in enumerate(groups):
        for i in cy:adj[i].add(n+j);adj[n+j].add(i)
    todo=set(range(N))-{n};deleted=[]
    while todo:
        candidates=[i for i in todo if len(adj[i])<=3]
        assert candidates,'incidence graph has a nonempty 4-core'
        if prefer=='supports':key=lambda i:(i>=n,len(adj[i]),-i)
        elif prefer=='points':key=lambda i:(i<n,len(adj[i]),-i)
        else:key=lambda i:(len(adj[i]),-i)
        i=min(candidates,key=key);deps=sorted(adj[i]);deleted.append((i,deps));todo.remove(i)
        for j in deps:adj[j].remove(i)
        adj[i].clear()
    plan=[];depth={n:0}
    for i,deps in reversed(deleted):
        k=len(deps)
        axes=max(itertools.combinations(range(3),k),key=lambda ax:abs(np.linalg.det(X[np.ix_(deps,ax)]))) if k else ()
        if k:assert abs(np.linalg.det(X[np.ix_(deps,axes)]))>1e-16,(i,deps,axes)
        plan.append([i,deps,list(axes)]);depth[i]=1+max([depth[j] for j in deps],default=-1)
    gen=dict(n_supports=n,grid=grid,controls=np.rint(X*grid).astype(np.int64).tolist(),groups=groups,plan=plan)
    return gen,depth

if __name__=='__main__':
    import sys
    from pathlib import Path
    from fractions import Fraction as F
    from atlas_opt import Atlas,optimize
    from numeric import mechanics
    sys.set_int_max_str_digits(0);R=Path(__file__).parent
    a=json.loads((R/'H213_exact.json').read_text());P=np.array([[float(F(t)) for t in x] for x in a['P']]);q=np.array([[float(F(t)) for t in x] for x in a['Q']]);c=np.array([float(F(t)) for t in a['centroid']]);x=P-c;n=q/(1-q@c)[:,None]
    scale=np.linalg.norm(x[2]);z=x[2]/scale;aux=np.eye(3)[np.argmin(abs(z))];e1=np.cross(aux,z);e1/=np.linalg.norm(e1);e2=np.cross(z,e1);O=np.array([e1,e2,z])
    pp=x@O.T/scale;qq=n@O.T*scale;pp[2]=[0,0,1]
    order=[2]+[i for i in range(len(P)) if i!=2];groups=[a['faces'][i] for i in order];points=pp[order]
    gen,depth=make_chart(qq,points,groups,grid=10**13,prefer='supports')
    (R/'H213_PRIMAL_CHART_GENERATOR.json').write_text(json.dumps(gen,sort_keys=True,separators=(',',':')))
    (R/'H213_primal_faces.json').write_text(json.dumps(a['primal_faces'],separators=(',',':')))
    rec=recover(gen);print('depth',max(depth.values()),'recovererror',np.max(abs(rec-np.vstack([qq,points]))),flush=True)
    r=mechanics(rec[:137],a['primal_faces'],tol=1e-12);print('H213_RECHART',r,flush=True)
    model=Atlas(gen,a['primal_faces'],stable=23,unstable=2);st=model.state(model.u0);print('nfree',model.np,'mine',st['vals'].min(),'minpos',st['vals'][st['vals']>0].min(),'bad',np.flatnonzero(st['vals']<0).tolist(),flush=True)
    np.savez(R/'H213_chart_gauge.npz',rotation=O,scale=scale,centroid=c,reference_q=qq,reference_p=pp)
    u,st,msg=optimize(model,steps=300,trust=1e-5,keep=1e-6,goal=5e-5)
    model.save(u,R/'H213_FULLSPACE_RESULT_GENERATOR.json');print('H213_FULLSPACE_DONE',msg,st['vals'].min(),st['gaps'][~model.inc].min(),flush=True)
