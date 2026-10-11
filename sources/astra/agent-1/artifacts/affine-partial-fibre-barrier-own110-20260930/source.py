"""Uniform-centred partial-fibre shadow systems with a common affine metric.

For a fixed direction, the overlay of the upper/lower fibre diagrams is fixed
for0<tau<2. Its vertices move linearly with tau. Every physical embedding uses
the SAME A on vertices and A^-T on support normals; actual uniform moments are
integrated on that body. Complete rehulling is mandatory for any own110 hit.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import pathlib,json,time,hashlib
import numpy as np,gmpy2
from scipy.optimize import differential_evolution,minimize
from scipy.spatial import cKDTree,QhullError
from steiner_centroid_goal import steiner
from geometry import halfspace_mesh,arrows,census
from persistence_search import pairs
from cyclic_flower_mass_goal import Found

def run(source,out,directions=18,iterations=480,seed=937386,objective='census'):
    if objective not in ('census','barrier'):raise ValueError('Unknown explicit physical objective')
    source=pathlib.Path(source);out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);data=source.read_bytes();a=json.loads(data);g=list(map(gmpy2.mpq,a['centroid']));Q=[]
    for i in a['active']:
        row=list(map(gmpy2.mpq,a['raw_halfspaces'][i]));den=row[3]-sum(row[k]*g[k] for k in range(3));Q.append([float(row[k]/den) for k in range(3)])
    Q=np.array(Q);old=halfspace_mesh(Q);scale=np.sqrt(np.mean(np.sum(old['X']**2,axis=1)));Q*=scale
    rng=np.random.default_rng(seed);vecs=[q/np.linalg.norm(q) for q in Q]
    while len(vecs)<directions:vecs.append(rng.normal(size=3))
    vecs=[v/np.linalg.norm(v) for v in vecs[:directions]];np.savez(out/'centred_source.npz',Q=Q,scale=scale)
    (out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes());(out/'fibre_source.py').write_bytes(pathlib.Path('steiner_centroid_goal.py').read_bytes());(out/'definition.json').write_text(json.dumps(dict(source=str(source.resolve()),sha256=hashlib.sha256(data).hexdigest(),directions=[v.tolist() for v in vecs],seed=seed,iterations=iterations,objective=objective,isotropic_search_scale=float(scale),scope='Partial-fibre rational construction and ONE common affine physical embedding, actual own volume integration, only own110 nominates exact audit'),indent=2))
    start=time.time();history=[];bounds=[(1e-5,1.),(-2.2,2.2),(-2.2,2.2),(-4.,4.),(-4.,4.),(-4.,4.)]
    try:
        for di,v in enumerate(vecs):
            p=out/f'direction{di:02d}';p.mkdir();raw=steiner(Q,v,.5);m=halfspace_mesh(raw);E=len(m['edges'])
            if not 17<=E<=249:
                (p/'OUTSIDE_EDGE_BUDGET.json').write_text(json.dumps(dict(E=E,direction=v.tolist()),indent=2));continue
            ref=m['X'];t=ref@v;y=ref-t[:,None]*v;d=Q@v;up=np.flatnonzero(d>0);down=np.flatnonzero(d<0);upper=np.min((1-y@Q[up].T)/d[up],axis=1);lower=np.max((1-y@Q[down].T)/d[down],axis=1);mid=(upper+lower)/2
            tri=m['triangles'];edgefaces={tuple(e):[] for e in m['edges']}
            for f,cy in enumerate(m['faces']):
                for i,j in zip(cy,cy[1:]+cy[:1]):edgefaces[tuple(sorted((i,j)))].append(f)
            if any(len(x)!=2 for x in edgefaces.values()):raise ValueError('Reference fibre mesh is not closed')
            eq=np.array(list(edgefaces.values()));active=m['active'];checks=[]
            for tau in [.17,.82]:
                X=ref+(.5-tau)*mid[:,None]*v;mm=halfspace_mesh(steiner(Q,v,tau));error=float(cKDTree(mm['X']).query(X)[0].max())
                checks.append(dict(tau=tau,error=error,V=len(mm['X']),E=len(mm['edges']),F=len(mm['active'])))
                if error>2e-7 or len(mm['X'])!=len(ref) or len(mm['edges'])!=E:raise ValueError('Linear shadow system failed independent hull validation')
            (p/'shadow_checks.json').write_text(json.dumps(checks,indent=2));np.savez(p/'model.npz',Q=Q,reference_vertices=ref,midpoint=mid,direction=v,triangles=tri,active=active,primal_edges=m['edges'],polar_edges=eq)
            calls=0;best=float('inf');bestz=None;localhist=[];bad={};localstart=time.time()
            def body(z):
                tau=z[0];A=np.array([[np.exp(z[1]),z[3],z[4]],[0,np.exp(z[2]),z[5]],[0,0,np.exp(-z[1]-z[2])]])
                X=(ref+(.5-tau)*mid[:,None]*v)@A.T;H=np.linalg.solve(A.T,steiner(Q,v,tau)[active].T).T;b=X[tri];six=np.einsum('ij,ij->i',b[:,0],np.cross(b[:,1],b[:,2]));V=six.sum()/6
                if six.min()<=0 or V<=0:raise ValueError('Nonpositive physical shadow mass')
                g=(six[:,None]*b.sum(1)).sum(0)/(4*six.sum());P=X-g;den=1-H@g
                if den.min()<=0:raise ValueError('Uniform centroid outside transformed physical body')
                R=H/den[:,None];return X,H,P,R,g,A,float(V)
            def evaluate(z):
                nonlocal calls,best,bestz
                calls+=1
                try:
                    X,H,P,R,g,A,V=body(z);U=int(sum(arrows(P).max(1)<0));S=int(sum(arrows(R).max(1)<0))
                    if min(S,U)<1:return 1000.
                    if S==U==1:
                        mm=halfspace_mesh(H);check=census(mm,0)
                        if check['S']==check['U']==1 and 17<=check['E']<=249:
                            np.savez(out/'POTENTIAL_OWN110.npz',X=mm['X'],Q=H,parameters=z,direction=v,matrix=A,source_centered_Q=Q,amount=z[0]);(out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(direction_index=di,calls=calls,source=str(source.resolve()),**check),indent=2));raise Found()
                        raise ValueError('Candidate model census does not survive independent full hull reconstruction')
                    bars=[]
                    for pts,ed in [(P,m['edges']),(R,eq)]:
                        pp,h=pairs(pts,ed);bars.extend((1-h[pp[:,1]]/np.sum(pts[pp[:,0]]**2,axis=1)).tolist())
                    if objective=='census':score=float(S+U-2+.45*max(bars,default=0)+.04*sum(bars)/max(S+U-2,1))
                    else:score=float(max(bars,default=0)+.04*sum(bars))
                    if score<best:
                        best=score;bestz=np.array(z);row=dict(direction_index=di,calls=calls,score=score,S=S,U=U,E=E,V=len(ref),F=len(active),maxbar=max(bars,default=0),parameters=list(z),centroid=g.tolist(),volume=V,seconds=time.time()-localstart);localhist.append(row);np.savez(p/'best.npz',X=X,Q=H,parameters=z,direction=v,matrix=A,amount=z[0]);(p/'history.json').write_text(json.dumps(localhist,indent=2));print('AFFINE_FIBRE_GOAL',json.dumps({k:v for k,v in row.items() if k!='parameters'}),flush=True)
                    return score
                except (ValueError,RuntimeError,AssertionError,QhullError,np.linalg.LinAlgError) as err:
                    key=str(err).split('\n')[0];bad[key]=bad.get(key,0)+1;return 1000.
            pop=[np.array([t,0.,0.,0.,0.,0.]) for t in [.0001,.001,.01,.05,.2,.5,1.]]
            while len(pop)<84:
                if len(pop)<50:z=np.r_[10**rng.uniform(-5,0),rng.normal(size=5)*.3]
                else:z=np.array([rng.uniform(a,b) for a,b in bounds])
                pop.append(np.clip(z,np.array(bounds)[:,0],np.array(bounds)[:,1]))
            differential_evolution(evaluate,bounds,init=np.array(pop),seed=seed+di,maxiter=iterations,workers=1,updating='immediate',tol=1e-8,atol=1e-10,polish=False)
            if bestz is not None:minimize(evaluate,bestz,method='Nelder-Mead',bounds=bounds,options={'maxiter':1800,'xatol':1e-8,'fatol':1e-9})
            record=dict(direction=di,calls=calls,best=best,E=E,failures=bad,seconds=time.time()-start);history.append(record);(out/'history.json').write_text(json.dumps(history,indent=2));(p/'FINITE_END.json').write_text(json.dumps(record,indent=2))
    except Found:return
    (out/'FINITE_END.json').write_text(json.dumps(dict(directions=len(vecs),seconds=time.time()-start,scope='Finite common-affine partial-fibre search ended without a qualifying figure'),indent=2))

if __name__=='__main__':
    import sys
    run(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 18,int(sys.argv[4]) if len(sys.argv)>4 else 480)
